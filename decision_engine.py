import time
import hashlib


class NotificationEngine:

    def __init__(self):
        self.user_history = {}
        self.recent_hashes = set()

    def generate_hash(self, event):
        raw = event["user_id"] + event["event_type"] + event.get("message", "")
        return hashlib.md5(raw.encode()).hexdigest()

    def classify(self, event):

        user_id = event["user_id"]
        score = 0

        # Expiry check
        if event.get("expires_at") and event["expires_at"] < time.time():
            return "NEVER", "Notification expired"

        # Duplicate check
        event_hash = self.generate_hash(event)
        if event_hash in self.recent_hashes:
            return "NEVER", "Duplicate notification detected"

        self.recent_hashes.add(event_hash)

        # Priority scoring
        if event["event_type"] == "system_alert":
            score += 50

        if event.get("priority_hint") == "high":
            score += 20

        # Fatigue logic
        history = self.user_history.get(user_id, {"count": 0})

        if history["count"] >= 5:
            score -= 30

        # Final classification
        if score >= 70:
            decision = "NOW"
        elif score >= 40:
            decision = "LATER"
        else:
            decision = "NEVER"

        # Update history
        self.user_history[user_id] = {
            "count": history["count"] + 1
        }

        explanation = f"Score: {score}, Previous count: {history['count']}"
        return decision, explanation