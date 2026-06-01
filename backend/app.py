from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_data():
    with open("data/phishing_data.csv", newline='') as file:
        return list(csv.DictReader(file))

def filter_data(data, training_status=None):
    if training_status:
        data = [r for r in data if r["training_status"] == training_status]
    return data

def calculate_metrics(data):
    total = len(data)
    clicked = sum(1 for r in data if r["link_clicked"] == "Yes")
    reported = sum(1 for r in data if r["phishing_reported"] == "Yes")

    return {
        "total_users": total,
        "failure_rate": round((clicked / total) * 100, 2) if total else 0,
        "reporting_rate": round((reported / total) * 100, 2) if total else 0
    }

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.get("/api/dashboard")
def dashboard(training_status: str = Query(None)):
    data = load_data()
    data = filter_data(data, training_status)
    return {"summary_metrics": calculate_metrics(data)}