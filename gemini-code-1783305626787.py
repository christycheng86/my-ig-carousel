import io
import zipfile
import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# --- 頁面基本設定 ---
st.set_page_config(page_title="專業級 IG 輪播文產生器 + AI 爆款內容箱", layout="wide")
st.title("🎨 專業級 IG 輪播文自動生成工具 (3:4 直式)")
st.write("✨ **目前版本：雙字體獨立控制 + AI 爆款文案產生器（方案 B 免費版）**")

# --- 🌟 【新功能】方案 B：AI 爆款文案提示詞工具箱 ---
st.markdown("---")
with st.expander("🚀 🔥 點開此處：AI 爆款內容產生器 (IG / Threads 萬用提示詞)", expanded=True):
    st.subheader("💡 步驟：在下方輸入主題 ➔ 選擇爆款公式 ➔ 複製指令丟給免費 AI ➔ 貼回下方做圖！")
    
    # 用戶輸入主題與領域
    ai_topic = st.text_input("1. 請輸入你想寫的【主題/關鍵字】", placeholder="例如：時間管理、低卡減肥美食、職場溝通技巧...")
    ai_target = st.text_input("2. 請輸入你的【目標受眾/痛點】", placeholder="例如：經常加班的上班族、想吃甜食又怕胖的人...")
    
    # 爆款公式選擇
    prompt_style = st.selectbox(
        "3. 選擇爆款文案公式框架",
        [
            "【反常識爆款法】(打破常規，Threads與IG點閱率極高)",
            "【痛點共鳴與具體解法】(吸粉與儲存量最高的萬用公式)",
            "【黃金3步驟教學法】(最適合做成IG輪播圖的實用乾貨)"
        ]
    )
    
    # 根據選擇動態生成 Prompt
    base_prompt = ""
    if prompt_style == "【反常識爆塊法】(打破常規，Threads與IG點閱率極高)":
        base_prompt = f"""你是一位精通 Instagram 和 Threads 的自媒體百萬社群專家。
請幫我針對主題「{ai_topic}」，針對「{ai_target}」這群受眾，撰寫一組「反常識、打破傳統思維」的爆款內容。

請嚴格依照以下格式輸出：

【1. IG 輪播圖專用文案 (請直接給我每頁的文字內容)】
第 1 頁 (封面)：[請給出一個極度吸睛、顛覆認知的標題]
第 2 頁 (痛點)：[指出大家目前的盲點，為什麼傳統做法沒用]
第 3 頁 (反轉)：[給出一個反直覺、讓人驚訝的核心觀點]
第 4 頁 (結論/金句)：[用一句話總結這個觀點，並加上呼籲留言互動的行動指標]

【2. Threads 專用短貼文 (短小精悍、容易引發轉發)】
[請寫出一段 150 字內、帶有強烈個人觀點、扎心且容易引發共鳴或爭論的 Threads 短文，結尾引導大家討論]

【3. IG 貼文下方長文案】
[包含吸引人的開頭、詳細補充說明、5個相關Hashtags]"""

    elif prompt_style == "【痛點共鳴與具體解法】(吸粉與儲存量最高的萬用公式)":
        base_prompt = f"""你是一位精通 Instagram 和 Threads 的自媒體百萬社群專家。
請幫我針對主題「{ai_topic}」，針對「{ai_target}」這群受眾，撰寫一組「痛點共鳴與具體解法」的爆款內容。

請嚴格依照以下格式輸出：

【1. IG 輪播圖專用文案 (請直接給我每頁的文字內容)】
第 1 頁 (封面)：[扎心的痛點問句，例如：你是不是也常常...]
第 2 頁 (共鳴)：[描述受眾的真實慘狀，讓他們覺得被理解]
第 3 頁 (解法)：[給出 2-3 個馬上能用的具體行動步驟]
第 4 頁 (呼籲)：[提醒他們儲存這篇貼文，並在留言區分享想法]

【2. Threads 專用短貼文 (高互動率)】
[寫出一段語氣像朋友聊天、一針見血指出痛點並給出核心建議的 Threads 貼文，結尾留一個問句引發留言]

【3. IG 貼文下方長文案】
[包含開頭共鳴、詳細步驟拆解、5個相關Hashtags]"""

    else:
        base_prompt = f"""你是一位精通 Instagram 和 Threads 的自媒體百萬社群專家。
請幫我針對主題「{ai_topic}」，針對「{ai_target}」這群受眾，撰寫一組「黃金3步驟教學法」的實用乾貨內容。

請嚴格依照以下格式輸出：

【1. IG 輪播圖專用文案 (請直接給我每頁的文字內容)】
第 1 頁 (封面)：[乾貨標題，例如：新手必學！3步驟輕鬆學會...]
第 2 頁 (步驟 1 & 2)：[簡短說明前兩個核心步驟]
第 3 頁 (步驟 3)：[說明最關鍵的第三個步驟]
第 4 頁 (頁尾呼籲)：[引導收藏、追蹤，以及轉發到限時動態]

【2. Threads 專用短貼文】
[列點式的乾貨分享，語氣爽快、含金量高，讓人看完想立刻收藏的 Threads 短文]

【3. IG 貼文下方長文案】
[詳細的步驟補充說明、5個相關Hashtags]"""

    st.text_area("📋 點選下方文字方塊 ➔ 複製（Ctrl+A 然後 Ctrl+C）這段終極 Prompt 去餵給 AI：", value=base_prompt, height=300)
st.markdown("---")


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
st.sidebar.header("🔤 字體與預設顏色設定")
uploaded_title_font = st.sidebar.file_uploader("1. 上傳【標題】專用字體", type=["ttf", "otf", "ttc"], key="title_font_uploader")
uploaded_body_font = st.sidebar.file_uploader("2. 上傳【內文/頁尾】專用字體", type=["ttf", "otf", "ttc"], key="body_font_uploader")

title_size = st.sidebar.slider("預設標題大小", min_value=20, max_value=200, value=75)
body_size = st.sidebar.slider("預設內文大小", min_value=15, max_value=120, value=42)
footer_size = st.sidebar.slider("預設頁尾大小", min_value=15, max_value=80, value=28)

default_title_color = st.sidebar.color_picker("全域預設【標題】顏色", value="#1A1A1A")
default_body_color = st.sidebar.color_picker("全域預設【內文】顏色", value="#333333")

title_y_pos = st.sidebar.slider("標題垂直位置 (Y)", min_value=50, max_value=600, value=250)
body_y_pos = st.sidebar.slider("內文垂直位置 (Y)", min_value=250, max_value=1100, value=480)

if uploaded_title_font is not None:
    try: font_title = ImageFont.truetype(io.BytesIO(uploaded_title_font.read()), title_size)
    except: font_title = ImageFont.load_default()
else: font_title = ImageFont.load_default()

if uploaded_body_font is not None:
    try:
        font_body = ImageFont.truetype(io.BytesIO(uploaded_body_font.read()), body_size)
        uploaded_body_font.seek(0)
        font_footer = ImageFont.truetype(io.BytesIO(uploaded_body_font.read()), footer_size)
    except: font_body = font_footer = ImageFont.load_default()
else: font_body = font_footer = ImageFont.load_default()

# --- 側邊欄：輪播內容與背景設定 ---
st.sidebar.markdown("---")
st.sidebar.header("📝 輪播內容設定")
ig_handle = st.sidebar.text_input("Instagram 帳號 (頁尾顯示)", value="@your_studio")
num_pages = st.sidebar.number_input("總頁數", min_value=1, max_value=10, value=4)

pages_data = []
for i in range(num_pages):
    st.sidebar.markdown(f"---")
    st.sidebar.subheader(f"第 {i+1} 頁設定")
    title = st.sidebar.text_input(f"標題 {i+1}", f"這是第 {i+1} 頁的標題")
    p_title_color = st.sidebar.color_picker(f"第 {i+1} 頁【標題】顏色", value=default_title_color, key=f"t_color_{i}")
    
    body = st.sidebar.text_area(f"內文 {i+1}", f"在這裡貼上 AI 幫你寫的第 {i+1} 頁內文文案。")
    p_body_color = st.sidebar.color_picker(f"第 {i+1} 頁【內文】顏色", value=default_body_color, key=f"b_color_{i}")
    
    bg_type = st.sidebar.selectbox(f"第 {i+1} 頁背景類型", ["單色背景", "漸層背景", "上傳底圖"], key=f"bg_type_{i}")
    
    bg_info = {
        "title": title, "body": body, "bg_type": bg_type, 
        "title_color": p_title_color, "body_color": p_body_color
    }
    
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

    # 繪製標題
    title_lines = wrap_text(page["title"], font_title, PAGE_WIDTH - 200)
    current_y = title_y_pos
    for line in title_lines:
        draw.text((start_x + 100, current_y), line, fill=page["title_color"], font=font_title)
        bbox = font_title.getbbox(line)
        current_y += (bbox[3] - bbox[1]) + 15

    # 繪製內文
    body_lines = wrap_text(page["body"], font_body, PAGE_WIDTH - 200)
    current_y = body_y_pos
    for line in body_lines:
        draw.text((start_x + 100, current_y), line, fill=page["body_color"], font=font_body)
        bbox = font_body.getbbox(line)
        current_y += (bbox[3] - bbox[1]) + 15

    # 繪製頁尾
    footer_text = f"{i+1}/{num_pages}  |  {ig_handle}"
    draw.text((start_x + 100, PAGE_HEIGHT - 120), footer_text, fill="#A0A0A0", font=font_footer)

if num_pages > 1:
    draw.ellipse([PAGE_WIDTH - 100, 670, PAGE_WIDTH + 100, 870], fill="#FF6B6B")

# --- 網頁前端預覽與下載處理 ---
st.subheader("🖼️ 輪播文即時預覽")

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
