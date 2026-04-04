# Hotel Price Sync CMS

### 旅宿價格同步展示系統（WordPress × Python × REST API）

這是一個以 **WordPress** 為核心的全端整合專案，目標是建立一套可擴充的 **旅宿價格管理與自動同步系統**。  
系統透過 **自定義內容類型（CPT）** 與 **ACF 欄位** 管理飯店資料，並規劃串接 **Python 爬蟲** 與 **WordPress REST API**，實現房價資料的自動抓取、清洗與同步更新。

此專案定位為一個可展示的 **接案作品集 Demo**，用來呈現從資料建模、CMS 管理、前端展示，到 API 自動化整合的完整開發流程。

---

## ✨ 專案目標

- 建立可管理飯店資料的 WordPress 後台系統
- 顯示 Agoda / Booking 等平台價格資訊
- 透過 Python 自動更新 WordPress 內的價格欄位
- 作為可延伸的旅遊比價 / CMS 整合型作品集

---

## 🚀 核心功能

### 已完成

- 使用 **CPT UI** 建立自定義內容類型：`飯店 (hotels)`
- 使用 **ACF** 建立價格欄位：
  - `agoda_price`
  - `booking_price`
- 完成飯店資料的後台輸入與管理
- 成功在前台頁面顯示 ACF 價格欄位內容
- 完成本機開發環境建置（XAMPP + WordPress + MySQL）
- 建立 Git / GitHub 版本控制流程

### 開發中

- 建立更完整的單頁飯店展示模板
- 串接 WordPress REST API
- 透過 Python 腳本自動更新飯店價格
- 建立資料清洗流程（如 `TWD 4,500 → 4500`）
- 完成爬蟲抓取 → 清洗 → API 傳輸 → 前台更新 的全鏈路測試

### 規劃中

- 增加更多飯店資料欄位（來源平台、更新時間、房型條件等）
- 建立價格歷史紀錄
- 加入定時排程更新
- 擴充至更多旅遊平台資料來源

---

## 🛠️ 技術棧

### Backend

- WordPress
- PHP 8.x
- MySQL
- ACF (Advanced Custom Fields)
- CPT UI

### Frontend

- WordPress Theme / Template
- HTML / CSS

### Automation & Integration

- Python 3.10+
- Requests
- BeautifulSoup
- WordPress REST API

### Development Tools

- XAMPP
- Git
- GitHub

---

## 🧱 系統架構概念

```text
Python Scraper
    ↓
Data Cleaning
    ↓
WordPress REST API
    ↓
WordPress (CPT + ACF)
    ↓
Hotel Frontend Page
```
