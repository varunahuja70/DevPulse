<div align="center">

# ⚡ DevPulse

### The Minimal, Apple-Inspired AI Quota Notch & Companion for Windows 💻✨

[![Version](https://img.shields.io/badge/version-1.22.0-26D67C?style=for-the-badge)](https://github.com/varunahuja70/DevPulse/releases)
[![Platform](https://img.shields.io/badge/platform-Windows%2010%20%7C%2011-0078D6?style=for-the-badge&logo=windows)](https://github.com/varunahuja70/DevPulse)
[![License](https://img.shields.io/badge/license-MIT-lightgrey?style=for-the-badge)](LICENSE)

<p align="center">
  <b>Monitor your AI allowances in real-time right from your screen edge.</b><br>
  Designed with Apple/macOS ergonomics, physics-based micro-interactions, and instant tray access.
</p>

---

<!-- 🎥 DEMO VIDEO / SCREENSHOT PLACEHOLDER -->
<p align="center">
  <br>
  <!-- VIDEO / GIF DEMO HERE -->
  <a href="#demo">
    <img src="https://via.placeholder.com/800x450/121316/26D67C?text=%E2%96%B6%EF%B8%8F+Add+Your+Demo+Video+/+GIF+Here+(800x450)" alt="DevPulse Demo Video Placeholder" width="80%">
  </a>
  <br>
  <sub><i>🎬 Replace the link above with your demo video or preview GIF</i></sub>
  <br><br>
</p>

---

</div>

## 🌟 Why DevPulse?

When coding with multiple AI tools, you often wonder:
- ⏳ **How much AI quota do I have left?**
- 🤖 **Is Claude or Codex still thinking, or did it finish?**

**DevPulse** rests gracefully on your screen edge and gives you exact answers in a single glance — with zero distraction.

---

## ✨ Features at a Glance

| Feature | Description |
|---|---|
| 🍏 **macOS-Grade UI** | Ultra-clean dark aesthetics inspired by Apple Sonoma & Linear. |
| ⚡ **Live AI Notches** | Tracks real-time quotas for **Claude, Codex, Antigravity, Cursor, Grok, Copilot & OpenCode**. |
| 🎛️ **Fluid Physics** | Spring-animated toggles, smooth card transitions & zero layout jitter. |
| 🔒 **100% Private & Safe** | Read-only local session tokens. No passwords stored, zero tracking. |
| ⚙️ **Minimal Footprint** | Built in **Rust + Tauri 2** for ultra-light memory usage (<30MB RAM). |

---

## 🚀 Quick Download & Install

Just want to use the app? Grab the latest pre-built Windows installer:

👉 **[Download Latest DevPulse Setup (.exe)](https://github.com/varunahuja70/DevPulse/releases/latest)**

1. Download **`DevPulse_1.22.0_x64-setup.exe`**.
2. Run the installer and launch **DevPulse**.
3. It will automatically detect your local AI sessions! 🎉

---

## 🛠️ Build & Run from Source

If you want to contribute or build it locally:

### 1️⃣ Prerequisites
- 🦀 [Rust & Cargo](https://rustup.rs/) (with MSVC C++ Build Tools)
- 🟢 [Node.js](https://nodejs.org/) (v18+)
- 🪟 Windows 10/11 (with WebView2 Runtime)

### 2️⃣ Clone the Repo
```powershell
git clone https://github.com/varunahuja70/DevPulse.git
cd DevPulse
```

### 3️⃣ Build the Hook Library
```powershell
cargo build --release -p codenotch-hook --target-dir target/hook
```

### 4️⃣ Run in Development Mode
```powershell
cd codenotch
npx @tauri-apps/cli dev
```

### 5️⃣ Build Release Installer (.exe)
```powershell
cd codenotch
npx @tauri-apps/cli build
```
The fresh installer will be created at:
📂 `target/release/bundle/nsis/DevPulse_1.22.0_x64-setup.exe`

---

## 🎨 Supported Providers

- 🟣 **Claude** (Claude Code token & active thinking pulse)
- 🟢 **Codex** (OpenAI rate limits & 5h/weekly quota)
- 🌐 **Antigravity** (`agy` CLI & quota breakdown)
- ⚡ **Cursor** (Editor API usage & allowance)
- 🚀 **Grok** (Weekly build allowance)
- 🐙 **GitHub Copilot** (Premium requests & chat balance)
- 🦙 **OpenCode / Go** (Rolling 5h/weekly allowance)

---

## 👤 Author

Developed & Maintained by **Varun Ahuja**
- 🐙 GitHub: [@varunahuja70](https://github.com/varunahuja70)

---

<div align="center">
  Made with ❤️ for developers who love clean, minimal tools.
</div>
