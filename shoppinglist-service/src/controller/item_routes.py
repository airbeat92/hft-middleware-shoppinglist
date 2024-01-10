import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.schemas.item_schema import ItemCreate, ItemRead, ItemUpdate
from src.database import get_db
from src.service.item_service import create_item, get_items, get_item, update_item, delete_item

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", response_model=ItemRead)
async def create_item_route(item: ItemCreate, db: Session = Depends(get_db)):
    try:
        result = create_item(db=db, item_data=item)
        logger.info(f"Created an item with id {result.id}")
        return result
    except Exception as e:
        logger.error(f"Error occurred while creating an item: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/", response_model=List[ItemRead])
async def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        items = get_items(db, skip=skip, limit=limit)
        logger.info(f"Retrieved {len(items)} items")
        return items
    except Exception as e:
        logger.error(f"Error occurred while retrieving items: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{item_id}", response_model=ItemRead)
async def read_item(item_id: int, db: Session = Depends(get_db)):
    try:
        db_item = get_item(db, item_id=item_id)
        if db_item is None:
            logger.warning(f"Item with id {item_id} not found")
            raise HTTPException(status_code=404, detail="Item not found")
        logger.info(f"Retrieved item with id {item_id}")
        return db_item
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error occurred while retrieving item {item_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{item_id}", response_model=ItemRead)
async def update_item_route(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    try:
        db_item = update_item(db, item_id=item_id, item_data=item)
        if db_item is None:
            logger.warning(f"Attempted to update non-existent item with id {item_id}")
            raise HTTPException(status_code=404, detail="Item not found")
        logger.info(f"Updated item with id {item_id}")
        return db_item
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error occurred while updating item {item_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{item_id}", response_model=ItemRead)
async def delete_item_route(item_id: int, db: Session = Depends(get_db)):
    try:
        db_item = delete_item(db, item_id=item_id)
        if db_item is None:
            logger.warning(f"Attempted to delete non-existent item with id {item_id}")
            raise HTTPException(status_code=404, detail="Item not found")
        logger.info(f"Deleted item with id {item_id}")
        return db_item
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error occurred while deleting item {item_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))
