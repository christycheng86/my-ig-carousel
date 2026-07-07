<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <title>爆款心理測驗輪播文攪拌器</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; padding: 30px; background-color: #f5f5f7; color: #1d1d1f; text-align: center; }
        .container { max-width: 650px; margin: 0 auto; background: white; padding: 40px; border-radius: 16px; box-shadow: 0 4px 30px rgba(0,0,0,0.05); }
        h2 { font-weight: 600; font-size: 24px; margin-bottom: 5px; }
        .sub { color: #86868b; margin-bottom: 25px; }
        button { background-color: #000; color: white; border: none; padding: 14px 30px; font-size: 16px; font-weight: 500; border-radius: 8px; cursor: pointer; transition: 0.2s; }
        button:hover { background-color: #333; }
        .result { margin-top: 30px; padding: 20px; background: #fafafa; border: 1px solid #e5e5e5; text-align: left; border-radius: 8px; }
        .prompt-box { margin-top: 15px; background: #f4f4f9; padding: 20px; border-radius: 8px; font-size: 14px; border-left: 4px solid #000; line-height: 1.6; }
    </style>
</head>
<body>

<div class="container">
    <h2>🔥 爆款心理測驗輪播文攪拌器</h2>
    <p class="sub">融合 FUFU AI LAB 標籤流風格 • 專為 Gemini 打造</p>
    <button onclick="shufflePrompt()">🎲 啟動隨機攪拌</button>

    <div id="displayZone" style="display:none;">
        <div class="result">
            <strong>📋 本次動態抽籤維度：</strong>
            <p id="dimensions" style="line-height: 1.5; margin-top: 10px;"></p>
        </div>
        <p style="margin-top:25px; font-weight:bold; color:#333;">👇 複製下方生成的全套指令發給 Gemini 執行：</p>
        <div class="prompt-box" id="finalPrompt" style="white-space: pre-line; text-align: left;"></div>
    </div>
</div>

<script>
// 1. 新增 FUFU AI LAB 風格的人格標籤選項資料庫
const personalityTags = [
    {title: "選項 A：貪婪的自噬者", desc: "你以過度反思為生，在自我內耗的泥潭中優雅地枯萎。那種對完美的病態執著，最終只會將你自傲的靈魂啃食殆盡，成為這世間最寂寞的虛無存在，荒謬且無止盡。"},
    {title: "選項 B：精緻的逃避者", desc: "你用『開拓新局』的虛假勤奮，去掩蓋你根本不敢下注的懦弱。手握微薄碎銀，在床榻上輾轉失眠，活成自己人生中最焦慮的旁觀者。"},
    {title: "選項 C：盲目的殉道者", desc: "你自帶心軟同直覺的天賦，卻在商業實踐中活成別人的專業擦屁股部隊。不斷流失底氣換取碎銀，最後連自己的本人生說明書都全數歸零。"},
    {title: "選項 D：安全感的囚徒", desc: "防禦心重到極致，每走一步都在算計沉沒代價。你以為死守籌碼、不交學費是理智，其實你只是在命運的藏鋒期裡進行優雅的慢性自殺。"}
];

const painPoints = [
    "表面上安分守己收工，返到屋企內耗到失眠，想動又不知落戶哪行。",
    "命中自帶極強直覺/心軟天賦，但在商業實踐中不斷幫人擦屁股、流失底氣。",
    "報咗好多變現課程，但防禦心太重，一到要擺籌碼就縮，極怕碎銀歸零。"
];

const angles = [
    "命運底層代碼的「藏鋒期/沉潛期」：行錯個人週期表，用力等於破財。",
    "天賦密碼的「雙重能量撕裂」：將星落錯位，高爆發特質被用來應付無謂嘅內耗。",
    "心理學的「損失厭惡」與玄學短板：拿着軍師的說明書去幹衝鋒陷陣的重資產硬路。"
];

const slangs = ["講句難聽啲", "骨格精奇", "倒錢落海", "心大心細", "死火", "執生", "踢爆"];

function shufflePrompt() {
    // 隨機抽籤
    const tag = personalityTags[Math.floor(Math.random() * personalityTags.length)];
    const pain = painPoints[Math.floor(Math.random() * painPoints.length)];
    const angle = angles[Math.floor(Math.random() * angles.length)];
    const shuffledSlangs = [...slangs].sort(() => 0.5 - Math.random()).slice(0, 3);

    document.getElementById("dimensions").innerHTML = `
        <b>人格標籤：</b>${tag.title}<br>
        <b>痛點維度：</b>${pain}<br>
        <b>玄學反轉：</b>${angle}<br>
        <b>廣東話庫：</b>${shuffledSlangs.join(', ')}
    `;
    
    const promptText = `你是一位精通 Instagram 和 Threads 演算法的自媒體百萬社群行銷專家、玄學與大眾心理學大師。請為我撰寫一組高品質、高轉發的【5頁 IG 輪播文文案】。風格請嚴格參考熱門的「黑天使系心理測驗」對號入座流。

【嚴格執行避坑規則】：
- 絕不直接出現「賺錢、副業、創業、金錢、收入、投資、虧損、發財、暴富、算命、八字、生命靈數」等字眼。
- 必須使用高級替代詞：開拓第二曲線、打造個人賽道、啟動新局、解鎖變現通道、商業實踐、增長、拿結果、碎銀、真金白銀、籌碼、成本、學費、沉沒代價、資源、底氣、財富週期、天賦密碼、命運底層代碼、個人週期表、能量配置、自帶的說明書。

【本次抽籤指定的隨機攪拌維度】：
- 核心人格標籤：${tag.title}
- 標籤精準描述：${tag.desc}
- 核心受眾痛點：${pain}
- 玄學/心理學反轉角度：${angle}
- 必須融入的地道廣東話詞彙：${shuffledSlangs.join(', ')}

【輪播文輸出格式】：
請精準輸出 PAGE 1 到 PAGE 5 的文字。每頁字數要極度精煉（少於 80 字），方便我直接複製進 Canva。語氣要直接、專業、細膩、銳利，具備優雅的撕裂感。語言使用地道香港廣東話。

- PAGE 1 (封面)：(必須是具有衝擊力、心理測驗或標籤流的廣東話大標題)
- PAGE 2 (人格定義)：(展現本次指定的人格標籤與描述，文字要優雅而毒舌，讓人忍不住轉發 Story)
- PAGE 3 (底層痛點拆解)：(融入核心痛點與玄學反轉角度，直擊為什麼他們會卡在白天安分、晚上失眠或煞錯位的死火現狀)
- PAGE 4 (破局允許)：(給予順應天賦密碼、在對的財富週期收斂或看清說明書的具體解法)
- PAGE 5 (高價值收藏 CTA)：(引導留字互動，例如：【立刻儲存】。留言區留下你的選項，我話你知點樣順勢增長)`;

    document.getElementById("finalPrompt").innerText = promptText;
    document.getElementById("displayZone").style.display = "block";
}
</script>

</body>
</html>
