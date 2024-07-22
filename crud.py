from sqlalchemy.orm import Session

from db import models
from db.models import DBCheeseType, DBCheese, PackagingType
from schemas import CheeseTypeCreate, CheeseBase, CheeseCreate


def get_all_cheese_types(db: Session):
    return db.query(DBCheeseType).all()


def create_cheese_type(db: Session, cheese_type: CheeseTypeCreate):
    db_cheese_type = DBCheeseType(
        name=cheese_type.name,
        description=cheese_type.description,
    )
    db.add(db_cheese_type)
    db.commit()
    db.refresh(db_cheese_type)
    return db_cheese_type


def get_cheese_type_by_id(db: Session, cheese_type_id: int):
    return db.query(DBCheeseType).filter(DBCheeseType.id == cheese_type_id).first()


def delete_cheese_type(db: Session, cheese_type_id: int):
    try:
        # Find the cheese type by ID
        cheese_type = db.query(DBCheeseType).filter(DBCheeseType.id == cheese_type_id).first()

        # Check if cheese type exists
        if cheese_type is None:
            return {"status": "error", "message": "Cheese type not found."}

        # Delete the cheese type
        db.delete(cheese_type)
        db.commit()

        return {"status": "success", "message": "Cheese type deleted successfully."}
    except Exception as e:
        db.rollback()
        return {"status": "error", "message": f"An error occurred: {str(e)}"}


def get_all_cheeses(
        db: Session,
        package_type: PackagingType | None = None,
        cheese_type: str | None = None,
):
    queryset = db.query(DBCheese)

    if package_type is not None:
        queryset = queryset.filter(models.DBCheese.package_type == package_type.value)

    if cheese_type is not None:
        queryset = queryset.filter(models.DBCheese.cheese_type.has(name=cheese_type))

    return queryset.all()


def create_cheese(db: Session, cheese: CheeseCreate) -> dict:
    try:
        db_cheese = DBCheese(
            title=cheese.title,
            price=cheese.price,
            package_type=cheese.package_type,
            cheese_type_id=cheese.cheese_type_id,
        )
        db.add(db_cheese)
        db.commit()
        db.refresh(db_cheese)

        return {"status": "success", "message": "Cheese created successfully.", "cheese": db_cheese.title}
    except Exception as e:
        db.rollback()
        return {"status": "error", "message": f"An error occurred: {str(e)}"}


def get_cheese_by_id(db: Session, cheese_id: int):
    try:
        db_cheese = db.query(DBCheese).filter(models.DBCheese.id == cheese_id).first()
        return db_cheese
    except Exception as e:
        return {"status": "error", "message": f"An error occurred: {str(e)}"}


def delete_cheese(db: Session, cheese_id: int):
    try:
        cheese = db.query(DBCheese).filter(DBCheese.id == cheese_id).first()
        db.delete(cheese)
        db.commit()

        return {"status": "success", "message": f"{cheese.title} deleted successfully."}
    except Exception as e:
        db.rollback()
        return {"status": "error", "message": f"An error occurred: {str(e)}"}
