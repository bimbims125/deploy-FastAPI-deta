import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, relationship

Base =  declarative_base()

class Film(Base):
  __tablename__ = 'film'

  id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
  title = sa.Column(sa.String(30), nullable=False)
  description = sa.Column(sa.String(1000), nullable=False)

class Author(Base):

  __tablename__ = 'author'

  id =  sa.Column(sa.Integer, primary_key=True, autoincrement=True)
  name =   sa.Column(sa.String(255), nullable=False)
  email = sa.Column(sa.String(255), nullable=False)
  blog = relationship('Blog', backref='author', lazy='joined')

class Blog(Base):

  __tablename__ = 'blog'

  id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
  title = sa.Column(sa.String(255), nullable=False, unique=True)
  slug = sa.Column(sa.String(255), nullable=False, unique=True)
  body = sa.Column(sa.Text, nullable=False)
  author_id = sa.Column(sa.Integer, sa.ForeignKey('author.id'))


