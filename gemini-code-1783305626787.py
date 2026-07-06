import io
import zipfile
from PIL import Image, ImageDraw, ImageFont
import streamlit as st

# --- 頁面基本設定 ---
st.set_page_config(page_title="IG 輪播文產生器", layout="wide")
st.title("🎨 IG 輪播文自動生成工具 (4:5 直式)")
st.write("在左側輸入內容，右側可預覽並下載切片後的圖片！")

# --- 初始化字體 ---
# 網頁版建議將 .ttf/.ttc 字體檔案放在與 app.py 同個資料夾內，確保部署到雲端時字體不會失效
try:
    # 這裡以常見的中文字體為例，你可以替換成你喜歡的字體檔名
    font_title = ImageFont.truetype("msjh.ttc", 60)
    font_body = ImageFont.truetype("msjh.ttc", 40)
    font_footer = ImageFont.truetype("msjh.ttc", 30)
except IOError:
    # 如果找不到，預設使用系統字體（不支援中文，僅作備份）
    font_title = font_body = font_footer = ImageFont.load_default()

# --- 左側控制面板：編輯內容 ---
st.sidebar.header("📝 輪播文內容設定")
ig_handle = st.sidebar.text_input(
    "Instagram 帳號 (頁尾顯示)", value="@your_studio"
)
num_pages = st.sidebar.number_input(
    "總頁數", min_value=1, max_value=10, value=3
)

pages_data = []
for i in range(num_pages):
    st.sidebar.markdown(f"---")
    st.sidebar.subheader(f"第 {i+1} 頁")
    title = st.sidebar.text_input(f"標題 {i+1}", f"這是第 {i+1} 頁的標題")
    body = st.sidebar.text_area(f"內文 {i+1}", f"這是內文描述...\n可以換行。")
    bg_color = st.sidebar.color_picker(
        f"背景顏色 {i+1}", value="#F7F9FC" if i % 2 == 0 else "#E3E9F2"
    )

    pages_data.append({"title": title, "body": body, "bg_color": bg_color})

# --- 核心圖片處理與繪製 ---
PAGE_WIDTH = 1080
PAGE_HEIGHT = 1350
total_width = PAGE_WIDTH * num_pages

# 建立超大畫布
canvas = Image.new("RGB", (total_width, PAGE_HEIGHT), color="#FFFFFF")
draw = ImageDraw.Draw(canvas)

# 繪製每一頁
for i, page in enumerate(pages_data):
    start_x = i * PAGE_WIDTH

    # 背景
    draw.rectangle(
        [start_x, 0, start_x + PAGE_WIDTH, PAGE_HEIGHT], fill=page["bg_color"]
    )

    # 標題
    draw.text((start_x + 100, 200), page["title"], fill="#1A1A1A", font=font_title)

    # 內文
    draw.text((start_x + 100, 400), page["body"], fill="#4A4A4A", font=font_body)

    # 頁尾
    footer_text = f"{i+1}/{num_pages}  |  {ig_handle}"
    draw.text(
        (start_x + 100, PAGE_HEIGHT - 120),
        footer_text,
        fill="#A0A0A0",
        font=font_footer,
    )

# 範例跨頁裝飾（在第1頁與第2頁之間畫一個圓）
if num_pages > 1:
    draw.ellipse(
        [PAGE_WIDTH - 100, 600, PAGE_WIDTH + 100, 800], fill="#FF6B6B"
    )

# --- 右側預覽與下載 ---
st.subheader("🖼️ 輪播文預覽 (左右滑動即為 IG 呈現效果)")

# 將大畫布切片，並存入記憶體供使用者下載
output_images = []
cols = st.columns(num_pages)  # 網頁上並排顯示預覽

# 建立一個記憶體內的 ZIP 檔
zip_buffer = io.BytesIO()
with zipfile.ZipFile(zip_buffer, "w") as zip_file:
    for i in range(num_pages):
        start_x = i * PAGE_WIDTH
        box = (start_x, 0, start_x + PAGE_WIDTH, PAGE_HEIGHT)
        page_img = canvas.crop(box)

        # 在網頁上顯示預覽
        with cols[i]:
            st.image(page_img, caption=f"第 {i+1} 頁", use_container_width=True)

        # 將圖片轉為 bytes 存入 ZIP
        img_buffer = io.BytesIO()
        page_img.save(img_buffer, format="PNG")
        zip_file.writestr(f"slide_{i+1}.png", img_buffer.getvalue())

# 下載按鈕
st.markdown("---")
st.download_button(
    label="📥 打包下載所有圖片 (ZIP)",
    data=zip_buffer.getvalue(),
    file_name="ig_carousel.zip",
    mime="application/zip",
)