from transformers import pipeline
from Cogniezer.config.configuration import ConfigurationManager
from Cogniezer.logging import logger
from Cogniezer.components.model_loader import ModelLoader

class PredictionPipeline:
    def __init__(self):
        self.config_manager = ConfigurationManager()
        self.config=self.config_manager.get_model_config()

        self.tokenizer, self.model = ModelLoader(config=self.config).load()
    
    def predict(self,text):

        logger.info("Loading model")
        model_loader = ModelLoader(config=self.config)

        gen_kwargs = {"length_penalty":0.8,"num_beams":8,"max_length":512}

        pipe = pipeline("summarization", model=self.model, tokenizer=self.tokenizer)

        logger.info("Generating summary")
        logger.info(f"Input Text: {text}")
        
        summary = pipe(text, **gen_kwargs)[0]['summary_text']
        
        logger.info(f"Generated Summary: {summary}")
        return summary