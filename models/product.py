from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import declarative_base, relationship

from config.db import meta, engine

item = Table(
    "items",
    meta,
    Column("typeId", Integer, primary_key=True ),
    Column("totalSize", Integer),
    Column("offset", Integer),
    relationship("product")



)

product = Table(
    "products",
    meta,
    Column("id", Integer),
    Column("name", String(255)),
    Column("description", String(255)),
    Column("price", Integer),
    Column("stars", Integer),
    Column("img", String(255)),
    Column("location", String(255)),
    Column("createdAt", String(255)),
    Column("updatedAt", String(255)),
    Column("typeId", Integer, ForeignKey("items.typeId") ),
)

meta.create_all(engine)

