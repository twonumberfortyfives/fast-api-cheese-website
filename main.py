from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from db.engine import SessionLocal

app = FastAPI()


def get_db() -> Session:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root() -> dict:
    return {"message": "Hello World"}


@app.get("/cheese-types/", response_model=list[schemas.CheeseTypeList])
def get_cheese_types(db: Session = Depends(get_db)) -> list:
    return crud.get_all_cheese_types(db)


@app.get("/retrieve-cheese-type/{cheese_type_id}", response_model=schemas.CheeseTypeList)
def retrieve_cheese_type(cheese_type_id: int, db: Session = Depends(get_db)):
    cheese_type = crud.get_cheese_type_by_id(db, cheese_type_id)
    if cheese_type is None:
        raise HTTPException(status_code=404, detail="Cheese type not found")
    return cheese_type


@app.post("/create-cheese-type/", response_model=schemas.CheeseTypeCreate)
def create_cheese_type(
        cheese_type: schemas.CheeseTypeCreate,
        db: Session = Depends(get_db)
) -> dict:
    return crud.create_cheese_type(db, cheese_type)


@app.delete("/delete-cheese-type/{cheese_type_id}", response_model=dict)
def delete_cheese_type(cheese_type_id: int, db: Session = Depends(get_db)) -> dict:
    response = crud.delete_cheese_type(db, cheese_type_id)

    if response['status'] == "success":
        return {"message": "Cheese type deleted successfully."}
    else:
        raise HTTPException(status_code=404, detail=response['message'])


@app.get("/cheeses/", response_model=list[schemas.CheeseList])
def get_cheeses(db: Session = Depends(get_db)) -> list:
    return crud.get_all_cheeses(db=db)


@app.post("/create-cheese/", response_model=dict)
def create_cheese(cheese: schemas.CheeseCreate, db: Session = Depends(get_db)) -> dict:
    response = crud.create_cheese(db, cheese)
    if response['status'] == "success":
        return response
    else:
        raise HTTPException(status_code=404, detail=response)


@app.get("/cheese/{cheese_id}/", response_model=schemas.CheeseList)
def get_cheese_by_id(cheese_id: int, db: Session = Depends(get_db)):
    return crud.get_cheese_by_id(db, cheese_id)


@app.delete("/cheese-delete/{cheese_id}", response_model=dict)
def delete_cheese(cheese_id: int, db: Session = Depends(get_db)) -> dict:
    return crud.delete_cheese(db, cheese_id)
