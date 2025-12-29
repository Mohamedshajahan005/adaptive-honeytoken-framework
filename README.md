# 🔐 Adaptive Honeytoken Framework for Enterprise File Security

## 📌 Overview
This project proposes an **Adaptive Honeytoken Framework** designed to enhance enterprise file security by embedding decoy files (honeytokens) and triggering **automated responses** when unauthorized access is detected.

The system dynamically evaluates risk based on user behavior, access time, and file sensitivity, enabling real-time incident response.

---

## 🎯 Key Features
- Honeytoken-based data breach detection
- Behavioral risk scoring engine
- Automated response (quarantine, alert, logging)
- Real-time monitoring dashboard (Tkinter GUI)
- Enterprise-focused file security model

---

## 🛠️ Technologies Used
- Python
- Tkinter (GUI)
- File System Monitoring
- Rule-based Risk Scoring
- CSV / Excel Honeytokens

---

## 🧠 System Architecture
1. Honeytoken Generation Layer  
2. Access Monitoring Layer  
3. Risk Evaluation Engine  
4. Automated Response Engine  
5. Logging & Alert Module  

---

## ⚙️ Automated Responses
| Risk Level | Action Taken |
|----------|-------------|
| Low | Log activity |
| Medium | Alert administrator |
| High | Quarantine file + block user |

---

## 🚀 How to Run
```bash
pip install -r requirements.txt
python gui_dashboard.py
