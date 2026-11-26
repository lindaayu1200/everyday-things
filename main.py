import os
from pathlib import Path

TEXT = "A microwave oven is a lunchbox-sized drummer whose invisible beat nudges the water in your food until it heats up.\nThe drummer maps the oven's invisible waves nudging water, but leaves out that dry edges can stay cold and the food does not brown like it does in a regular oven."

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", Path(__file__).resolve().parent))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(TEXT + "\n", encoding="utf-8")
