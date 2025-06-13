### Шаг (Задание) 1: МОДЕЛИ И МИГРАЦИЯ

**Задание**:  
- Добавить в `models.py` ассоциативную таблицу `founditem_tag` (если ещё нет), где `found_item_id` и `tag_id` — первичные ключи.  
- В модели `FoundItem` добавить поле `tags`, а в `Tag` — поле `found_items`, связывающее их через `founditem_tag`.  
- Создать и применить Alembic-миграцию, которая создаст таблицу `founditem_tag`.

---

### Шаг (Задание) 2: СХЕМЫ И ЭНДПОИНТ

**Задание**:  
- Обновить `schemas.py`, если нужно, чтобы FoundItem-схемы возвращали список тегов.  
- Убедиться, что при получении FoundItem (GET /found_items) вы используете `selectinload(FoundItem.tags)` или аналог, чтобы теги загружались.

---

### Шаг (Задание) 3: ЭНДПОИНТЫ ДЛЯ ПРИВЯЗКИ/ОТВЯЗКИ

**Задание**:  
- Создать два маршрута в `routers/found_items.py`, аналогичные LostItem:  
  - `POST /found_items/{found_item_id}/tags?tag_id=...` — привязка тега (attach).  
  - `DELETE /found_items/{found_item_id}/tags/{tag_id}` — отвязка (detach).  
- Не забыть использовать `selectinload(FoundItem.tags)` перед обращением к `found_item.tags`, чтобы избежать lazy load.  

