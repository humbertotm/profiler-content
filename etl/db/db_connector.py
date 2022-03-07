import os, psycopg2, yaml

CONFIG_PATH = os.environ['APP_PATH'] + '/config/config.yml'

class DBConnector():
    __instance = None

    def __new__(cls):
        if DBConnector.__instance is None:
            config_file = open(CONFIG_PATH, 'r')
            config_data = yaml.load(config_file, Loader=yaml.Loader)
            db_host = config_data['db']['host']
            db_port = config_data['db']['port']
            target_db = config_data['db']['name']
            db_username = config_data['db']['user']
            db_user_pwd = config_data['db']['password']

            DBConnector.__instance = psycopg2.connect(host=db_host, port=db_port, dbname=target_db, user=db_username, password=db_user_pwd)

        return DBConnector.__instance

    @classmethod
    def disconnect(cls):
        if DBConnector.__instance is None:
            return
        else:
            DBConnector.__instance.close()
            DBConnector.__instance = None
            return

