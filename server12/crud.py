from sqlalchemy.orm import Session
from models import Pair
from server12.schemas import PairCreate

def get_pair(db: Session, pair_id):
    return db.query(Pair).filter(Pair.id == pair_id).first()

def create_pair(db: Session, pair: PairCreate, pair_id):
    db_pair = Pair(pair_id, **pair.dict())
    db.add(db_pair)
    db.commit()
    db.refresh(db_pair)
    return db_pair