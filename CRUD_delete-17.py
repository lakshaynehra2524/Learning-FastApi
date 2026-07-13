from fastapi import FastAPI , Depends , HTTPException
from sqlalchemy import create_engine , Column , Integer , String
from sqlalchemy.orm import Session , sessionmaker , declarative_base

app = FastAPI()

DATABASE_URL = "sqlite:///./CRUD_delete_test.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

sessionLocal = sessionmaker(bind=engine)

Base = declarative_base

# Table (Model)
class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(String)

Base.metadata.create_all(bind=engine)
