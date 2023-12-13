from sqlalchemy.orm import Session
from src.models.item import Item


def create_item(db: Session, item_data):
    item = Item(**item_data.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()


def update_item(db: Session, item_id: int, item_data):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        item_data_dict = item_data.dict(exclude_unset=True)
        for key, value in item_data_dict.items():
            setattr(item, key, value)
        db.commit()
        db.refresh(item)
    return item


def delete_item(db: Session, item_id: int):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
    return item

