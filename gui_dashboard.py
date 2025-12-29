import tkinter as tk
from tkinter import ttk
from behavior_profiler import extract_features
from ml_anomaly_detector import detect_anomaly
from risk_fusion_engine import calculate_risk
from automated_response import respond
import matplotlib.pyplot as plt

# Globals
attempt_count = {}
risk_history = []

def run_detection():
    username = entry_user.get()
    filename = entry_file.get()

    if not username or not filename:
        return

    # Track attempts
    attempt_count[username] = attempt_count.get(username, 0) + 1

    features = extract_features(username, filename)
    ml_score = detect_anomaly(features)

    rule_score = 0.7 if features["unknown_user"] else 0.2
    final_risk = calculate_risk(rule_score, ml_score)

    # AUTO ESCALATION AFTER 3 ATTEMPTS
    if attempt_count[username] >= 3:
        final_risk = max(final_risk, 0.85)

    action = respond(final_risk, filename, username)


    # Risk color coding
    if final_risk < 0.4:
        color = "green"
    elif final_risk < 0.7:
        color = "orange"
    else:
        color = "red"

    result_label.config(
        text=f"Risk Score: {final_risk}\nAction: {action}",
        fg=color
    )

    # Update table
    table.insert("", "end", values=(username, filename, final_risk, action))

    # Update risk history
    risk_history.append(final_risk)

def show_risk_graph():
    plt.figure()
    plt.plot(risk_history, marker="o")
    plt.title("Risk Trend Over Time")
    plt.xlabel("Access Attempt")
    plt.ylabel("Risk Score")
    plt.ylim(0, 1)
    plt.show()

# GUI Window
root = tk.Tk()
root.title("Adaptive Honeytoken Security Dashboard")
root.geometry("620x520")

tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Filename").pack()
entry_file = tk.Entry(root, width=40)
entry_file.insert(0, "honeytokens/finance_report.xlsx")
entry_file.pack()

tk.Button(root, text="Run Security Check", command=run_detection).pack(pady=5)
tk.Button(root, text="Show Risk Trend", command=show_risk_graph).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 11, "bold"))
result_label.pack(pady=10)

# Live Log Table
columns = ("User", "File", "Risk", "Action")
table = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    table.heading(col, text=col)

table.pack(expand=True, fill="both")



root.mainloop()

