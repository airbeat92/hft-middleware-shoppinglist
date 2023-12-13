from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.schemas.item_schema import ItemCreate, ItemRead, ItemUpdate
from src.database import get_db
from src.service.item_service import create_item, get_items, get_item, update_item, delete_item

router = APIRouter()


@router.post("/", response_model=ItemRead)
async def create_item_route(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db=db, item_data=item)


@router.get("/", response_model=List[ItemRead])
async def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_items(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=ItemRead)
async def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.put("/{item_id}", response_model=ItemRead)
async def update_item_route(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    db_item = update_item(db, item_id=item_id, item_data=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.delete("/{item_id}", response_model=ItemRead)
async def delete_item_route(item_id: int, db: Session = Depends(get_db)):
    db_item = delete_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item