from configparser import ConfigParser

class Config:
    def __init__(self, config_file="src/langgraphagenticai/ui/uniconfigfile.ini"):
        self.config=ConfigParser()
        self.config.read(config_file)
        
    def get_llm_options(self): 
        return self._get_list_option("LLM_OPTIONS")

    def get_usecase_options(self):
        return self._get_list_option("USECASE_OPTIONS")

    def get_groq_model_options(self):
        return self._get_list_option("GROQ_MODEL_OPTIONS")

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE", "AgenticAI")

    def _get_list_option(self, key):
        value = self.config["DEFAULT"].get(key)
        if not value:
            raise ValueError(f"⚠️ Missing required config key: '{key}' in .ini file.")
        return [item.strip() for item in value.split(",")]
