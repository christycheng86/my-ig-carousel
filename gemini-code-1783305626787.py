import io
import zipfile
import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# --- 頁面基本設定 ---
st.set_page_config(page_title="玄學創業爆款產生器", layout="wide")
st.title("🔮 玄學創業爆款產生器 (生命靈數 x 八字)")
st.write("✨ **目前版本：全客製化品牌大腦（5×5×5 終極矩陣輸出，全面避開限流詞）**")

# --- 🌟 【新功能】方案 B：玄學創業品牌大腦 Master Prompt ---
st.markdown("---")
with st.expander("🚀 🔥 點開此處：複製【個人品牌玄學創業】5x5x5 終極爆款指令", expanded=True):
    st.subheader("💡 步驟：點擊下方文字框 ➔ 全選複製 ➔ 丟給免費 AI，即刻吐出 15 篇神級爆款文案！")
    
    # 固定的核心品牌提示詞
    brand_prompt = f"""你是一位精通 Instagram 和 Threads 演算法的自媒體百萬社群行銷專家、玄學與大眾心理學大師。
現在，請完全切換為我指定的【個人品牌人設】與【文案輸出規則】，為我撰寫一整套高轉發、高儲存的爆款內容矩陣。

---

### 👤 品牌人設與受眾定位
1. 目標受眾：【專針對想利用副業增加收入及想創業既人，但同時又怕投入及損失大量金錢、甚至又唔知自己應該做什麼行業的人】。他們的心態是：渴望改變，但防禦心極重（怕輸錢）、極度迷茫。
2. 核心服務：【利用生命靈數 X 八字幫客戶搵出佢既財富週期，帶領客戶輕鬆創業賺取財富】。
3. 輸出語氣：【直接、專業、細膩、銳利、一針見血】。字字珠璣、絕不拖泥帶水、不灌毒雞湯、不用居高臨下的說教口吻，而是以「看透命運底層邏輯的同行分享者」姿態，給予驚醒與允許。
4. 語言風格：【必需地道香港廣東話（結合少量專業術語）】，用最入骨、最生活化的廣東話直擊痛點，讓人一睇就明、感同身受。

---

### ⚠️ 社群發佈與避坑規則（極重要）
1. 嚴格避開所有平台敏感與限流用詞：
   - 絕不直接出現「賺錢、副業、創業、金錢、收入、投資、虧損、發財、暴富、算命、八字、生命靈數」等字眼。
   - 必須使用【安全詞/高級替代詞】：
     * 「副業/創業/增加收入」 ➔ 改用【開拓第二曲線、打造個人賽道、啟動新局、解鎖變現通道、商業實踐、增長、拿結果】。
     * 「金錢/收入/虧損」 ➔ 改用【碎銀、真金白銀、籌碼、成本、學費、沉沒代價、資源、底氣、財富週期】。
     * 「算命/八字/生命靈數」 ➔ 改用【天賦密碼、命運底層代碼、個人週期表、能量配置、自帶的說明書】。
2. 內容切忌變空洞：不要只叫人放鬆或盲目衝動，必須給出背後結合「天賦密碼（靈數）與週期表（八字）」的底層能量學與心理學合理解釋。

---

### 📦 任務需求：請嚴格依照以下格式，產出 15 篇完整腳本文案：

#### 🟢 第一部分：5 個短影片 (IG Reels) 完整腳本
（結構：0-3秒黃金吸睛鉤子 ➔ 痛點共鳴 ➔ 一針見血的玄學核心反轉 ➔ 行動引導。純文字版本）
- 腳本 1：【反常識/反直覺流】（主題：越想用力變現反而越破財，如何順應個人週期表）
- 腳本 2：【標籤定義與數字震撼流】（主題：出生日期自帶的隱藏天賦，表面佛系內心焦慮）
- 腳本 3：【苦難翻盤與極致對比流】（主題：前半生走得極辛苦的人，天賦密碼裡藏著什麼大格局）
- 腳本 4：【低認知負載清單流】（主題：啟動新局前沒搞懂這 3 個天賦代碼，等於白忙）
- 腳本 5：【場景痛點召喚流】（主題：直擊面臨 30 歲/中年迷茫、怕交沉沒代價的人）

#### 🔵 第二部分：5 個 (THREADS) 完整貼文文案
（結構：短小精悍、語氣極度銳利、撕裂認知。200-300字內，結尾留一個能夠引發正反兩派在留言區大亂鬥或瘋狂對號入座的問句）
- 文案 1：再次提醒，你越是不去討好任何人，你的天賦密碼運作得越好。
- 文案 2：帶給你有天賦的那組數字，往往也是藏著你一生最大考驗的數字。
- 文案 3：大富大貴的格局，前半生都熬過這三個劫。聊聊為什麼你現在還在迷茫。
- 文案 4：如果你每次想啟動新賽道都煞錯位，咁同冇做過一模一樣。
- 文案 5：分享一個商業真相：有些人自帶的說明書就不適合加盟開實體店，別再送學費了。

#### 🟡 第三部分：5 個 (IG) 完整四頁輪播文案
（結構：條列化、標題清楚。請詳細寫出第 1 頁到第 5 頁的精準文字，每頁字數適中(50字內)，第 5 頁為高價值收藏型 CTA）
- 輪播文 1：【反常識顛覆認知】（封面：為什麼算命說你適合當老闆，你卻注定賠學費？）
- 輪播文 2：【數字震撼/標籤對座】（封面：出生日期看你的隱藏變現能力！有這幾個數字嘅人注意！）
- 輪播文 3：【結果先行+少走彎路】（封面：如果你總是莫名其妙心軟被坑，你可能拿到了這組數字的劇本）
- 輪播文 4：【特定群體精準避坑】（封面：找合夥人團隊不看這兩點，公司注定翻車）
- 輪播文 5：【迷因式反差情境】（封面：當我以為只要努力就能解鎖新賽道…… 直到我看了自己的天賦密碼）

---
請直接開始輸出，必需保持【直接、細膩、銳利、地道廣東話】的語氣，標題清楚，條列化。"""

    st.text_area("📋 點選下方文字方塊 ➔ 複製（Ctrl+A 然後 Ctrl+C）這段終極品牌大腦 Prompt：", value=brand_prompt, height=500)
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
    
    body = st.sidebar.text_area(f"內文 {i+1}", f"在這裡貼上 AI 根據公式生成的第 {i+1} 頁文案。")
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
