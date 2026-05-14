# Marketing-Video-AI-Pipeline

![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)

> **Showcase** — ~15% skeleton. Core implementation not included.

Feishu Bitable-triggered pipeline that turns product records into Seedance video prompts. A Flask webhook receives Bitable events, calls Gemini 2.5 Pro for multimodal analysis, produces a 12-grid storyboard, and writes Seedance prompts back to the source table.

## Stack

- Python, Flask
- Google Gemini 2.5 Pro API
- Seedance 2.0
- Feishu (Lark) Bitable API

## Pipeline

```
Feishu Bitable row created/updated
    └── Flask webhook receives event
         └── Gemini 2.5 Pro: multimodal product analysis
              └── 12-grid storyboard generated
                   └── Seedance 2.0 prompts written
                        └── Prompts written back to Bitable row
```

## Usage

```bash
pip install -r requirements.txt
cp .env.example .env   # fill Gemini key, Feishu credentials

# Start the webhook server
python app.py   # listens on :5000

# Expose locally for Bitable to reach (dev)
ngrok http 5000

# Trigger manually with a product JSON
python pipeline.py --product product.json --dry-run
```

## Structure

```
Marketing-Video-AI-Pipeline/
├── app.py              # Flask webhook entry
├── pipeline.py         # core pipeline (usable standalone)
├── storyboard.py       # 12-grid storyboard builder
├── seedance.py         # Seedance prompt generator
├── feishu_client.py    # Bitable read/write wrapper
└── .env.example
```

## Feishu Webhook Setup

1. In Bitable, open Automation and add a webhook trigger.
2. Set the URL to `https://your-host/webhook/bitable`.
3. Grant the app token read/write access to the target base.
