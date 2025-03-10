from sqlalchemy import ForeignKey, Column, Integer, String, create_engine
from sqlalchemy.orm import relationship, declarative_base

engine = create_engine('sqlite:///one_to_many.db')
Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    platform = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    reviews = relationship('Review', back_populates='game')

    def __repr__(self):
        return f'Game(id={self.id}, title={self.title}, platform={self.platform})'

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, autoincrement=True)
    score = Column(Integer, nullable=False)
    comment = Column(String, nullable=False)
    game_id = Column(Integer, ForeignKey('games.id'), nullable=False)

    game = relationship("Game", back_populates="reviews")

    def __repr__(self):
        return f'Review(id={self.id}, score={self.score}, game_id={self.game_id})'
