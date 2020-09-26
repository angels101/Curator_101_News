import os
class Config:
    '''
    This is the parent configuration class
    '''
    NEWS_API_KEY='6edb7b566bad48f689bcc51c050f1db7'
    BASE_URL = "https://newsapi.org/v2/sources?q={}&apiKey={}"
    ARTICLES_BASE_URL='https://newsapi.org/v2/everything?sources={}&apikey={}'
    


class ProdConfig(Config):
    '''
    production configuration class which is a child of config class
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration class, child of the class Config
    '''
    DEBUG=True
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
