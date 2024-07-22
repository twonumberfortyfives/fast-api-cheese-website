from pydantic import BaseModel

from db.models import PackagingType


class CheeseTypeBase(BaseModel):
    name: str
    description: str


class CheeseTypeCreate(CheeseTypeBase):
    pass


class CheeseTypeList(CheeseTypeBase):
    id: int

    class Config:
        from_attributes = True


class CheeseBase(BaseModel):
    title: str
    price: int
    package_type: PackagingType


class CheeseList(CheeseBase):
    id: int
    cheese_type: CheeseTypeList

    class Config:
        from_attributes = True


class CheeseCreate(CheeseBase):
    cheese_type_id: int
