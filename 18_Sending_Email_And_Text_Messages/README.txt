 🚀 Python Automation: Chapter 18 - Email & SMS 📬

This repository documents my progress through Chapter 18, focusing on mastering communication protocols (SMTP, IM6P) and integrating them with system tasks to create automated workflows.

---

 🛠 Project Deep Dives

 🤖 Remote Download Daemon (`controllingYourComputerThroughEmail.py`)
This script turns your email into a remote control. It polls Gmail every 15 minutes. If it finds a specific email with a secret key (`123456`), it extracts a magnet link and initiates the download on the host PC using the `subprocess` module.

 ⚖️ The Fairness Engine (`randomChoreAssignmentEmailer.py`)
This script automates household management by distributing chores fairly. It reads a history file to ensure no person is assigned the same task they performed in the previous cycle, then shuffles and dispatches personalized emails to the group.

 🧹 Auto-Unsubscriber (`autoUnsubscriber.py`)
Automates the detection of "Unsubscribe" links hidden in marketing emails. It utilizes `BeautifulSoup` with a custom `lambda` filter to locate the exact URL required to clean up an inbox.

 💰 Dues Reminder (`sendDuesReminder.py`)
An administrative tool bridging Excel and Email. It parses member records from a spreadsheet and automatically drafts and sends reminders to any individual whose payment status is not marked as "paid."

 ⛈ Umbrella Alert (`umbrellaReminder.py` & `textMyself.py`)
A weather-aware automation. It queries the OpenWeatherMap API for regional forecasts. If rain is detected in the immediate forecast, it utilizes the Twilio API to send a "Carry an Umbrella" SMS alert.

---

 ⚙️ Technical Requirements

To run these scripts, the following libraries are required:

```bash
pip install imapclient pyzmail36 beautifulsoup4 openpyxl requests twilio