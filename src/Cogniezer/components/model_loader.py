import os
from Cogniezer.entity import AiModelConfig
from transformers import AutoTokenizer, Trainer, TrainingArguments
from transformers import AutoModelForSeq2SeqLM, DataCollatorForSeq2Seq
from datasets import load_dataset, load_from_disk
import torch
from Cogniezer.logging import logger

class ModelLoader:
    def __init__(self, config:AiModelConfig):
        self.config = config

    def load(self):
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        logger.info(f"Using device: {device}")
        tokernizer = AutoTokenizer.from_pretrained(self.config.tokenizer_dir)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_dir).to(device)

        return tokernizer, model
