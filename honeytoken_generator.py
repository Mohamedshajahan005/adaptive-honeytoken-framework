import os
import uuid
import json

def create_honeytoken():
    os.makedirs("honeytokens", exist_ok=True)

    token_id = str(uuid.uuid4())
    filename = "finance_report.xlsx"

    metadata = {
        "token_id": token_id,
        "classification": "TOP_SECRET",
        "decoy": True
    }

    with open(f"honeytokens/{filename}", "w") as f:
        f.write("Sensitive Financial Data")

    with open(f"honeytokens/{filename}.meta", "w") as f:
        json.dump(metadata, f)

    print("[+] Advanced Honeytoken deployed")

if __name__ == "__main__":
    create_honeytoken()
