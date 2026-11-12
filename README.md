# 宿舍學伴｜新生入住指南

第一次住宿時，要找電器、訪客或保證金規定，常常得翻好幾頁文件。所以我想把它整理成像學長姐陪你看規定的小網站：直接找問題、看重點，需要時也能對照來源。

本專案延續宿舍RAG作業，新增可直接瀏覽的指南網站，並用AGENTS.md記錄文字、版型、內容與開發規則，讓AI能依同一方式繼續新增主題。

## 已有功能
- 六篇具條文依據的指南、分類與關鍵字搜尋。
- 可分享的hash指南網址（例如 #guide/electricity）。
- 入住準備建議清單，本機儲存勾選進度。
- RAG01與RAG02下載與Colab入口。
- 手機版、鍵盤操作、無資料提示、來源版本標示。

這是純HTML/CSS/JavaScript專案，不呼叫LLM。聊天功能請另外在Colab執行Notebook，需自行設定Groq密鑰。既有Notebook尚未於本次網站工作中重新驗證模型下載與API執行。

## 本機預覽
可直接開啟index.html，或在專案資料夾執行：

```sh
python3 -m http.server 8000
```

瀏覽 http://localhost:8000 。本機Colab按鈕只開Colab首頁，可下載Notebook後使用Colab的「檔案→上傳筆記本」。發布至PeiTsenYeh的GitHub Pages後，按鈕會自動連到同一儲存庫main分支的notebooks/檔案。若改owner或branch，調整assets/app.js最下方。

## 上傳GitHub與開啟Pages
1. 用PeiTsenYeh登入GitHub，建立Public儲存庫，例如dormitory-guide，分支使用main。
2. 解壓縮專案ZIP，把index.html、AGENTS.md、README.md、.nojekyll以及assets/、content/、notebooks/、scripts/放到儲存庫根目錄，不要多包一層dormitory-guide資料夾。可用Git，或GitHub「Add file → Upload files」拖曳檔案與資料夾上傳。
3. Commit後，進入Settings → Pages，Source選Deploy from a branch；Branch選main、資料夾選/(root)，按Save。
4. 等Pages顯示部署成功網址。若儲存庫叫dormitory-guide，預期為https://peitsenyeh.github.io/dormitory-guide/；實際以Pages設定頁顯示為準。
5. 開網站確認指南、清單及兩個Colab按鈕；直接開 #guide/deposit 應可顯示保證金指南。

本套件沒有已生成的rag-data.zip或原始PDF。RAG01需上傳先前的4頁194934706.pdf。執行後取得rag-data.zip，另上傳至公開下載位置，在RAG02設定KB_ZIP_URL並更新GitHub Notebook，助教才能從網址載入。不要上傳金鑰。

## 讓AI新增內容
先讓AI讀AGENTS.md，再給明確主題與來源。範例：

> 請先閱讀AGENTS.md。依照我提供的新文件新增「報修指南」，使用既有共用版型、標示文件版本與條文頁碼。文件沒寫的電話與辦理時間不要猜。更新完成後執行驗證，說明來源與修改範圍。

複製content/TEMPLATE.json格式，新增物件到content/guides.js。分類、搜尋、卡片及內文會自動更新，不必另外複製HTML。範本不是實際指南，不會顯示在網站。

## 驗證

```sh
python3 scripts/validate.py
node --check assets/app.js
```

第二行需要已安裝Node。第一行只需Python標準庫。另手動確認：搜尋與清空搜尋、分類切換、無結果、指南開啟與返回、未知slug提示、清單重整與重設、手機窄版、Tab鍵操作、Colab檔案路徑。

## 來源與範圍
先前由使用者提供194934706.pdf的文字內容：管理辦法105年6月30日、保證金要點105年5月31日。網站呈現依據這份歷史版本的摘要，不宣稱是現行規定或校方服務。來源PDF目前未包含於專案，頁碼為先前文件的PDF頁次。

後續優先補充同校最新版本、收退費須知、入住公告與報修資訊。其他學校資料需獨立標示學校與適用範圍，不能混入北科大規定。
