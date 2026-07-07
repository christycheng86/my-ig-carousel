<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <title>爆款文案隨機攪拌生成器</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 30px; background-color: #f4f4f9; color: #333; text-align: center; }
        .container { max-width: 600px; margin: 0 auto; background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        button { background-color: #007bff; color: white; border: none; padding: 12px 25px; font-size: 18px; border-radius: 8px; cursor: pointer; transition: 0.3s; }
        button:hover { background-color: #0056b3; }
        .result { margin-top: 25px; padding: 20px; background: #eef2f7; border-left: 5px solid #007bff; text-align: left; border-radius: 6px; }
        .prompt-box { margin-top: 15px; background: #fff3cd; padding: 15px; border-radius: 6px; font-size: 14px; border-left: 5px solid #ffc107; }
    </style>
</head>
<body>

<div class="container">
    <h2>🔥 爆款文案隨機攪拌器 (免API版)</h2>
    <p>點擊下方按鈕，自動動態重組代碼，生成發給 Gemini 的最強指令！</p>
    <button onclick="shufflePrompt()">🎲 啟動隨機攪拌</button>

    <div id="displayZone" style="display:none;">
        <div class="result">
            <strong>📋 今日抽籤維度：</strong>
            <p id="dimensions"></p>
        </div>
        <p style="margin-top:20px; font-weight:bold; color:#555;">👇 複製下方生成的全套指令發給 AI：</p>
        <div class="prompt-box" id="finalPrompt" style="white-space: pre-line; text-align: left;"></div>
    </div>
</div>

<script>
const painPoints = [
    "報咗好多變現課程，但防禦心太重，一到要擺籌碼就縮。",
    "表面上安分守己收工，返到屋企內耗到失眠，想動又不知落戶哪行。",
    "以前做實體或者盲目跟風，交足真金白銀當學費，依家驚到唔敢行錯一步。",
    "命中自帶極強直覺/心軟天賦，但在商業實踐中不斷幫人擦屁股、流失底氣。",
    "30-40歲精緻迷茫，手頭有少少碎銀，想開拓第二曲線但極怕歸零。"
];

const angles = [
    "命運底層代碼的「藏鋒期/沉潛期」：行錯個人週期表，用力等於破財。",
    "天賦密碼的「雙重能量撕裂」：將星落錯位，高爆發特質被用來應付辦公室政治。",
    "能量學的「排毒與格局重塑」：前半生熬過的劫，是幫你斷開垃圾磁場的開光過程。",
    "心理學的「損失厭惡」與玄學短板：拿着軍師的說明書去幹衝鋒陷陣的重資產硬路。"
];

const slangs = ["講句難聽啲", "骨格精奇", "倒錢落海", "心大心細", "死火", "執生", "踢爆"];

function shufflePrompt() {
    const pain = painPoints[Math.floor(Math.random() * painPoints.length)];
    const angle = angles[Math.floor(Math.random() * angles.length)];
    
    // 隨機抽 3 個廣東話
    const shuffledSlangs = [...slangs].sort(() => 0.5 - Math.random()).slice(0, 3);

    document.getElementById("dimensions").innerHTML = `<b>痛點：</b>${pain}<br><b>角度：</b>${angle}<br><b>詞彙：</b>${shuffledSlangs.join(', ')}`;
    
    const promptText = `你是一位精通 Instagram 和 Threads 演算法的自媒體百萬社群行銷專家、玄學與大眾心理學大師。請為我撰寫 1 篇高轉發、高儲存的爆款 Threads 貼文。

【嚴格執行避坑規則】：
- 絕不直接出現「賺錢、副業、創業、金錢、收入、投資、虧損、發財、暴富、算命、八字、生命靈數」等字眼。
- 必須使用高級替代詞：開拓第二曲線、打造個人賽道、啟動新局、解鎖變現通道、商業實踐、增長、拿結果、碎銀、真金白銀、籌碼、成本、學費、沉沒代價、資源、底氣、財富週期、天賦密碼、命運底層代碼、個人週期表、能量配置、自帶的說明書。

【本次隨機攪拌維度】：
- 核心痛點：${pain}
- 玄學/心理學反轉角度：${angle}
- 必須融入的地道廣東話詞彙：${shuffledSlangs.join(', ')}

【文案輸出規則】：
- 語氣：直接、專業、細膩、銳利、一針見血。以「看透命運底層邏輯的同行分享者」姿態。
- 語言：地道香港廣東話。
- 結構：短小精悍、撕裂認知。150-200字內，結尾留一個引發在留言區大亂鬥的問句。`;

    document.getElementById("finalPrompt").innerText = promptText;
    document.getElementById("displayZone").style.display = "block";
}
</script>

</body>
</html>
