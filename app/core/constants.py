from ast import Constant
from collections import namedtuple

cDB_DRIVER = Constant(value="mysql+pymysql")
cAPP_HOST = Constant(value="localhost")
cAPP_PORT = Constant(value=5000)
cDB_HOST = Constant(value="localhost")
cDB_PORT = Constant(value=3306)
cDB_NAME = Constant(value="tutorial_db")
cDB_USER = Constant(value="root")
cDB_PASSWORD = Constant(value="")
cJWT_SECRET_KEY = Constant(value="secret_key")
cALGORITHM = Constant(value="HS256")
cACCESS_TOKEN_EXPIRE_MINUTES = Constant(value=10)
cREFRESH_TOKEN_EXPIRE_DAYS = Constant(value=7)