"""
Seedance 2.0 prompt builder.
Produces Seedance-compatible video prompts from storyboard cells.
"""

from typing import List, Dict


class SeedancePromptBuilder:
    DURATION = 9  # seconds per clip
    PROMPT_LENGTH_TARGET = (100, 180)  # chars

    def build(self, storyboard_cells: List[Dict]) -> List[str]:
        """One Seedance prompt per cell. [Not shown]"""
        pass

    def _format_action(self, cell: dict) -> str:
        """Lead with action/dance description, extend to 350 chars max. [Not shown]"""
        pass
