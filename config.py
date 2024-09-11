class Config:
    SECRET_KEY  = 'pollomanhizounviajedelcualnuncavolvio' 
    DEBUG       = True

class DevelopmentConfig(Config):
    MYSLQ_HOST      = 'localhost'
    MYSLQ_USER      = 'root'
    MYSLQ_PASSWORD  = ''
    MYSLQ_DB        = 'lectura'

config = {
    'development': DevelopmentConfig
}