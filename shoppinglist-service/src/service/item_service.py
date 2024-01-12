import logging
from sqlalchemy.orm import Session
from models.item import Item

logger = logging.getLogger(__name__)

def create_item(db: Session, item_data):
    item = Item(**item_data.dict())
    db.add(item)
    try:
        db.commit()
        db.refresh(item)
        logger.info(f"Item {item.id} has been created.")
    except Exception as e:
        logger.error(f"Error occurred while creating an item: {e}")
        db.rollback()
        raise
    return item

def get_items(db: Session, skip: int = 0, limit: int = 100):
    items = db.query(Item).offset(skip).limit(limit).all()
    logger.info(f"Queried {len(items)} items, skipped: {skip}, limit: {limit}")
    return items

def get_item(db: Session, item_id: int):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        logger.info(f"Item {item_id} has been queried.")
    else:
        logger.warning(f"Item {item_id} not found.")
    return item

def update_item(db: Session, item_id: int, item_data):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        item_data_dict = item_data.dict(exclude_unset=True)
        for key, value in item_data_dict.items():
            setattr(item, key, value)
        try:
            db.commit()
            db.refresh(item)
            logger.info(f"Item {item_id} has been updated.")
        except Exception as e:
            logger.error(f"Error occurred while updating item {item_id}: {e}")
            db.rollback()
            raise
    else:
        logger.warning(f"Attempted to update a non-existent item {item_id}.")
    return item

def delete_item(db: Session, item_id: int):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        try:
            db.delete(item)
            db.commit()
            logger.info(f"Item {item_id} has been deleted.")
        except Exception as e:
            logger.error(f"Error occurred while deleting item {item_id}: {e}")
            db.rollback()
            raise
    else:
        logger.warning(f"Attempted to delete a non-existent item {item_id}.")
    return item
