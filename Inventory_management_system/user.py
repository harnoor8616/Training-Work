import csv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
db_url=os.getenv("DATABASE_URL")
base=declarative_base()
class User(base):
    __tablename__="InvyTrack_Users"
    sr_no=Column(Integer,primary_key=True,autoincrement=True)
    username=Column(String(50),unique=True,nullable=False)
    password=Column(String(100),nullable=True)
class Manage_user:
    def __init__(self,username,password,is_file_based=False):
        self.username=username
        self.password=password
        self.is_file_based=is_file_based
        if not self.is_file_based:
            self.engine = create_engine(db_url)
            base.metadata.create_all(self.engine)
            Session = sessionmaker(bind=self.engine)
            self.session = Session()
    def save_to_csv(self):
        try:
            with open(file="InvyTrack_Users.csv",mode="a",newline="") as file:
                writer=csv.writer(file)
                writer.writerow([self.username, self.password])
            print("Credentials saved to .csv file successfully")
        except Exception as e:
            print(f"Error: {e}")
    def save_to_database(self):
        pass