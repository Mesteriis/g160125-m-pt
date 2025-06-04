"""Load books data

Revision ID: 2e9e6d1f5da1
Revises: a718b23eaea0
Create Date: 2025-03-04 14:13:47.918506

"""
from typing import Sequence, Union
import json
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import Session
from models import Author, Book, Tag, book_tag_association


# revision identifiers, used by Alembic.
revision: str = '2e9e6d1f5da1'
down_revision: Union[str, None] = 'a718b23eaea0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    """Загружает данные из JSON в БД."""
    bind = op.get_bind()
    session = Session(bind=bind)

    # Очистка таблиц перед загрузкой новых данных
    session.execute(sa.text("DELETE FROM book_tag_association"))
    session.execute(sa.text("DELETE FROM books"))
    session.execute(sa.text("DELETE FROM authors"))
    session.execute(sa.text("DELETE FROM tags"))
    session.commit()

    with open("data/books.json", "r") as f:
        data = json.load(f)

    # Загружаем авторов
    for author in data["authors"]:
        session.execute(sa.insert(Author).values(id=author["id"], name=author["name"]))

    # Загружаем теги
    for tag in data["tags"]:
        session.execute(sa.insert(Tag).values(id=tag["id"], name=tag["name"]))

    # Загружаем книги
    for book in data["books"]:
        session.execute(sa.insert(Book).values(id=book["id"], title=book["title"], author_id=book["author_id"]))

    # Загружаем связи книг и тегов
    for book in data["books"]:
        for tag_id in book["tag_ids"]:
            session.execute(sa.insert(book_tag_association).values(book_id=book["id"], tag_id=tag_id))

    session.commit()


def downgrade():
    """Удаляет загруженные данные."""
    bind = op.get_bind()
    session = Session(bind=bind)
    session.execute(sa.text("DELETE FROM book_tag_association"))
    session.execute(sa.text("DELETE FROM books"))
    session.execute(sa.text("DELETE FROM authors"))
    session.execute(sa.text("DELETE FROM tags"))
    session.commit()