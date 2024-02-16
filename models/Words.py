from .BaseModel import Base, str_uuid
from sqlalchemy import String, VARCHAR, UUID
from sqlalchemy.orm import Mapped, mapped_column


class Words(Base):
    __tablename__ = "words"

    id: Mapped[str_uuid]
    word: Mapped[str] = mapped_column(String(100), nullable=False)
    translate: Mapped[str] = mapped_column(String(100), nullable=False)
    language_code: Mapped[str] = mapped_column(VARCHAR(2), nullable=False)
