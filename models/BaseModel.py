from uuid import uuid4
from typing import Annotated
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, mapped_column
from sqlalchemy import UUID, String


def generated_uuid():
    return str(uuid4())


str_uuid = Annotated[str, mapped_column(String(36), primary_key=True, default=generated_uuid)]


class Base(DeclarativeBase, MappedAsDataclass):
    pass
