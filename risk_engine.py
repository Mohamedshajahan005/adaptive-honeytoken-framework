from config import AUTHORIZED_USERS

def calculate_risk(username, access_time, filename):
    risk_score = 0

    if username not in AUTHORIZED_USERS:
        risk_score += 50

    if "confidential" in filename.lower():
        risk_score += 30

    if access_time.hour < 6 or access_time.hour > 22:
        risk_score += 20

    return min(risk_score, 100)
