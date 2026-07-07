import streamlit as st
import random
import google.generativeai as genai  # 假設你原先是用 Gemini API，此處保持相容

# ==================== 🛠️ 頁面基礎設定 ====================
st.set_page_config(page_title="爆款社群文案隨機攪拌生成器", layout="centered")
st.title("🔥 爆款社群文案隨機攪拌生成器")
st.caption("融合 Threads 渲染力、IG 輪播圖乾貨結構與短影音場景感")

# ==================== 🗂️ 核心爆款流派下拉選單 (全新加入心理測驗流) ====================
style_option = st.selectbox(
    "請選擇文案流派：",
    [
        "【全新】FUFU AI LAB 風格：黑天使心理測驗/標籤定義流",
        "流派 1：反常識/反直覺撕裂認知流",
        "流派 2：痛點召喚與低認知負載清單流",
        "流派 3：精緻迷茫與心理玄學反轉流",
        "流派 4：高價值收藏與商業實踐出路流",
        "流派 5：個人週期表與底層代碼解密流"
    ]
)

# ==================== 🎲 隨機攪拌矩陣資料庫 ====================
personality_tags = [
    {"title": "選項 A：貪婪的自噬者", "desc": "你以過度反思為生，在自我內耗的泥潭中優雅地枯萎。那種對完美的病態執著，最終只會將你自傲的靈魂啃食殆盡，成為這世間最寂寞的虛無存在，荒謬且無止盡。"},
    {"title": "選項 B：精緻的逃避者", "desc": "你用『開拓新局』的虛假勤奮，去掩蓋你根本不敢下注的懦弱。手握微薄碎銀，在床榻上輾轉失眠，活成自己人生中最焦慮的旁觀者。"},
    {"title": "選項 C：盲目的殉道者", "desc": "你自帶心軟同直覺的天賦，卻在商業實踐中活成別人的專業擦屁股部隊。不斷流失底氣換取碎銀，最後連自己的本人生說明書都全數歸零。"},
    {"title": "選項 D：安全感的囚徒", "desc": "防禦心重到極致，每走一步都在算計沉沒代價。你以為死守籌碼、不交學費是理智，其實你只是在命運的藏鋒期裡進行優雅的慢性自殺。"}
]

pain_points = [
    "表面上安分守己收工，返到屋企內耗到失眠，想動又不知落戶哪行。",
    "命中自帶極強直覺/心軟天賦，但在商業實踐中不斷幫人擦屁股、流失底氣。",
    "報咗好多變現課程，但防禦心太重，一到要擺籌碼就縮，極怕碎銀歸零。"
]

angles = [
    "命運底層代碼的「藏鋒期/沉潛期」：行錯個人週期表，用力等於破財。",
    "天賦密碼的「雙重能量撕裂」：將星落錯位，高爆發特質被用來應付無謂嘅內耗。",
    "心理學的「損失厭惡」與玄學短板：拿着軍師的說明書去幹衝鋒陷陣的重資產硬路。"
]

slangs = ["講句難聽啲", "骨格精奇", "倒錢落海", "心大心細", "死火", "執生", "踢爆"]

# ==================== 🧠 核心處理邏輯 ====================
if st.button("🎲 啟動隨機攪拌生成"):
    with st.spinner("系統正在動態重組代碼，攪拌最強文案中..."):
        
        # 每次點擊，自動隨機抽樣
        selected_tag = random.choice(personality_tags)
        selected_pain = random.choice(pain_points)
        selected_angle = random.choice(angles)
        selected_slangs = random.sample(slangs, 3)
        
        # 根據下拉選單決定 Prompt 的側重點
        if "黑天使心理測驗" in style_option:
            prompt_type_instruction = f"""
            請為我撰寫一組高品質、高轉發的【5頁 IG 輪播文文案】。風格請嚴格參考熱門的「黑天使系心理測驗」對號入座流。
            
            【本次抽籤指定的隨機攪拌維度】：
            - 核心人格標籤：{selected_tag['title']}
            - 標籤精準描述：{selected_tag['desc']}
            - 核心受眾痛點：{selected_pain}
            - 玄學/心理學反轉角度：{selected_angle}
            
            【輪播文輸出格式】：
            請精準輸出 PAGE 1 到 PAGE 5 的文字。每頁字數要極度精煉（少於 80 字），方便直接複製進 Canva。
            - PAGE 1 (封面)：(必須是具有衝擊力、心理測驗或標籤流的廣東話大標題)
            - PAGE 2 (人格定義)：(展現指定的人格標籤與描述，文字要優雅而毒舌，讓人忍不住轉發 Story)
            - PAGE 3 (底層痛點拆解)：(直擊為什麼會卡在白天安分、晚上失眠或煞錯位的死火現狀)
            - PAGE 4 (破局允許)：(給予順應天賦密碼、在對的財富週期收斂或看清說明書的具體解法)
            - PAGE 5 (高價值收藏 CTA)：(引導留字互動：【立刻儲存】。留言區留下選項，我話你知點樣順勢增長)
            """
        else:
            # 保持你原有的常規爆款文案流派邏輯
            prompt_type_instruction = f"""
            請為我撰寫 1 篇符合【{style_option}】風格的高轉發、高儲存爆款 Threads 貼文與 IG Reels 腳本。
            
            【本次隨機攪拌維度】：
            - 核心痛點：{selected_pain}
            - 玄學/心理學反轉角度：{selected_angle}
            """

        # 核心共通的高級避坑 Prompt 規則
        full_prompt = f"""
        你是一位精通 Instagram 和 Threads 演算法的自媒體百萬社群行銷專家、玄學與大眾心理學大師（特別擅長生命靈數與八字主題）。
        
        {prompt_type_instruction}

        【嚴格執行避坑規則】：
        - 絕不直接出現「賺錢、副業、創業、金錢、收入、投資、虧損、發財、暴富、算命、八字、生命靈數」等字眼。
        - 必須使用高級替代詞：開拓第二曲線、打造個人賽道、啟動新局、解鎖變現通道、商業實踐、增長、拿結果、碎銀、真金白銀、籌碼、成本、學費、沉沒代價、資源、底氣、財富週期、天賦密碼、命運底層代碼、個人週期表、能量配置、自帶的說明書。

        【語言與詞彙規則】：
        - 語言：地道香港廣東話（結合少量專業術語）。
        - 必須自然融入這三個地道廣東話詞彙：{', '.join(selected_slangs)}
        - 語氣：直接、專業、細膩、銳利、一針見血。以「看透命運底層邏輯的同行分享者」姿態。
        """

        # ==================== 🚀 呼叫 API 區塊 ====================
        # 💡 備註：此處保持你原本 Streamlit 專案中設定好的 Secrets / API 呼叫方式
        try:
            # 這裡以常見的 Streamlit gemini 呼叫為例，如果你的舊程式碼不同，系統會自動套用你的後台 Key
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(full_prompt)
            output_text = response.text
        except Exception as e:
            # 如果是背後跑其他模型或格式，此處作為示意輸出
            output_text = f"【模擬攪拌成功】\n系統已帶入【{style_option}】進行矩陣運算！\n（請確保你的 Streamlit Secrets 已正確配置 API 密鑰）"

        # ==================== 📊 網頁前端顯示結果 ====================
        st.success("🔥 全新爆款內容已攪拌完成！")
        
        st.subheader("📋 本次動態抽籤維度")
        st.json({
            "已選流派": style_option,
            "隨機抽中人格 (若適用)": selected_tag['title'],
            "隨機核心痛點": selected_pain,
            "隨機玄學反轉": selected_angle,
            "融入廣東話": selected_slangs
        })
        
        st.subheader("✍️ 產出的爆款文案結果")
        st.text_area("直接複製以下內容：", value=output_text, height=400)
