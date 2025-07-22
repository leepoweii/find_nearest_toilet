# 附近公廁尋找器 🚽

> 使用政府開放資料的智慧公廁導航系統 - AI Vibe Coding 實驗專案

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.1+-green.svg)
![uv](https://img.shields.io/badge/uv-package_manager-orange.svg)

## 📖 專案背景

一直以來，我都只把 Python 這門程式語言用在一些「幕後作業」，例如做數據分析、統計運算，或是開發個人用的小工具。這些成果雖然帶來成就感，卻往往只呈現在指令列或圖表中，讓朋友看了也不知道該怎麼操作。

這在瀏覽政府的開放資料時，發現了一份「全國公廁建檔」的清單，裡頭詳細列出了全台灣各地的公廁資訊。對於平常待在金門的我來說，在台北要找廁所並不是那麼方便，於是腦中閃過一個念頭：「如果能一鍵帶我去廁所，應該很實用吧？」

正好最近很紅各種 Vibe Coding，於是我決定和「GPT 好夥伴」一起來場小實驗，經過幾回合的切磋，很快就製作出了這個「附近公廁尋找器」的網站雛形。

## ✨ 主要功能

- 🎯 **即時定位**: 自動取得使用者位置
- 📍 **附近搜尋**: 基於 Haversine 公式計算最近的公廁距離
- 🗺️ **一鍵導航**: 直接開啟手機預設地圖應用程式導航
- 📱 **響應式設計**: 使用 Tailwind CSS 和 DaisyUI 打造美觀介面
- ⚡ **高效能計算**: 使用 NumPy 向量化計算提升查詢速度
- 🏛️ **政府開放資料**: 基於官方「全國公廁建檔」資料庫

## 🛠️ 技術架構

### 後端 (Flask)
- **Flask**: 輕量級 Web 框架
- **Pandas**: 資料處理與分析
- **NumPy**: 高效能數值計算
- **Haversine 算法**: 地球表面兩點間距離計算

### 前端
- **HTML5**: 支援地理定位 API
- **Tailwind CSS**: 快速響應式設計
- **DaisyUI**: 美觀的 UI 組件庫
- **Vanilla JavaScript**: 原生 JS 處理互動

### 資料來源
- 政府開放資料：全國公廁建檔清單
- 格式：CSV/JSON 包含座標、名稱等資訊

## 🚀 快速開始

### 環境需求
- Python 3.11 或以上版本
- [uv](https://docs.astral.sh/uv/) package manager

### 安裝步驟

1. **複製專案**
```bash
git clone https://github.com/leepoweii/find_nearest_toilet
cd find_nearest_toilet
```

2. **安裝依賴**
```bash
uv sync
```

3. **啟動應用程式**
```bash
uv run flask run
```

4. **開啟瀏覽器**
```
http://localhost:5000
```

### 開發模式

開啟 Flask 除錯模式：
```bash
uv run flask --debug run
```

## 📁 專案結構

```
find_nearest_toilet/
├── app.py                 # Flask 主應用程式
├── pyproject.toml          # uv 專案配置
├── requirements.txt        # 傳統依賴列表（保留相容性）
├── data/                   # 公廁資料
│   ├── all_toilets.csv     # 公廁清單 CSV 格式
│   └── all_toilets.json    # 公廁清單 JSON 格式
├── templates/              # HTML 模板
│   └── index.html          # 主頁面
├── static/                 # 靜態檔案
│   ├── css/               # 樣式表
│   ├── icons/             # 應用程式圖示
│   ├── manifest.json      # PWA 配置
│   └── service-worker.js  # Service Worker
├── tailwind.config.js     # Tailwind CSS 配置
├── package.json           # Node.js 依賴（前端工具）
└── zbpack.json           # Zeabur 部署配置
```

## 🔧 使用方法

1. **允許位置存取**: 首次使用時瀏覽器會請求地理位置權限
2. **自動搜尋**: 系統會自動找到最近的公廁
3. **查看結果**: 顯示公廁名稱、距離等資訊
4. **開始導航**: 點擊「導航」按鈕開啟地圖導航

## 🌟 技術亮點

### 高效能距離計算
```python
def haversine_vectorized(lat1, lon1, lat2, lon2):
    """
    使用 NumPy 向量化的 Haversine 計算
    大幅提升大量座標點的查詢效能
    """
    R = 6371  # 地球半徑 (km)
    # ... 向量化計算邏輯
    return R * c
```

### 響應式設計
- 桌面版：清晰的卡片佈局
- 平板：適中的間距設計
- 手機：單欄優化顯示

## 🙏 致謝

- 政府開放資料平台提供公廁資料
- AI 協助程式開發與除錯
- Flask 與相關開源套件的開發者們

## 📞 聯絡資訊

如有任何問題或建議，歡迎透過 GitHub Issues 聯絡。

---

*這個專案展現了 AI Vibe Coding 的可能性 - 從想法到實作，讓技術真正服務生活需求。* 🚀