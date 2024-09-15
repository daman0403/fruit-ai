from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

app = FastAPI()

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class FAQModel(Base):
    __tablename__ = "faqs"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, index=True)
    answer = Column(String)

Base.metadata.create_all(bind=engine)

class FAQ(BaseModel):
    id: Optional[int]
    question: str
    answer: str

    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/faqs", response_model=List[FAQ])
def get_faqs(db: SessionLocal = Depends(get_db)):
    faqs = db.query(FAQModel).all()
    return faqs

@app.get("/faqs/{faq_id}", response_model=FAQ)
def get_faq(faq_id: int, db: SessionLocal = Depends(get_db)):
    faq = db.query(FAQModel).filter(FAQModel.id == faq_id).first()
    if faq is None:
        raise HTTPException(status_code=404, detail="FAQ not found")
    return faq

@app.post("/faqs", response_model=FAQ)
def create_faq(faq: FAQ, db: SessionLocal = Depends(get_db)):
    db_faq = FAQModel(**faq.dict(exclude={"id"}))
    db.add(db_faq)
    db.commit()
    db.refresh(db_faq)
    return db_faq

@app.put("/faqs/{faq_id}", response_model=FAQ)
def update_faq(faq_id: int, faq: FAQ, db: SessionLocal = Depends(get_db)):
    db_faq = db.query(FAQModel).filter(FAQModel.id == faq_id).first()
    if db_faq is None:
        raise HTTPException(status_code=404, detail="FAQ not found")
    for key, value in faq.dict(exclude={"id"}).items():
        setattr(db_faq, key, value)
    db.commit()
    db.refresh(db_faq)
    return db_faq

@app.delete("/faqs/{faq_id}")
def delete_faq(faq_id: int, db: SessionLocal = Depends(get_db)):
    db_faq = db.query(FAQModel).filter(FAQModel.id == faq_id).first()
    if db_faq is None:
        raise HTTPException(status_code=404, detail="FAQ not found")
    db.delete(db_faq)
    db.commit()
    return {"message": "FAQ deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)