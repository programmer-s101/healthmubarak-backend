from sqlalchemy import Column, Integer, String, Float
from app.database import Base
from pydantic import BaseModel

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    image = Column(String, nullable=True)


# ----------- Pydantic Response Model (for API JSON) -----------
class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    image: str | None = None

    class Config:
        orm_mode = True
