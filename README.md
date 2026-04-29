# 🚗 Autoservice Web System

Информационная система автосервиса, разработанная на Django в рамках курсовой работы.

---

## 📌 Описание проекта

Система предназначена для автоматизации работы автосервиса и включает:

* управление пользователями и ролями
* учёт автомобилей клиентов
* оформление заказов на ремонт
* каталог услуг (карточки)
* чат между пользователями
* форум
* финансовую систему (баланс и транзакции)

---

## 🛠 Технологии

* Python 3.11+
* Django
* PostgreSQL
* HTML / CSS / JavaScript

---

## ⚙️ Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone <repo_url>
cd autoservice
```

### 2. Создать виртуальное окружение

```bash
python -m venv venv
```

### 3. Активировать окружение

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### 4. Установить зависимости

```bash
pip install -r requirements.txt
```

### 5. Выполнить миграции

```bash
python manage.py migrate
```

### 6. Запустить сервер

```bash
python manage.py runserver
```

---

## 📁 Структура проекта

```
autoservice/
├── apps/
│   ├── users/
│   ├── cars/
│   ├── orders/
│   ├── services_app/
│   ├── chat/
│   ├── forum/
│   ├── finance/
│   ├── media_files/
│   └── moderation/
├── autoservice/
├── templates/
├── static/
└── media/
```

---

## 📊 Архитектура

Проект реализован по архитектуре MVT (Model-View-Template) с использованием Django ORM и PostgreSQL.

---
