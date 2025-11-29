import requests
import json
from typing import List, Dict
from pprint import pprint
from urllib.parse import urljoin

# Constants
BASE_URL = "https://api.example.com/"  # Replace with actual base in interview
API_KEY = "your_api_key_here"  # If needed

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# --- Reusable Utilities ---

def get(endpoint: str, params: Dict = {}) -> Dict:
    url = urljoin(BASE_URL, endpoint)
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()

def post(endpoint: str, data: Dict) -> Dict:
    url = urljoin(BASE_URL, endpoint)
    response = requests.post(url, headers=HEADERS, json=data)
    response.raise_for_status()
    return response.json()

def log(title: str, data: Dict):
    print(f"\n=== {title} ===")
    pprint(data)

# --- Example: Analyze Merchant Transactions ---

def fetch_all_merchants() -> List[Dict]:
    return get("merchants")["data"]  # assuming {"data": [...]}

def fetch_merchant_transactions(merchant_id: str) -> List[Dict]:
    return get(f"merchants/{merchant_id}/transactions")["transactions"]

def detect_suspicious_activity(transactions: List[Dict]) -> List[Dict]:
    flagged = []
    seen_ids = set()
    for tx in transactions:
        # Example rules: duplicate ID or amount > $10,000
        if tx["id"] in seen_ids or tx["amount"] > 10000:
            flagged.append(tx)
        seen_ids.add(tx["id"])
    return flagged

def run_analysis():
    merchants = fetch_all_merchants()
    for merchant in merchants:
        merchant_id = merchant["id"]
        txns = fetch_merchant_transactions(merchant_id)
        suspicious = detect_suspicious_activity(txns)
        if suspicious:
            log(f"Suspicious transactions for {merchant_id}", suspicious)

# --- Entry point ---
if __name__ == "__main__":
    run_analysis()
