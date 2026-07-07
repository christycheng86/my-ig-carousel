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
    
    # 爆款公式選擇 (加入 FUFU AI LAB 心理測驗標籤流)
    prompt_style = st.selectbox(
        "3. 選擇爆款文案公式框架",
        [
            "【全新】FUFU AI LAB 風格：黑天使心理測驗/標籤定義流",
            "【反常識爆款法】(打破常規，Threads與IG點閱率極高)",
            "【痛點共鳴與具體解法】(吸粉與儲存量最高的萬用公式)",
            "【黃金3步驟教學法】(最適合做成IG輪播圖的實用乾貨)"
        ]
    )
    
    # 根據選擇動態生成 Prompt
    base_prompt = ""
    if prompt_style == "【全新】FUFU AI LAB 風格：黑天使心理測驗/標籤定義流":
        base_prompt = f"""你是一位精通 Instagram 和 Threads 演算法的自媒體百萬社群行銷專家、大眾心理學與玄學大師。
請幫我針對主題「{ai_topic}」，針對「{ai_target}」這群受眾，撰寫一組高品質、高轉發的【5頁 IG 輪播文文案】。風格請嚴格參考熱門的「黑天使系心理測驗」對號入座標籤流。

【嚴格執行避坑與高級詞彙規則】：
- 絕不直接出現「賺錢、副業、創業、金錢、收入、投資、虧損、發財、暴富、算命、八字、生命靈數」等直白字眼。
- 必須使用高級替代詞：開拓第二曲線、打造個人賽道、啟動新局、解鎖變現通道、商業實踐、增長、拿結果、碎銀、真金白銀、籌碼、成本、學費、沉沒代價、資源、底氣、財富週期、天賦密碼、命運底層代碼、個人週期表、能量配置、自帶的說明書。

【語言與詞彙規則】：
- 語言：使用地道香港廣東話（結合少量專業術語）。
- 請自然融入像是「講句難聽啲、骨格精奇、倒錢落海、死火、執生、踢爆」等廣東話口語。
- 語氣：直接、專業、細膩、銳利，具備優雅的撕裂感。

請嚴格依照以下格式輸出：

【1. IG 輪播圖專用文案 (每頁字數請極度精煉，少於 80 字，方便直接複製做圖)】
- PAGE 1 (封面)：[具有強烈心理衝擊力、心理測驗或標籤流的廣東話大標題]
- PAGE 2 (內耗標籤定義)：[為這個主題精準定義一個極具高級感的人格標籤（例如：貪婪的自噬者 / 精緻的逃避者 / 安全感的囚徒），並用優雅而毒舌的筆觸描述他們的真實慘狀、盲目反思與內耗]
- PAGE 3 (底層痛點拆解)：[引入玄學或心理學反轉角度，拆解為什麼他們會卡在「白天安分、晚上失眠、煞錯位」的死火現狀]
- PAGE 4 (破局允許/天賦通道)：[給予順應天賦密碼、在對的週期收斂或看清自己人生說明書的具體出路解法]
- PAGE 5 (高價值收藏 CTA)：[引導留字互動，例如：【立刻儲存】。留言區留下你的選項，我話你知點樣順勢增長]

【2. Threads 專用短貼文 (扎心且引發瘋狂轉發)】
[寫出一段短小精悍、帶有強烈觀點、一針見血戳中這種內耗人格的廣東話短文，結尾引導轉發或討論]"""

    elif prompt_style == "【反常識爆款法】(打破常規，Threads與IG點閱率極高)" or prompt_style == "【反常識爆塊法】(打破常規，Threads與IG點閱率極高)":
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
请幫我針對主題「{ai_topic}」，針對「{ai_target}」這群受眾，撰寫一組「黃金3步驟教學法」的實用乾貨內容。

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
st.sidebar
