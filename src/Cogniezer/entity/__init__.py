from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class AiModelConfig:
    root_dir: Path
    model_dir: Path
    tokenizer_dir: Path