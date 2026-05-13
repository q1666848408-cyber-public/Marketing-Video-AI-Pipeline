<div align="center">

# 🎥 Marketing Video AI Pipeline

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Gemini](https://img.shields.io/badge/Gemini-2.5%20Pro-4285F4?style=flat-square&logo=google&logoColor=white)](https://deepmind.google/gemini)
[![Seedance](https://img.shields.io/badge/Seedance-2.0-FF6B35?style=flat-square)](https://www.volcengine.com)
[![Lark](https://img.shields.io/badge/Lark-Bitable-00D6B9?style=flat-square&logo=bytedance&logoColor=white)](https://open.feishu.cn)

**Dual-track AI short-video pipeline — marketing (e-commerce) and traffic (dance / kids) — Feishu Bitable × Gemini × Seedance 2.0**

> ⚠️ **Showcase Only** — ~15% skeleton. Production prompts, Feishu credentials & rendering glue not included.

</div>

---

## ✨ Overview

A unified backend driving two distinct short-video production tracks:

- **Marketing videos** — product-led, conversion-focused. 12-grid storyboard + reference images.
- **Traffic videos** — dance & kids modes, fan-acquisition. 4-grid character + scene refs.

Both tracks are triggered by Feishu Bitable automations, run on a Singapore Flask server, and write final prompt artifacts back to Feishu for manual rendering in Seedance 2.0.

---

## 🏗️ Architecture

```
   Feishu Bitable                  Flask Server (SG)
  ┌────────────────┐              ┌──────────────────────┐
  │  Marketing     │── HTTP ─────►│  /api/marketing      │
  │  Bitable       │              │  └ MarketingPipeline │
  └────────────────┘              ├──────────────────────┤
  ┌────────────────┐              │  /api/traffic        │
  │  Traffic       │── HTTP ─────►│  └ TrafficPipeline   │
  │  Bitable       │              │     · dance mode     │
  └────────────────┘              │     · kids mode      │
                                  └──────────┬───────────┘
                                             │
                              ┌──────────────┴──────────────┐
                              ▼                             ▼
                      ┌───────────────┐           ┌──────────────────┐
                      │  Gemini 2.5   │           │  Seedance prompt │
                      │  multi-modal  │           │  generator       │
                      └───────┬───────┘           └────────┬─────────┘
                              │                             │
                              └──────────────┬──────────────┘
                                             ▼
                              Reference images + Seedance prompts
                                             │
                                             ▼
                                  Write back to Feishu
```

---

## 📁 Structure

```
marketing-video-ai-pipeline/
├── server.py                # Flask entry
├── pipelines/
│   ├── marketing.py         # Marketing track
│   └── traffic.py           # Traffic (dance / kids) track
├── platforms/
│   ├── gemini.py            # Gemini API client
│   └── seedance.py          # Seedance prompt builder
└── requirements.txt
```

---

## 🔧 Tech Stack

| Layer | Technology |
|---|---|
| Web Server | Flask + Gunicorn |
| Hosting | Singapore VPS |
| Trigger | Feishu Bitable automation |
| LLM (multi-modal) | Gemini 2.5 Pro |
| Video model | Seedance 2.0 (manual render) |
| Storage | Feishu Drive / Bitable |

---

<div align="center">
<sub>Showcase version · Production prompts not included · For portfolio reference only</sub>
</div>
