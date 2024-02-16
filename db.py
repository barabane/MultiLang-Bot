import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.Users import Users
from models.Words import Words
from models.UserWords import UserWords
from models.BaseModel import Base

load_dotenv()


class DB:
    def __init__(self):
        self.engine = create_engine(
            f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}",
            echo=True)
        self.session = sessionmaker(bind=self.engine)()
        self.metadata = Base.metadata

        self.metadata.create_all(bind=self.engine)
        # self.metadata.drop_all(bind=self.engine)


db = DB()
