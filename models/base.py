from db import db
from sqlalchemy import MetaData

class BaseModel(db.Model):
    """
    class to standardize constraint names across db engines
    see: alembic.sqlalchemy.org/en/latest/naming.html
    """
    __abstract__ = True
    metadata = MetaData(naming_convention={
        "ix": 'ix_%(column_0_label)s',
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    })