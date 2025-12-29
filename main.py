from behavior_profiler import extract_features
from ml_anomaly_detector import detect_anomaly, train_model
from risk_fusion_engine import calculate_risk
from automated_response import respond

def simulate(username, filename):
    features = extract_features(username, filename)
    ml_score = detect_anomaly(features)

    rule_score = 0.7 if features["unknown_user"] else 0.2
    final_risk = calculate_risk(rule_score, ml_score)

    action = respond(final_risk, filename, username)
    print("[SECURITY ACTION]:", action)

if __name__ == "__main__":
    train_model()
    simulate("attacker_user", "honeytokens/finance_report.xlsx")

