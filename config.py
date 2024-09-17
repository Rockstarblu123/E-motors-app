class Config:
    SECRET_KEY  = 'pollomanhizounviajedelcualnuncavolvio' 
    DEBUG       = True

class DevelopmentConfig(Config):
    MYSQL_HOST      = 'localhost'
    MYSQL_USER      = 'root'
    MYSQL_PASSWORD  = 'mysql'
    MYSQL_DB        = 'hola'


config = {
    'development': DevelopmentConfig
}