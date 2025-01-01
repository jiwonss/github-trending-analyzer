from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import ARRAY
from app.core.database import Base


class Repository(Base):
    __tablename__ = "repositories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    owner = Column(String, nullable=False)
    url = Column(String, nullable=False)
    description = Column(String, nullable=True)
    star_count = Column(Integer, nullable=False)
    fork_count = Column(Integer, nullable=False)
    language = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    pushed_at = Column(DateTime, nullable=False)
    topics = Column(ARRAY(String), nullable=True)
