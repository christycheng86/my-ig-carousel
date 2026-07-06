import io
import zipfile
import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# --- 頁面基本設定 ---
st.set_page_config(page_title="專業級 IG 輪播文產生器 + 終極 AI 爆款大腦", layout="wide")
st.title("🎨 專業級 IG 輪播文自動生成工具 (3:4 直式)")
st.write("✨ **目前版本：雙字體控制 + 終極 AI 爆款內容箱（融合 6 大自媒體流派）**")

# --- 🌟 【新功能】方案 B：終極 AI 爆款公式庫 ---
st.markdown("---")
with st.expander("🚀 🔥 點開此處：終極 AI 爆款內容產生器 (最新私藏公式庫)", expanded=True):
    st.subheader("💡 步驟：輸入主題 ➔ 選擇私藏爆款流派 ➔ 複製終極指令去餵 AI ➔ 貼回下方做圖！")
    
    # 用戶輸入主題與領域
    ai_topic = st.text_input("1. 請輸入你想寫的【主題/關鍵字】", value="生命靈數x八字", placeholder="例如：生命靈數x八字、職場溝通、低卡美食...")
    ai_target = st.text_input("2. 請輸入你的【目標受眾/痛點/標籤】", value="想利用副業增加收入與創業既人，但同時又怕投入及損失大量金錢、甚至又唔知自己應該做咩行業的人", placeholder="例如：想創業又怕虧錢的迷茫上班族...")
    
    # 爆款公式選擇 (完整封裝用戶提供的精華)
    prompt_style = st.selectbox(
        "3. 選擇私藏爆款流派框架",
        [
            "【反常識/反直覺流】(Steve Koh 風格，撕裂認知、高情緒共鳴)",
            "【標籤定義與數字震撼流】(身分認同、出生日期與特質對號入座)",
            "【苦難翻盤與極致對比流】(欲揚先抑、命運重新框架、少走彎路)",
            "【低認知負載與否定恐懼流】(清單式乾貨、沒做這事等於白做、好用到回不去)",
            "【特定群體精準避坑流】(創業/合夥團隊/契合反差、具象化後果)",
            "【迷因反差與場景召喚流】(當我以為...翻車短劇、那一天場景痛點)"
        ]
    )
    
    # 建立強大提示詞邏輯
    base_prompt = f"""你是一位精通 Instagram、Threads 既自媒體百萬社群行銷專家、玄學與大眾心理學大師。
現在要針對主題「{ai_topic}」，以及目標受眾/痛點「{ai_target}」，撰寫一組極具感染力、直擊人性的爆款內容。

請根據我選擇的【爆款流派：{prompt_style}】，嚴格依照該流派的文字結構、語氣和以下指定格式輸出。"""

    if "【反常識/反直覺流】" in prompt_style:
        base_prompt += f"""
        
【流派核心邏輯】
運用「反常識心態鉤子」＋「場景化痛點/狀態描繪」＋「給予允許/底層解法」＋「高價值/情感共鳴 CTA」。
善用句型：「再次提醒，你越【做某件反直覺的放鬆/放下動作】，【某個大眾渴望的正面結果】就會越好。」

【⚠️ 避坑指南（請在撰寫時嚴格遵守）】
1. 切忌變成人性「毒雞湯」：不要只是一味叫人放鬆，必須給出背後的底層邏輯（如「心流」與「接納」的科學/心理學/命理能量學解釋），否則內容會顯得空洞、神棍。
2. 語氣不要居高臨下：不要用「教育、訓斥」的口吻，要用「同行者、分享者」的姿態去寫。

【輸出格式要求】
1. IG 輪播圖專用文案 (請給出每頁文字)：
   - 第 1 頁 (封面)：[反常識顛覆認知鉤子，直擊受眾盲點]
   - 第 2 頁 (痛點拆解)：[描繪受眾日常行為盲點，為什麼傳統努力反而讓你虧錢或迷茫]
   - 第 3 頁 (解法與底層邏輯)：[帶入生命靈數/八字的核心觀點，給出反直覺的具體落地方案]
   - 第 4 頁 (金句結尾)：[套用「再次提醒...越放鬆結果越好」句型，高價值收藏型 CTA]

2. Threads 專用短貼文：
   - 語氣像朋友真誠聊天、一針見血。約 150-200 字，文字極具撕裂認知的殺傷力，引導正反兩派留言大亂鬥。

3. IG 貼文下方長文案與 5 個 Hashtags。"""

    elif "【標籤定義與數字震撼流】" in prompt_style:
        base_prompt += f"""
        
【流派核心邏輯】
【身份認同/測試型鉤子】 + 【數字震撼/標籤對座】 + 【1-10級由弱到強的痛點/爽點遞進】。
善用句型：
-「出生日期看你的【某種隱藏能力/特質】！有【數字 A、B、C】嘅人注意！」
-「表面【特質 X】但內心其實【特質 Y】嘅出生日期，中咗嘅出聲！」
-【特定人群/高價值標籤】+【命理/身體特徵】+【多半/一定具備某種超能力/特質】

【輸出格式要求】
1. IG 輪播圖專用文案 (請給出每頁文字)：
   - 第 1 頁 (封面)：[用身分與震撼數字召喚，例如：命盤帶這三樣/這幾個出生日期的人注意]
   - 第 2 頁 (特質對座)：[表面特質 X 與內心特質 Y 的極致對比，讓受眾驚呼「太準了」]
   - 第 3 頁 (1-10級痛點遞進)：[從弱到強列出這群人在創業/副業上遇到的層層迷茫與虧錢恐懼]
   - 第 4 頁 (引導互動)：[標籤化對號入座，呼籲在留言區出聲、交流]

2. Threads 專用短貼文：
   - 用廣東話/流暢口語風格，寫一段極易引發轉發和「中咗！」對號入座的互動短文。

3. IG 貼文下方長文案與 5 個 Hashtags。"""

    elif "【苦難翻盤與極致對比流】" in prompt_style:
        base_prompt += f"""
        
【流派核心邏輯】
【特定領域真相】 ＋ 【痛苦重新框架 + 願景轉移】 ＋ 【心理儀式/少走彎路型 CTA】。
善用句型：
-【極致的成就/好命】+【往往伴隨著極致的痛苦/代價】（例如：大富大貴的格局，前半生都熬過這三個劫）
-「分享一個【領域】真相：【特定標籤】的人，早年一定會【經歷某種特定痛苦】。」
-「如果你總是...你可能拿到了靈數 X 的劇本。聽完這段話，你會少走 10 年彎路...」

【輸出格式要求】
1. IG 輪播圖專用文案 (請給出每頁文字)：
   - 第 1 頁 (封面)：[結果先行 + 命運/神聖對比高潮公式，例如：帶給你有天賦的數字，也藏著最大業障]
   - 第 2 頁 (苦難框架)：[重新詮釋受眾目前的「迷茫與怕虧錢」，告訴他們這是大格局前半生必經的劫]
   - 第 3 頁 (翻盤劇本)：[利用生命靈數/八字指出如何從這個痛苦中醒來，完成轉移]
   - 第 4 頁 (呼籲)：[少走10年彎路的心理儀式型 CTA，引導收藏]

2. Threads 專用短貼文：
   - 強調「少走彎路」、「命運重新框架」，寫出一段直擊心靈、看完讓人想立刻收藏轉發的扎心金句文。

3. IG 貼文下方長文案與 5 個 Hashtags。"""

    elif "【低認知負載與否定恐懼流】" in prompt_style:
        base_prompt += f"""
        
【流派核心邏輯】
【否定/恐懼型鉤子（XX沒做這件事＝白做）】＋【超低門檻＋超高回報承諾】＋【步驟化乾貨（低認知負載清單）】＋【存檔/私訊型 CTA】。
善用句型：
-「第一次用 [工具/方法] 冇做呢 [數字] 件事，就同冇用過一樣。」
-「如果你 [做某件事] 煞咗呢個位，咁同冇做過一模一樣。」

【輸出格式要求】
1. IG 輪播圖專用文案 (請給出每頁文字)：
   - 第 1 頁 (封面)：[否定恐懼鉤子：副業/創業不看這個靈數/八字煞到位，等於白做、好用到回不去]
   - 第 2 頁 (步驟清單 1 & 2)：[超低負載的清單拆解，不要給受眾大腦負擔]
   - 第 3 頁 (核心步驟 3)：[給出最關鍵、高回報的命理避坑盲點與解法]
   - 第 4 頁 (強烈呼籲)：[價值錨定，引導私訊或存檔收藏]

2. Threads 專用短貼文：
   - 清爽列點式、含金量極高的乾貨分享，讓人看完有強烈的「獲得感」，忍不住想 Bookmark。

3. IG 貼文下方長文案與 5 個 Hashtags。"""

    elif "【特定群體精準避坑流】" in prompt_style:
        base_prompt += f"""
        
【流派核心邏輯】
【特定群體標籤（創業/合夥人/團隊）】+ 【精準週期/命理契合反差觀點】+ 【誇張化/具象化的公司命運後果】。

【輸出格式要求】
1. IG 輪播圖專用文案 (請給出每頁文字)：
   - 第 1 頁 (封面)：[鎖定合夥人/團隊群體，拋出靈數X八字契合反差的震撼標題]
   - 第 2 頁 (合夥盲點)：[拆解精準週期中，為什麼跟某類八字的人合作會導致公司命運翻車]
   - 第 3 頁 (避坑方案)：[給出具體的篩選或互補落地方案，化解虧錢風險]
   - 第 4 頁 (呼籲)：[轉發給合夥人看，或者降維打擊式轉化 CTA]

2. Threads 專用短貼文：
   - 商業語氣中帶有命理精準度，戳中創業者最怕「隊友神助攻還是豬隊友」的痛點，引發高轉發。

3. IG 貼文下方長文案與 5 個 Hashtags。"""

    else:
        base_prompt += f"""
        
【流派核心邏輯】
【迷因式反差情境開頭】＋ 【理想與現實翻車自嘲/短劇】＋ 【專業反轉/場景痛點召喚】 ＋ 【福利型 LINE/私訊導流 CTA】。
善用句型：「當你 30 歲那年，突然發現自己為別人活了一輩子的那天…… 其實你的生命靈數早就警告過你了。」（複製 'The day you...' 场景感）

【輸出格式要求】
1. IG 輪播圖專用文案 (請給出每頁文字)：
   - 第 1 頁 (封面)：[當我以為...迷因式反差開頭，或者「那一天」場景痛點召喚]
   - 第 2 頁 (翻車情境)：[理想與現實的強烈對比自嘲，具象化受眾因為不懂命盤而虧錢、迷茫的慘狀]
   - 第 3 頁 (專業反轉)：[大反轉！神聖對比，給出生命靈數核心恐懼的真正救贖解法]
   - 第 4 頁 (導流呼籲)：[指令式轉化，引導點擊連結領取專屬命盤福利]

2. Threads 專用短貼文：
   - 畫面感極強的內心獨白式（Internal Monologue）強鈎子短文，極易引發粉絲在留言區分享自己的「翻車故事」。

3. IG 貼文下方長文案與 5 個 Hashtags。"""

    st.text_area("📋 點選下方文字方塊 ➔ 複製（Ctrl+A 然後 Ctrl+C）這段終極 Prompt 去餵給 AI：", value=base_prompt, height=400)
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
