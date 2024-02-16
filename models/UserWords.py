from .BaseModel import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class UserWords(Base):
    __tablename__ = "user_words"

    user_id: Mapped[str] = mapped_column(String(15), ForeignKey("users.id"), primary_key=True, nullable=False)
    word_id: Mapped[str] = mapped_column(String(36), ForeignKey("words.id"), nullable=False)
