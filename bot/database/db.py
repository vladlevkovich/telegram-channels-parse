from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine, async_scoped_session
from asyncio import current_task
from bot.config.config import settings
from typing import AsyncGenerator


class Database:
    def __init__(self):
        self.engine = create_async_engine(url=settings.DB_URL, echo=True)
        self.session = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )

    def get_scoped_session(self):
        session = async_scoped_session(session_factory=self.session, scopefunc=current_task)
        yield session


db = Database()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with db.session() as session:
        yield session
