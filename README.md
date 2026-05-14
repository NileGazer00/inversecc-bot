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
</p>

# 🔄 InverseCC Bot

**Contrarian trading bot that buys crypto when Reddit sentiment is strongly negative.**

> *"Be fearful when others are greedy, and greedy when others are fearful."* – Warren Buffett  
> This bot automates the second part.

---

## 📖 Table of Contents

- [What does it do?](#what-does-it-do)
- [How it works (flowchart)](#how-it-works-flowchart)
- [Installation](#installation)
- [Getting API keys](#getting-api-keys)
  - [Reddit API](#reddit-api)
  - [Binance Testnet API](#binance-testnet-api)
- [Configuration](#configuration)
- [Running the bot](#running-the-bot)
- [Example output](#example-output)
- [Troubleshooting](#troubleshooting)
- [Project structure](#project-structure)
- [Disclaimer](#disclaimer)

---

## What does it do?

The bot continuously monitors **r/CryptoCurrency** and **r/wallstreetbets** for posts/comments that mention `BTC`, `ETH`, `SOL`, or `DOGE`. It analyzes the sentiment of each text using **VADER**. If the sentiment score is **below -0.5** (strongly negative), it immediately places a **market buy order** on Binance (testnet by default) for a fixed amount (e.g., $10).

**Why?** When retail crowds panic, prices often overshoot – buying into extreme fear can be profitable.

---

## How it works (flowchart)

```mermaid
flowchart TD
    A[Start Bot] --> B[Fetch hot posts/comments from Reddit]
    B --> C{Contains BTC, ETH, SOL, or DOGE?}
    C -->|No| B
    C -->|Yes| D[Run VADER sentiment analysis]
    D --> E{Sentiment score < -0.5?}
    E -->|No| B
    E -->|Yes| F[Place market buy order on Binance Testnet]
    F --> G[Log trade & avoid duplicate buys for this session]
    G --> B
