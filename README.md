<!-- markdownlint-disable MD033 -->
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&pause=1000&color=00FFCC&center=true&vCenter=true&width=500&lines=InverseCC+Bot;Buy+when+Reddit+hates+it" alt="Typing SVG" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Binance-Testnet-yellow?logo=binance" alt="Binance Testnet">
  <img src="https://img.shields.io/badge/Reddit-API-FF4500?logo=reddit" alt="Reddit API">
  <img src="https://img.shields.io/badge/Sentiment-VADER-brightgreen" alt="VADER">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="MIT License">
  <img src="https://img.shields.io/badge/status-active-success" alt="Status">
</p>

# 🔄 InverseCC Bot

## 🤖 The Contrarian Trading Bot  
**"Buy when there's blood in the streets – even if the blood is on Reddit."**

InverseCC monitors **r/CryptoCurrency** and **r/wallstreetbets** in real time, detects **strongly negative sentiment** using VADER, and instantly places a **market buy order** on Binance (testnet by default). It automates the classic Buffett maxim: *"Be fearful when others are greedy, and greedy when others are fearful."*

---

## 📖 Table of Contents
- [🧠 How It Works](#-how-it-works)
- [📊 Example Run](#-example-run)
- [⚙️ Setup (5 minutes)](#️-setup-5-minutes)
- [🔧 Configuration](#-configuration)
- [📁 Project Structure](#-project-structure)
- [🚀 Roadmap](#-roadmap)
- [⚠️ Disclaimer](#-disclaimer)

---

## 🧠 How It Works

```mermaid
flowchart TD
    A[Start Bot] --> B[Fetch hot posts/comments from r/CryptoCurrency and r/wallstreetbets]
    B --> C{Contains BTC, ETH, SOL, or DOGE?}
    C -->|No| B
    C -->|Yes| D[Run VADER sentiment analysis]
    D --> E{Sentiment score < -0.5?}
    E -->|No| B
    E -->|Yes| F[Place market buy order on Binance Testnet]
    F --> G[Log trade & avoid duplicate buys]
    G --> B
