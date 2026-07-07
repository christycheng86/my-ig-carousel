import random
import os
from openai import OpenAI
from dotenv import load_dotenv

# 1. 自動讀取 .env 檔案
load_dotenv()

# 2. 檢查並初始化 OpenAI Client
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    # 這裡方便你如果沒設定環境變數，也可以直接貼上 sk-...
    api_key = "你的_OPENAI_API_KEY_貼在這裡" 

client = OpenAI(api_key=api_key)

# ==================== 💥 核心隨機攪拌矩陣 ====================

# 心理測驗/對號入座人格標籤 (新加入：FUFU AI LAB 風格)
personality_tags = [
    {"title": "選項 A：貪婪的自噬者", "desc": "你以過度反思為生，在自我內耗的泥潭中優雅地枯萎。那種對完美的病態執著，最終只會將你自傲的靈魂啃食殆盡。"},
    {"title": "選項 B：精緻的逃避者", "desc": "你用『尋找新局』的虛假勤奮，去掩蓋你不敢下注的懦弱。手握微薄碎銀，在床榻上輾轉失眠，活成最焦慮的旁觀者。"},
    {"title": "選項 C：盲目的殉道者", "desc": "你自帶心軟的天賦，卻在商業實踐中活成別人的擦屁股部隊。出賣靈魂換取碎銀，最後連自己的底氣都全數歸零。"},
    {"title": "選項 D：安全感的囚徒", "desc": "防禦心重到極致，每走一步都在算計沉沒代價。你以為死守籌碼是理智，其實你只是在命運的藏鋒期裡慢性自殺。"}
]

pain_points = [
    "表面上安分守己收工，返到屋企內耗到失眠，想動又不知落戶哪行。",
    "命中自帶極強直覺/心軟天賦，但在商業實踐中不斷幫人擦屁股、流失底氣。",
    "報咗好多變現課程，但防禦心太重，一到要擺籌碼就縮。"
]

angles = [
    "命運底層代碼的「藏鋒期/沉潛期」：行錯個人週期表，用力等於破財。",
    "天賦密碼的「雙重能量撕裂」：將星落錯位，高爆發特質被用來應付辦公室政治。",
    "心理學的「損失厭惡」與玄學短板：拿着軍師的說明書去幹衝鋒陷陣的重資產硬路。"
]

slangs = ["講句難聽啲", "骨格精奇", "倒錢落海", "死火", "執生", "踢爆"]

# ==================== 🎲 抽籤攪拌核心 ====================
selected_tag = random.choice(personality_tags)
selected_pain = random.choice(pain_points)
selected_angle = random.choice(angles)
selected_slangs = random.sample(slangs, 3)

# ==================== 📝 高級 Prompt 組裝 ====================
prompt = f"""
你是一位精通 Instagram 和 Threads 演算法的自媒體百萬社群行銷專家、玄學與大眾心理學大師。
請為我撰寫一組高品質、高轉發的【5頁 IG 輪播文文案】。風格請參考熱門的「黑天使系心理測驗」對號入座流。

【嚴格執行避坑規則】：
- 絕不直接出現「賺錢、副業、創業、金錢、收入、投資、虧損、發財、暴富、算命、八字、生命靈數」等字眼。
- 必須使用高級替代詞：開拓第二曲線、打造個人賽道、解鎖變現通道、商業實踐、增長、拿結果、碎銀、真金白銀、籌碼、成本、學費、沉沒代價、資源、底氣、財富週期、天賦密碼、命運底層代碼、個人週期表、能量配置、自帶的說明書。

【本次抽籤指定的人格標籤維度】：
- 核心人格標籤：{selected_tag['title']}
- 標籤精準文案：{selected_tag['desc']}
- 核心受眾痛點：{selected_pain}
- 玄學/心理學反轉角度：{selected_angle}
- 必須融入的地道廣東話詞彙：{', '.join(selected_slangs)}

【輪播文輸出格式】：
請精準輸出 PAGE 1 到 PAGE 5 的文字。每頁字數要精煉（少於 80 字），方便直接複製進 Canva。
語氣要「直接、專業、細膩、銳利、一針見血」，具備優雅的撕裂感。

- PAGE 1 (封面)：(必須是具有衝擊力、心理測驗或標籤流的廣東話標題)
- PAGE 2 (人格定義)：(展現本次指定的人格標籤與描述，文字要優雅而毒舌，讓人忍不住轉發)
- PAGE 3 (底層痛點拆解)：(融入核心痛點與玄學反轉角度，直擊為什麼他們會卡在白天安分、晚上失眠或煞錯位的死火現狀)
- PAGE 4 (破局允許)：(給予順應天賦密碼、在對的財富週期收斂或看清說明書的具體解法)
- PAGE 5 (高價值收藏 CTA)：(引導留字互動，例如：【立刻儲存】。留言區留下你的選項，我話你知點樣順勢增長)
"""

# ==================== 🚀 呼叫 AI 輸出 ====================
try:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a professional social media expert specialized in psychological and metaphysical content."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.85
    )
    print("🔥 幫你攪拌出來的全新【心理測驗標籤流】輪播文文案：\n")
    print(response.choices[0].message.content)

except Exception as e:
    print(f"❌ 執行出錯！錯誤訊息: {e}")
