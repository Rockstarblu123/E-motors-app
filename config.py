class config:
    SECRET KEY = ´3311546193´

    DEBUG       = True


class developmentConfig(config):
    MYSQL_HOST      = ´localhost´
    MYSQL_USER      =´root´
    MYSQL_PASSWORD  =´´
    MYSQL_DB()      =´E-motors´

config = {
    ´develoment´: developmentConfig
}