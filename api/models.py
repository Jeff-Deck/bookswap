from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey
from api.database import Base
from datetime import datetime


class CustomUser(Base):
    __tablename__ = 'users_customuser'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    cedula = Column(String)
    phone = Column(String)
    country = Column(String)
    province = Column(String)
    city = Column(String)


class Book(Base):
    __tablename__ = 'books_book'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    genre = Column(String)
    condition = Column(String)
    location = Column(String)
    created_at = Column(DateTime)
    owner_id = Column(Integer, ForeignKey('users_customuser.id'))
    available = Column(Boolean)


class ExchangeRequest(Base):
    __tablename__ = 'books_exchangerequest'

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String)
    timestamp = Column(DateTime)
    book_id = Column(Integer, ForeignKey('books_book.id'))
    receiver_id = Column(Integer, ForeignKey('users_customuser.id'))
    sender_id = Column(Integer, ForeignKey('users_customuser.id'))


class ExchangeHistory(Base):
    __tablename__ = 'books_exchangehistory'

    id = Column(Integer, primary_key=True, index=True)
    exchanged_on = Column(DateTime)
    book_id = Column(Integer, ForeignKey('books_book.id'))
    receiver_id = Column(Integer, ForeignKey('users_customuser.id'))
    sender_id = Column(Integer, ForeignKey('users_customuser.id'))


class ExchangeRating(Base):
    __tablename__ = 'exchange_ratings'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    exchange_id = Column(Integer)
    rater_id = Column(Integer, ForeignKey('users_customuser.id'))
    rated_user_id = Column(Integer, ForeignKey('users_customuser.id'))
    score = Column(Integer)
    comment = Column(Text)
    rated_at = Column(DateTime)

class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, index=True)
    exchange_request_id = Column(Integer, ForeignKey('books_exchangerequest.id'))
    sender_id = Column(Integer, ForeignKey('users_customuser.id'))
    content = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
