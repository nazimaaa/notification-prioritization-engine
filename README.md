# AI-Native Notification Prioritization Engine

## 📌 Problem Statement
Users receive too many notifications from different services (messages, reminders, alerts, promotions). 
This leads to alert fatigue, duplicate notifications, and missed critical alerts.

This system classifies every incoming notification into:
- NOW
- LATER
- NEVER

---

## 🏗 Architecture Overview

Event → Preprocessing → Duplicate Check → User Context →  
Scoring Engine → Decision (NOW/LATER/NEVER) → Audit Log

---

## 🧠 Decision Logic

### 1️⃣ Hard Rules
- Expired notification → NEVER
- Duplicate detected → NEVER

### 2️⃣ Priority Scoring
- System alerts → +50
- High priority hint → +20
- High recent frequency → -30 (fatigue penalty)

### 3️⃣ Final Classification
- Score ≥ 70 → NOW
- 40 ≤ Score < 70 → LATER
- Score < 40 → NEVER

---

## 🚫 Duplicate Handling
- Hash-based duplicate detection using MD5
- In-memory tracking of recent notifications

---

## 🔕 Alert Fatigue Strategy
- User notification count tracking
- Fatigue penalty applied after 5 notifications

---

## 🛠 Fallback Strategy
- If AI or advanced services fail, rule-based scoring ensures system stability
- Critical alerts always prioritized

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python app.py
