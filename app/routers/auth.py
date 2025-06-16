from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    tags=["Authentication"]
)

@router.post("/login")
async def login(db: Session = Depends(get_db)):
    
    return {"message": "login"}