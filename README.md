# 宿舍學伴｜新生入住指南 🏡

第一次住宿舍，難免會有很多問題：哪些電器可以帶？朋友能不能來？保證金要怎麼退？

雖然宿舍辦法裡都有規定，但要自己翻文件找答案還是有點麻煩。所以我想做一個像學長姐陪你看規定的小網站，把住宿資訊整理成容易查找、看得懂的生活指南。

## 直接查看作品

🌐 **[點我開啟「宿舍學伴」公開網站](https://peitsenyeh.github.io/dormitory-rag/)**

📋 **[查看 AI 開發規則 AGENTS.md](./AGENTS.md)**

網站已透過 GitHub Pages 公開。直接點上方連結就能瀏覽，不需要下載專案、安裝套件或啟動本機伺服器。

## 這次作業在做什麼？

這個專案延續之前的「宿舍生活小幫手」RAG 作業，進一步做成可以直接閱讀的宿舍指南網站。

這次除了完成網頁，也把文字風格、檔案結構、內容格式與來源規則寫進 `AGENTS.md`。之後請 AI 新增主題時，就能依照同一套方式繼續製作，不必每次重新設計。

## 網站可以做什麼？

- **閱讀六篇指南**：住宿申請、電器使用、訪客、生活規範、保證金及退宿。
- **分類與搜尋**：輸入關鍵字，找到相關指南。
- **查看條文依據**：指南附上條文、PDF 頁碼與文件版本。
- **使用入住清單**：勾選準備進度，儲存在自己的瀏覽器。
- **開啟 RAG 程式**：連到 Google Colab，執行原本的宿舍問答工具。

整體使用奶油白與淺綠色，文字採「親切學長姐」的風格：先說重點，再補充條件與依據；遇到文件沒寫的事情，就坦白說明。

## 建議查看順序

1. 開啟[公開網站](https://peitsenyeh.github.io/dormitory-rag/)。
2. 搜尋「電器」，點開指南，查看條文依據。
3. 試著切換分類、勾選入住準備清單。
4. 閱讀 [`AGENTS.md`](./AGENTS.md)，了解專案如何持續擴充。

以上網站功能都可以直接使用，不需要執行 Colab。

## AGENTS.md：讓 AI 知道怎麼繼續做

[`AGENTS.md`](./AGENTS.md) 記錄了：

- 專案目的與適用範圍。
- 網頁視覺與文字風格。
- 檔案結構及命名方式。
- 新增指南的固定格式。
- 條文、頁碼與文件版本的標示規則。
- 修改完成後的檢查方式。

例如，之後提供新的宿舍文件，就可以請 AI：

> 請先閱讀 AGENTS.md，依照既有格式新增「宿舍報修指南」，保留來源與版本資訊。文件沒有提供的電話或辦理時間，請不要自行補充。

## 如何延續這個專案？

指南內容集中在 [`content/guides.js`](./content/guides.js)，新增時參考 [`content/TEMPLATE.json`](./content/TEMPLATE.json)。

每篇指南包含：

- 唯一的英文識別名稱（slug）。
- 分類、標題與簡介。
- 來源文件版本與內容整理日期。
- 各段說明及條文依據。

新增內容後，網站會使用共用版型顯示，分類與搜尋也會讀取同一份資料，不需要重新製作整個頁面。

## 主要檔案

```text
index.html                 網站首頁
AGENTS.md                  AI 開發與內容規則
README.md                  專案介紹
assets/
  style.css                共用樣式
  app.js                   搜尋、分類、指南與清單功能
content/
  guides.js                指南內容
  TEMPLATE.json            新增指南的格式範本
notebooks/
  RAG01_宿舍小幫手.ipynb
  RAG02_宿舍小幫手.ipynb
scripts/
  validate.py              內容與檔案檢查程式
```

## 延伸作品：RAG 宿舍問答工具

除了可以直接閱讀的指南網站，本專案也保留之前的 RAG 作業。

### RAG01｜建立知識庫

將指定宿舍 PDF 依條文整理，保留來源、頁碼與版本，使用 EmbeddingGemma 2 和 FAISS 建立向量知識庫，匯出 `rag-data.zip`。

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PeiTsenYeh/dormitory-rag/blob/main/notebooks/RAG01_%E5%AE%BF%E8%88%8D%E5%B0%8F%E5%B9%AB%E6%89%8B.ipynb)

### RAG02｜宿舍生活小幫手

載入知識庫，搭配 Groq 大語言模型，根據檢索結果回答，並用 Gradio 顯示互動介面與來源。

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PeiTsenYeh/dormitory-rag/blob/main/notebooks/RAG02_%E5%AE%BF%E8%88%8D%E5%B0%8F%E5%B9%AB%E6%89%8B.ipynb)

RAG 聊天功能需要另外執行 Colab，並在 Colab 密鑰設定自己的 `Groq` API Key。公開指南網站不需要 API Key，也不需要先執行 RAG 程式。

## 使用技術

| 部分 | 技術 |
|---|---|
| 網頁 | HTML、CSS、JavaScript |
| 內容管理 | 獨立內容檔與共用版型 |
| 清單進度 | 瀏覽器 localStorage |
| 網站發布 | GitHub Pages |
| RAG 問答 | EmbeddingGemma 2、FAISS、Groq、Gradio |
| AI 協作規則 | AGENTS.md |

## 資料來源與版本

內容依先前提供的 `194934706.pdf` 整理，包含：

- 《國立臺北科技大學學生宿舍管理辦法》：民國 105 年 6 月 30 日修正版本。
- 《國立臺北科技大學學生宿舍住宿保證金實施要點》：民國 105 年 5 月 31 日通過版本。

每篇指南標示相關條文、PDF 頁碼與版本。原始 PDF 目前未包含在專案中。

入住清單屬於準備建議，不是學校正式要求。本網站為課堂專案，並非學校官方服務，也未確認上述文件為現行版本。實際住宿資格、費用與辦理方式，仍以學校最新公告為準。

## 後續想增加的內容

- 補充同校最新宿舍規定與入住公告。
- 加入有來源依據的報修及收退費指南。
- 依照 AGENTS.md 持續擴充內容，維持一致的風格與來源標示。
