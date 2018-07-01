from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(32),nullable=True,default='sf',index=True)
    email = Column(String(16),unique=True)
    # 创建组合索引
    __table_args__ = (
        UniqueConstraint('id', 'name', name='uix_id_name'),
        Index('ix_id_name', 'name', 'extra'),
    )

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/ormdb?charset=utf8', max_overflow=5)
Base.metadata.create_all(engine)

