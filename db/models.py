from enum import StrEnum, auto

from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship

from db.engine import Base


class PackagingType(StrEnum):
    IN_PACKAGE = auto()
    WEIGHT = auto()


class DBCheeseType(Base):
    __tablename__ = "cheese_type"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(String(511), nullable=False)


class DBCheese(Base):
    __tablename__ = "cheese"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String(255), nullable=False, unique=True)
    price = Column(Integer, nullable=False)
    package_type = Column(Enum(PackagingType), nullable=False)
    cheese_type_id = Column(Integer, ForeignKey("cheese_type.id"), nullable=False)

    cheese_type = relationship(DBCheeseType)  # creating relations
