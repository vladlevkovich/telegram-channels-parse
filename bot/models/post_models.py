from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import LargeBinary, ForeignKey
from sqlalchemy import func
from bot.database.base import Base
import datetime


class Channel(Base):
    __tablename__ = 'channels'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    channel: Mapped[str] = mapped_column(index=True, unique=True)
    created: Mapped[datetime.datetime] = mapped_column(server_default=func.now())


class Post(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=True)
    body: Mapped[str] = mapped_column(nullable=True)
    author: Mapped[str] = mapped_column(nullable=True)
    photo: Mapped[bytes] = mapped_column(nullable=True)
    created: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
