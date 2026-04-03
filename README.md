# 🤖 Task Scheduler Bot (Python + Telegram)

A real-time task scheduling and reminder bot that sends notifications directly to Telegram using bot API integration.

---

## 🚀 Features

* ⏰ Schedule tasks with custom timing
* 📩 Receive reminders on Telegram
* 🔁 Supports multiple scheduled tasks
* ⚡ Real-time execution using Python scheduler
* 🤖 Telegram Bot API integration
* 🔄 Async handling for modern Python compatibility

---

## 🛠️ Tech Stack

* **Python**
* **python-telegram-bot**
* **schedule**
* **asyncio**

---

## 📂 Project Structure

```
task-scheduler-bot/
│
├── telegram_bot.py   # Main bot logic
└── README.md
```

---

## ⚙️ Setup & Run

### 1️⃣ Install dependencies

```
pip install python-telegram-bot schedule
```

---

### 2️⃣ Add credentials

Edit `telegram_bot.py`:

```
TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
```

---

### 3️⃣ Run the bot

```
python telegram_bot.py
```

---

## 📌 Example

```
Enter task: Study DSA
Remind after: 5
```

👉 You will receive a Telegram notification after 5 seconds.

---

## 📈 Future Improvements

* 📅 Schedule by date/time (not just seconds)
* 🌐 Web interface
* ☁️ Cloud deployment (24/7 bot)
* 📊 Task history tracking

---

## 👨‍💻 Author

**Advaith S**
B.Tech CSE Student

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
