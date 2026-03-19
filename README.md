# 🤖 AI Telegram Task Assistant

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue" />
  <img src="https://img.shields.io/badge/aiogram-3.x-green" />
  <img src="https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram" />
  <img src="https://img.shields.io/badge/status-active-success" />
</p>

<p align="center">
  Telegram-бот с продуктовой логикой, который помогает пользователю разложить задачу и получить план действий.
</p>

---

## 🚀 Demo

👉 Открыть бота: https://t.me/Zaich_task_helper_bot

---

## ✨ Features

* 💰 Анализ запросов про доход и карьеру
* 📚 Рекомендации по обучению и навыкам
* 🚀 Планирование роста
* 🧠 Разбор пользовательских ситуаций
* 🎛 Кнопочный интерфейс
* ⚡ Быстрые ответы без внешних API

---

## 🖼 Пример работы

**Input:**

```text id="ex1"
хочу зарабатывать больше
```

**Output:**

```text id="ex2"
💰 Цель:
Выйти на доход 300–500k+

🔍 Анализ:
Сейчас нет чёткой стратегии роста

🛠 План:
1. Определи навыки
2. Выбери направление
3. Найди источники дохода

⚡ Быстрые шаги:
- Обнови резюме
- Откликнись на вакансии
```

---

## 🧱 Архитектура

```text id="arch"
Telegram → bot.py → ai_service.py → Response
```

* `bot.py` — обработка сообщений и UX
* `ai_service.py` — логика анализа

---

## 📁 Структура проекта

```bash id="struct"
ai-telegram-task-bot/
│
├── app/
│   ├── bot.py
│   ├── ai_service.py
│
├── README.md
├── requirements.txt
└── .env.example
```

---

## ⚙️ Установка

```bash id="install"
git clone https://github.com/tatsnaoblako-png/ai-telegram-task-bot
cd ai-telegram-task-bot
pip install -r requirements.txt
```

Создать `.env`:

```env id="env"
BOT_TOKEN=your_telegram_token
```

---

## ▶️ Запуск

```bash id="run"
python app/bot.py
```

---

## 🧠 Product thinking

Проект демонстрирует:

* проектирование пользовательских сценариев
* UX через Telegram-интерфейс
* декомпозицию задач
* имитацию AI-логики

---

## 📈 Roadmap

* [ ] Интеграция OpenAI
* [ ] Персонализация
* [ ] Хранение истории
* [ ] Web-интерфейс

---

## 👩‍💻 Author

Системный / бизнес-аналитик
Фокус: AI, автоматизация, цифровые продукты

---

## ⭐ Value

Этот проект показывает:

👉 не просто код
👉 а умение строить продукт

---

<p align="center">
  🚀 Ready to scale into real AI product
</p>
