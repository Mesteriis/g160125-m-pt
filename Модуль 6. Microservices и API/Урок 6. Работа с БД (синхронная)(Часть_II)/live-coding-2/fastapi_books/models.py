from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base


# Ассоциативная таблица для связи многие ко многим (книги - теги)
book_tag_association = Table(
    "book_tag_association",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("books.id")),
    Column("tag_id", Integer, ForeignKey("tags.id"))
)


class Author(Base):
    """Модель автора книг."""
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    # Один автор может написать несколько книг (1:N)
    books = relationship("Book", back_populates="author")


class Tag(Base):
    """Модель жанра (тега), который может быть у книги."""
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    # Один тег может быть у нескольких книг, связь через book_tag_association (M:N)
    books = relationship("Book", secondary=book_tag_association, back_populates="tags")


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("authors.id"))
    # У каждой книги есть один автор (N:1)
    author = relationship("Author", back_populates="books")
    # У каждой книги может быть несколько тегов (M:N)
    tags = relationship("Tag", secondary=book_tag_association, back_populates="books")
