My backend runs on FastAPI.

To use it:
1. Go to backend folder
2. Run:
pip install fastapi uvicorn
python -m uvicorn app:app --reload --port 5000

Main API:
http://127.0.0.1:5000/api/dashboard

You can filter:
?training_status=Trained
?training_status=Untrained

It returns:
- total_users
- failure_rate
- reporting_rate

Frontend should use this to display charts and metrics.
