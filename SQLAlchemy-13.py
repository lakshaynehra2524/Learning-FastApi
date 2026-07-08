from fastapi import FastAPI , Depends
from sqlalchemy import create_engine , Column , String , Integer
from sqlalchemy.orm import sessionmaker , session , declarative_base

app = FastAPI()

DATABASE_URL = "sqlite:///./SQLAlchemyDB_test.db"

engine = create_engine(
    DATABASE_URL ,
    connect_args={"check_same_thread":False}
)

sessionlocal = sessionmaker(bind=engine)

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer , primary_key=True , index=True)
    title = Column(String)
    completed = Column(String)

Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home(db:session = Depends(get_db)):
    return {
        "message":"DB connected!"
    }
