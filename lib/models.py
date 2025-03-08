from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    platform = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    # Establish a one-to-many relationship
    reviews = relationship('Review', backref=backref('game', lazy=True), cascade="all, delete-orphan")

    def __repr__(self):
        return f'Game(id={self.id}, title="{self.title}", platform="{self.platform}")'

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    score = Column(Integer, nullable=False)
    comment = Column(String, nullable=True)
    game_id = Column(Integer, ForeignKey('games.id'), nullable=False)

    def __repr__(self):
        return f'Review(id={self.id}, score={self.score}, game_id={self.game_id})'

# Create the SQLite engine and bind it to a database file
engine = create_engine('sqlite:///one_to_many.db')
Base.metadata.create_all(engine)
