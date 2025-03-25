# Создать простую структуру данных в представлениях по типу:
# info = {
#     "users_count": 100600,
#     "news_count": 100600,
#     "menu": [
#         {"title": "Главная",
#          "url": "/",
#          "url_name": "index"},
#         {"title": "О проекте",
#          "url": "/about/",
#          "url_name": "about"},
#         {"title": "Каталог",
#          "url": "/news/catalog/",
#          "url_name": "catalog"},
#     ]
# }
# Передать данные в шаблон catalog.html
# Меню "Главная - О проекте - Каталог" должно выводиться с помощью цикла

#   Описать маршруты 
#   /catalog,
#   /catalog/<int:news_id/>,
#   /catalog/<slug:slug>
#   и создали соответствующие представления в файле views.py
#   catalog возвращает HttpResponse("Каталог новостей")
#   get_news_by_id возвращает HttpResponse(f"Новость {news_id}")
#   get_category_by_name возвращает HttpResponse(f"Категория {slug}")
