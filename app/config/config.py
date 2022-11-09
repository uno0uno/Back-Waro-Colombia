import os
from dotenv import load_dotenv
from pathlib import Path

# ============================================================
# Configuration .evn WAROCOL.COM
# ============================================================

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:

    PROJECT_NAME:str = "MAGIC 1 WARO COLOMBIA"
    PROJECT_VERSION:str = "1.0"
    USR_MONGO_DB:str = os.getenv('USR_MONGO_DB')
    PASS_MONGO_DB:str = os.getenv('PASS_MONGO_DB')
    CLUSTER_MONGO_DB:str = os.getenv('CLUSTER_MONGO_DB')
    URL_CLUSTER_MONGO_DB = f"mongodb+srv://{USR_MONGO_DB}:{PASS_MONGO_DB}@{CLUSTER_MONGO_DB}.snrqy.mongodb.net/db?retryWrites=true&w=majority"


settings = Settings()

JWT_SECRET:str = os.getenv('AUTH_JWT_SECRET')
JWT_ALGORITHM:str = os.getenv('ALGORITHM')

PROJECT_ID_INFURA:str = os.getenv('PROJECT_ID_INFURA')
PROJECT_SECRET_INFURA:str = os.getenv('PROJECT_SECRET_INFURA')
END_POINT_INFURA:str = os.getenv('END_POINT_INFURA')
