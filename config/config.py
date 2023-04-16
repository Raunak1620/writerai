
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}

## Enter your Open API Key here
OPENAI_API_KEY = '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'
