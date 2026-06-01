# PhishNet: Phishing Awareness Analysis System

PhishNet is a Capstone II project developed at Florida International University for **CIS 4951: Capstone II**. The project focuses on measuring and visualizing the effectiveness of phishing awareness training using simulated phishing data in an ethical and controlled environment.

The system uses a **FastAPI backend** to process phishing simulation data and a **web-based dashboard** to display key awareness metrics such as total users, phishing failure rate, reporting rate, and differences between trained and untrained users.

---

## Project Overview

Phishing remains one of the most common cybersecurity threats because it targets human behavior rather than only technical vulnerabilities. Even with technical defenses such as firewalls, spam filters, and intrusion detection systems, users can still be tricked into clicking malicious links or failing to report suspicious messages.

PhishNet addresses this issue by providing a structured way to analyze phishing awareness outcomes. The project compares user behavior across training groups and visualizes the results through an interactive dashboard.

The main goals of the project are to:

- Analyze phishing susceptibility using simulated user behavior data
- Compare trained and untrained users
- Calculate phishing awareness metrics dynamically
- Display results through a simple dashboard
- Support cybersecurity education through ethical simulation and visualization

---

## Features

- FastAPI backend for processing phishing simulation data
- REST API endpoint for dashboard metrics
- CSV-based simulated phishing dataset
- Training status filtering for trained and untrained users
- Dashboard cards for total users, failure rate, and reporting rate
- Bar chart comparing trained and untrained failure rates
- Frontend built with HTML, CSS, JavaScript, and Chart.js
- CORS enabled so the frontend can connect to the backend locally

---

## Tech Stack

**Backend**

- Python
- FastAPI
- Uvicorn
- CSV data processing

**Frontend**

- HTML
- CSS
- JavaScript
- Chart.js

**Project Deliverables**

- Final report
- Presentation slides
- Research poster
- Backend prototype
- Frontend dashboard prototype

---

## Repository Structure

```text
Capstone-II-Project/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── data/
│       └── phishing_data.csv
│
├── frontend/
│   └── dashboard.html
│
├── docs/
│   ├── PhishNet Report.pdf
│   ├── PhishNet Slides.pdf
│   └── Phishnet Poster Final Version.pdf
│
└── README.md
```

---

## How to Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/xGrimReyes/Capstone-II-Project.git
cd Capstone-II-Project
```

### 2. Start the backend

Go into the backend folder:

```bash
cd backend
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
python -m uvicorn app:app --reload --port 5000
```

The backend should now be running at:

```text
http://127.0.0.1:5000
```

### 3. Start the frontend dashboard

Open a new terminal window and go into the frontend folder:

```bash
cd frontend
```

Start a simple local web server:

```bash
python -m http.server 5500
```

Open the dashboard in your browser:

```text
http://127.0.0.1:5500/dashboard.html
```

---

## API Endpoints

### Health Check

```http
GET /api/health
```

Example response:

```json
{
  "status": "ok"
}
```

### Dashboard Metrics

```http
GET /api/dashboard
```

Example response:

```json
{
  "summary_metrics": {
    "total_users": 6,
    "failure_rate": 50.0,
    "reporting_rate": 50.0
  }
}
```

### Filter by Training Status

```http
GET /api/dashboard?training_status=Trained
GET /api/dashboard?training_status=Untrained
```

The dashboard uses these filters to compare trained and untrained users.

---

## Dataset

The backend reads phishing simulation records from:

```text
backend/data/phishing_data.csv
```

The dataset includes fields such as:

- `record_id`
- `user_id`
- `training_status`
- `link_clicked`
- `phishing_reported`

These fields are used to calculate:

- **Total users:** number of records in the selected dataset
- **Failure rate:** percentage of users who clicked the phishing link
- **Reporting rate:** percentage of users who reported the phishing attempt

The included CSV is a small sample dataset for demonstrating the prototype. The project report and presentation discuss the broader evaluation approach using simulated phishing awareness results.

---

## Evaluation Summary

PhishNet evaluates phishing awareness by comparing trained and untrained user groups. The project focuses on two main metrics:

- **Failure rate:** how often users fall for a phishing attempt
- **Reporting rate:** how often users correctly report phishing activity

The evaluation shows that trained users are less likely to fail phishing attempts and more likely to report suspicious activity. This supports the idea that phishing awareness training can reduce user susceptibility when combined with clear measurement and visualization.

The project should be interpreted as an educational and analytical prototype rather than a real-world phishing campaign. No real phishing emails were sent, and the system uses simulated data for ethical academic evaluation.

---

## My Role: Research and Evaluation

My role in this project was **Member C: Research and Evaluation**.

My responsibilities included:

- Researching phishing awareness, phishing susceptibility, and user-focused cybersecurity defenses
- Supporting the background, motivation, evaluation, and related work sections
- Evaluating the effectiveness of phishing awareness training using simulated results
- Analyzing metrics such as failure rate and reporting rate
- Interpreting differences between trained and untrained user groups
- Helping communicate findings in the final report, slides, and poster

---

## Team Members

- Samuel Castellanos
- Devin Giles
- Carlos Rey
- Ahsan Sanders

---

## Course Information

- **Course:** CIS 4951: Capstone II
- **Institution:** Florida International University
- **Professor:** Prof. Masoud Sadjadi
- **Date:** April 15, 2026

---

## Future Improvements

Potential improvements for future versions include:

- Expanding the dataset with more simulated users
- Adding a real email simulation environment
- Improving dashboard visuals and analytics
- Adding user authentication
- Deploying the system online
- Adding more detailed reporting and trend analysis
- Incorporating additional phishing difficulty factors based on research frameworks such as the NIST Phish Scale

---

## Ethical Considerations

PhishNet uses simulated phishing data instead of targeting real users with real phishing campaigns. This keeps the project ethical, controlled, reproducible, and appropriate for an academic environment.

---

## Conclusion

PhishNet demonstrates how phishing awareness data can be processed, evaluated, and visualized to better understand user susceptibility. By combining simulated data, backend processing, and dashboard visualization, the project highlights the importance of user education as part of a broader cybersecurity defense strategy.
