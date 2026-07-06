import io
import zipfile
import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# --- 頁面基本設定 ---
st.set_page_config(page_title="專業級 IG 輪播文產生器 (3:4)", layout="wide")
st.title("🎨 專業級 IG 輪播文自動生成工具 (3:4 直式)")
st.write("這個版本已將圖片尺寸調整為 **1080x1440 (3:4)**！支援字體上傳、漸層背景、自訂底圖與自動換行。")

# --- 輔助函式：自動文字換行 ---
def wrap_text(text, font, max_width):
    lines = []
    current_line = ""
    for char in text:
        if char == '\n':
            lines.append(current_line)
            current_line = ""
            continue
        test_line = current_line + char
        bbox = font.getbbox(test_line)
        width = bbox[2] - bbox[0]
        if width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = char
    if current_line:
        lines.append(current_line)
    return lines

# --- 輔助函式：繪製漸層背景 ---
def draw_vertical_gradient(draw, rect, color1, color2):
    x1, y1, x2, y2 = rect
    h = y2 - y1
    c1 = tuple(int(color1.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    c2 = tuple(int(color2.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    for y in range(y1, y2):
        r = int(c1[0] + (c2[0] - c1[0]) * (y - y1) / h)
        g = int(c1[1] + (c2[1] - c1[1]) * (y - y1) / h)
        b = int(c1[2] + (c2[2] - c1[2]) * (y - y1) / h)
        draw.line([(x1, y), (x2, y)], fill=(r, g, b))

# --- 側邊欄：全域樣式與字體設定 ---
st.sidebar.header("🔤 全域樣式與字體")

# 1. 字體上傳
uploaded_font = st.sidebar.file_uploader("上傳中文字體 (.ttf 或 .otf)", type=["ttf", "otf"])

# 2. 字體大小滑桿
title_size = st.sidebar.slider("標題字體大小", min_value=20, max_value=120, value=65)
body_size = st.sidebar.slider("內文字體大小", min_value=15, max_value=80, value=38)
footer_size = st.sidebar.slider("頁尾字體大小", min_value=15, max_value=60, value=28)

# 3. 字體顏色與位置
text_color = st.sidebar.color_picker("字體顏色", value="#1A1A1A")
title_y_pos = st.sidebar.slider("標題垂直位置 (Y)", min_value=50, max_value=500, value=250)
body_y_pos = st.sidebar.slider("內文垂直位置 (Y)", min_value=250, max_value=1000, value=480)

# 4. 載入字體邏輯
if uploaded_font is not None:
    font_bytes = io.BytesIO(uploaded_font.read())
    try:
        font_title = ImageFont.truetype(font_bytes, title_size)
        font_bytes.seek(0)
        font_body = ImageFont.truetype(font_bytes, body_size)
        font_bytes.seek(0)
        font_footer = ImageFont.truetype(font_bytes, footer_size)
    except Exception as e:
        st.sidebar.error(f"字體載入失敗: {e}")
        font_title = font_body = font_footer = ImageFont.load_default()
else:
    st.sidebar.warning("⚠️ 目前使用系統預設字體（中文會變亂碼）。建議點擊上方「Browse files」上傳任何中文字體檔（如微軟正黑體、思源黑體 .ttf）！")
    font_title = font_body = font_footer = ImageFont.load_default()

# --- 側邊欄：輪播內容與背景設定 ---
st.sidebar.markdown("---")
st.sidebar.header("📝 輪播內容設定")
ig_handle = st.sidebar.text_input("Instagram 帳號 (頁尾顯示)", value="@your_studio")
num_pages = st.sidebar.number_input("總頁數", min_value=1, max_value=10, value=4)

pages_data = []
for i in range(num_pages):
    st.sidebar.markdown(f"---")
    st.sidebar.subheader(f"第 {i+1} 頁設定")
    title = st.sidebar.text_input(f"標題 {i+1}", f"第一天" if i == 0 else f"這是第 {i+1} 頁的標題")
    body = st.sidebar.text_area(f"內文 {i+1}", f"好日子" if i == 0 else f"輸入文字，這個版本會自動幫你換行。")
    
    bg_type = st.sidebar.selectbox(f"第 {i+1} 頁背景類型", ["單色背景", "漸層背景", "上傳底圖"], key=f"bg_type_{i}")
    bg_info = {"title": title, "body": body, "bg_type": bg_type}
    
    if bg_type == "單色背景":
        bg_info["bg_color"] = st.sidebar.color_picker(f"背景顏色 {i+1}", value="#F7F9FC", key=f"color_{i}")
    elif bg_type == "漸層背景":
        bg_info["grad_color1"] = st.sidebar.color_picker(f"漸層起點色 {i+1}", value="#4A90E2", key=f"g1_{i}")
        bg_info["grad_color2"] = st.sidebar.color_picker(f"漸層終點色 {i+1}", value="#50E3C2", key=f"g2_{i}")
    elif bg_type == "上傳底圖":
        bg_info["bg_image"] = st.sidebar.file_uploader(f"上傳底圖 {i+1} (建議 1080x1440)", type=["png", "jpg", "jpeg"], key=f"img_{i}")
        
    pages_data.append(bg_info)

# --- 核心圖片繪製與處理 ---
PAGE_WIDTH = 1080
PAGE_HEIGHT = 1440  
total_width = PAGE_WIDTH * num_pages

canvas = Image.new("RGB", (total_width, PAGE_HEIGHT), color="#FFFFFF")
draw = ImageDraw.Draw(canvas)

for i, page in enumerate(pages_data):
    start_x = i * PAGE_WIDTH
    rect = [start_x, 0, start_x + PAGE_WIDTH, PAGE_HEIGHT]
    
    if page["bg_type"] == "單色背景":
        draw.rectangle(rect, fill=page.get("bg_color", "#FFFFFF"))
    elif page["bg_type"] == "漸層背景":
        draw_vertical_gradient(draw, rect, page.get("grad_color1", "#FFFFFF"), page.get("grad_color2", "#CCCCCC"))
    elif page["bg_type"] == "上傳底圖":
        if page.get("bg_image") is not None:
            try:
                bg_img = Image.open(page["bg_image"]).convert("RGB")
                bg_img = bg_img.resize((PAGE_WIDTH, PAGE_HEIGHT), Image.Resampling.LANCZOS)
                canvas.paste(bg_img, (start_x, 0))
            except Exception as e:
                st.error(f"第 {i+1} 頁背景圖載入出錯: {e}")
                draw.rectangle(rect, fill="#F0F0F0")
        else:
            draw.rectangle(rect, fill="#EAEAEA")
            draw.text((start_x + 300, 700), "請在左側上傳 1080x1440 底圖...", fill="#888888", font=font_body)

    title_lines = wrap_text(page["title"], font_title, PAGE_WIDTH - 200)
    current_y = title_y_pos
    for line in title_lines:
        draw.text((start_x + 100, current_y), line, fill=text_color, font=font_title)
        bbox = font_title.getbbox(line)
        current_y += (bbox[3] - bbox[1]) + 15

    body_lines = wrap_text(page["body"], font_body, PAGE_WIDTH - 200)
    current_y = body_y_pos
    for line in body_lines:
        draw.text((start_x + 100, current_y), line, fill=text_color, font=font_body)
        bbox = font_body.getbbox(line)
        current_y += (bbox[3] - bbox[1]) + 15

    footer_text = f"{i+1}/{num_pages}  |  {ig_handle}"
    draw.text((start_x + 100, PAGE_HEIGHT - 120), footer_text, fill="#A0A0A0", font=font_footer)

if num_pages > 1:
    draw.ellipse([PAGE_WIDTH - 100, 670, PAGE_WIDTH + 100, 870], fill="#FF6B6B")

# --- 網頁前端預覽與下載處理 ---
st.subheader("🖼️ 輪播文即時預覽 (左右滑動即為 IG 呈現效果)")

cols = st.columns(num_pages)
zip_buffer = io.BytesIO()

with zipfile.ZipFile(zip_buffer, "w") as zip_file:
    for i in range(num_pages):
        start_x = i * PAGE_WIDTH
        box = (start_x, 0, start_x + PAGE_WIDTH, PAGE_HEIGHT)
        page_img = canvas.crop(box)
        
        with cols[i]:
            st.image(page_img, caption=f"第 {i+1} 頁預覽 (1080x1440)", use_container_width=True)
            
        img_buffer = io.BytesIO()
        page_img.save(img_buffer, format="PNG")
        zip_file.writestr(f"slide_{i+1}.png", img_buffer.getvalue())

st.markdown("---")
st.download_button(
    label="📥 打包下載所有圖片 (ZIP)",
    data=zip_buffer.getvalue(),
    file_name="ig_carousel_1440.zip",
    mime="application/zip"
)
