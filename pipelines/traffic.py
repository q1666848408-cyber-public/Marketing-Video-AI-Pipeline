"""
Traffic track — fan-acquisition video pipeline.
Two modes: dance (adult) and kids (CSAM-compliant content guardrails).
"""

from typing import Dict, Literal


class TrafficPipeline:
    def run(self, record: dict, mode: Literal["dance", "kids"]) -> Dict:
        """Mode-specific pipeline. [Not shown]"""
        pass

    def _dance_mode(self, record: dict) -> Dict:
        """4-grid character + env + Seedance dance prompts. [Not shown]"""
        pass

    def _kids_mode(self, record: dict) -> Dict:
        """Kids mode with safety guardrails. [Not shown]"""
        pass
