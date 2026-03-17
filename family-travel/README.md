# Семейный туристический портал «ФЭМИЛИ ТРЭВЕЛ»

Проект разработан с использованием **Django + React + PostgreSQL**.

## Запуск локально

### Способ 1: без Docker (для разработки)
1. **Бэкенд**:
   - Создайте базу PostgreSQL.
   - В папке `backend` выполните:
     ```bash
     pip install -r requirements.txt
     python manage.py migrate
     python manage.py createsuperuser
     python manage.py runserver
