from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import func
from bot.database.base import Base
import datetime


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(unique=True, index=True)
    user_first_name: Mapped[str] = mapped_column(nullable=True)
    user_last_name: Mapped[str] = mapped_column(nullable=True)
    created: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
