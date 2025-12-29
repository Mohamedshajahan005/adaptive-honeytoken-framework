import datetime
from config import RISK_THRESHOLDS, ALERT_FILE
import os

def automated_response(risk_score, username, filename):
    os.makedirs("alerts", exist_ok=True)

    if risk_score >= RISK_THRESHOLDS["HIGH"]:
        action = "BLOCK USER & ALERT ADMIN"
    elif risk_score >= RISK_THRESHOLDS["MEDIUM"]:
        action = "LOG & SEND WARNING"
    else:
        action = "MONITOR"

    with open(ALERT_FILE, "a") as f:
        f.write(f"{datetime.datetime.now()} | {username} | {filename} | {action}\n")

    print(f"[RESPONSE] Action taken: {action}")
