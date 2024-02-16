import datetime
from .BaseModel import Base, str_uuid
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column


class Users(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(15), primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(String(32), nullable=False)
    reg_date: Mapped[datetime.datetime] = mapped_column(server_default="TIMEZONE('utc', now())", nullable=False)
