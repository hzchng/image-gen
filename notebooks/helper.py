from pathlib import Path


root_dir = Path(__file__).parents[1]
output_dir = root_dir / "outputs"

base_model_dir = Path.home() / ".omlx/models/ImageGen"
