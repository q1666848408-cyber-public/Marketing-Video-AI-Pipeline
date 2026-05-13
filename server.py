"""
Flask entrypoint — Feishu Bitable automation endpoints.
Showcase version: routing only, handlers omitted.
"""

from flask import Flask, request, jsonify
from pipelines.marketing import MarketingPipeline
from pipelines.traffic import TrafficPipeline

app = Flask(__name__)
marketing = MarketingPipeline()
traffic = TrafficPipeline()


@app.route("/api/marketing", methods=["POST"])
def trigger_marketing():
    payload = request.get_json()
    # [Async job dispatch not shown]
    return jsonify({"code": 0})


@app.route("/api/traffic", methods=["POST"])
def trigger_traffic():
    payload = request.get_json()
    # [Mode routing (dance/kids) not shown]
    return jsonify({"code": 0})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
