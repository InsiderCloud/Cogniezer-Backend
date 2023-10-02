from Cogniezer.constants import CONFIG_PATH, PARAMS_PATH
from Cogniezer.entity import AiModelConfig
from Cogniezer.utils.common import read_yaml,create_directories

class ConfigurationManager:
    def __init__(
            self,
            config_path=CONFIG_PATH,
            params_path=PARAMS_PATH):
        
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)

        create_directories([self.config.artifacts_root])

    def get_model_config(self)-> AiModelConfig:
        config = self.config.model

        create_directories([config.root_dir])

        model_config = AiModelConfig(
            root_dir=config.root_dir,
            model_dir=config.model_dir,
            tokenizer_dir=config.tokenizer_dir
        )

        return model_config