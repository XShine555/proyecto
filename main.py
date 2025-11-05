from dotenv import load_dotenv

load_dotenv()

from sqlmodel import Session
from db import dbcontext

dbcontext.init_db()

session: Session = dbcontext.get_session()