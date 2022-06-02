from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from config.db import meta, engine

item = Table(
    "items",
    meta,
    Column("typeId", Integer, primary_key=True ),
    Column("totalSize", Integer),
    Column("offset", Integer),
    relationship()



)

product = Table(
    "products",
    meta,
    Column("typeId", Integer, ForeignKey("items.typeId") ),
    Column("totalSize", Integer),
    Column("offset", Integer),
    relationship()



)

