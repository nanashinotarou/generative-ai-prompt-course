# 🎓 3月 生成AIとプロンプトコース サイト仕様書（Geminiレポート）

> **最終更新**: 2026-03-06
> **対象**: Day 1 〜 Day 3（実装済み）
> **状態**: 大規模オーバーホール中

---

## 📌 プロジェクト概要

| 項目 | 内容 |
|------|------|
| **プロジェクト名** | 3月 生成AIとプロンプト研修 |
| **フォルダ** | `g:\マイドライブ\研修\【202603】生成AIとプロンプト` |
| **GitHub** | `nanashinotarou/generative-ai-prompt-course` |
| **URL** | [generative-ai-prompt-course.pages.dev](https://generative-ai-prompt-course.pages.dev/) |
| **技術スタック** | HTML / CSS / Vanilla JS |
| **外部CDN** | Font Awesome 6.4, Google Fonts (Noto Sans JP, Teko, Fira Code, Share Tech Mono) |

---

## 📁 ファイル構成

```
【202603】生成AIとプロンプト/
├── index.html                    # ポータル（カレンダー＋講座一覧）
├── index_dev_notes.html          # 開発者向けレシピ集（設計・デザイン意図）
├── main.js                       # 共通JS（クイズエンジン、最新ボタン自動化）
├── _routes.json                  # Cloudflare Pages ルーティング設定
├── GEMINI_REPORT.md              # ←このファイル（プロジェクト仕様書）
│
├── vol01-1_ai_start.html         # Day 1: AIの夜明け（導入）
├── vol02-1_canva_basics.html     # Day 2: Canva基礎
└── vol01-3_prompt.html           # Day 3: プロンプトエンジニアリング（Magical Experience v2.0）
```

---

## 🎨 テーマ・配色マップ

| Day | ファイル名 | テーマ色 | コンセプト |
|-----|-----------|----------|-----------|
| 1 | `vol01-1_ai_start.html` | Azure / Blue | 清潔感のある導入、信頼感 |
| 2 | `vol02-1_canva_basics.html` | Purple / Pink | クリエイティビティ、Canvaブランドカラー |
| 3 | `vol01-3_prompt.html` | **Night Indigo** | 魔法、奥深さ、Dark Mode基調 |

---

## 🕹️ インタラクティブ機能（Day 3 特集）

- **Bento Card**: 情報をマトリックス状に整理するモダンなレイアウト
- **Timeline UI**: 学習ステップや歴史を視覚的に表現
- **Ticket Style Summary**: 動画の内容をチケット風に要約
- **Scenario Sandbox**: ビジネスユースケースを試行錯誤するエリア
- **Magical Cauldron**: プロンプトを調合するメタファー（Sparkles演出付き）
- **Audio Feedback**: 魔法発動時やクリック時のSE（WebAudio/SoundCloud等）

---

## 📐 共通レイアウトパターン

```html
<body>
  <div class="calendar-nav">...</div> <!-- 上部のカレンダー -->
  <div class="container">
    <header class="hero">
      <span class="tag-pill">Day N</span>
      <h1>TITLE</h1>
      <p class="hero-sub">サブタイトル</p>
    </header>
    <div class="content">
      <!-- 講義ノート -->
      <!-- 動画セクション -->
      <!-- インタラクティブ要素 -->
      <!-- クイズエリア -->
    </div>
  </div>
  <footer class="page-footer">...</footer>
</body>
```

---

## 📝 今後の改善予定

- [ ] `styles.css` への共通スタイル切り出し（ Phase 5 ）
- [ ] クイズの難易度別（初級/中級/上級）実装（ Phase 4 ）
- [ ] `index_dev_notes.html` の Day 別フィルタリング実装（ Phase 3 ）
