from pathlib import Path
from sys import platform
from os import getenv


class Config:

    # Config Environment Variables
    MONGO_SERVER = 'MONGO_SERVER'
    MONGO_PORT = 'MONGO_PORT'
    MONGO_USER = 'MONGO_USER'
    MONGO_PASSWORD = 'MONGO_PASSWORD'
    DB_SERVER = 'DB_SERVER'
    DB_PORT = 'DB_PORT'
    DB_USER = 'DB_USER'
    DB_PASSWORD = 'DB_PASSWORD'
    DB_DATABASE = 'DB_DATABASE'
    BROKER_NAME = 'BROKER_NAME'
    BROKER_PORT = 'BROKER_PORT'
    BROKER_TIMEOUT = 'BROKER_TIMEOUT'
    BROKER_USER = 'BROKER_USER'
    BROKER_PASSWORD = 'BROKER_PASSWORD'
    HOST_HOSTNAME='HOST_HOSTNAME'
    

    @property
    def broker_name(self):
        return getenv(self.BROKER_NAME)

    @property
    def broker_port(self):
        return getenv(self.BROKER_PORT)

    @property
    def broker_user(self):
        return getenv(self.BROKER_USER)

    @property
    def broker_password(self):
        return getenv(self.BROKER_PASSWORD)

    @property
    def db_server(self):
        return getenv(self.DB_SERVER)

    @property
    def db_port(self):
        return getenv(self.DB_PORT)

    @property
    def db_user(self):
        return getenv(self.DB_USER)

    @property
    def db_password(self):
        return getenv(self.DB_PASSWORD)

    @property
    def db_database(self):
        return getenv(self.DB_DATABASE)

    @property
    def mongo_server(self):
        return getenv(self.MONGO_SERVER)

    @property
    def mongo_port(self):
        return getenv(self.MONGO_PORT)

    @property
    def mongo_user(self):
        return getenv(self.MONGO_USER)

    @property
    def mongo_password(self):
        return getenv(self.MONGO_PASSWORD)
    
    @property
    def hostname(self):
        return getenv(self.HOST_HOSTNAME)    
    

    
