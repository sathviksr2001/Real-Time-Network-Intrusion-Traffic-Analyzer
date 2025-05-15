
# 📡 Real-Time Network Intrusion & Traffic Analyzer

An intelligent system that monitors live network traffic, detects suspicious patterns, and provides real-time anomaly detection using machine learning (Isolation Forest). This project combines the power of **packet sniffing**, **unsupervised anomaly detection**, and a **live dashboard interface** to visualize network behavior.

---

## 🚀 Features

- 📥 Captures real-time network packets using **Scapy**
- 🔎 Analyzes packet-level data including source IP, destination IP, and packet length
- 🧠 Detects anomalies using **Isolation Forest** (unsupervised ML)
- 📊 Displays live stats on a responsive **Flask web dashboard**
- 🛡️ Useful for identifying unusual activity, possible intrusions, and traffic spikes

---

## 🛠️ Tech Stack

| Layer              | Technology            |
|-------------------|-----------------------|
| Packet Capture     | `Scapy`               |
| Web Server         | `Flask`               |
| ML for Anomalies   | `Scikit-learn`        |
| Data Analysis      | `Pandas`              |
| Dashboard Frontend | HTML + JS             |
| Backend Threading  | `threading` module    |

---

## 📂 Project Structure

```
smart-network-analyzer/
│
├── app/
│   ├── __init__.py               # Flask app setup
│   ├── views.py                  # Routes and data API
│   ├── packet_sniffer.py         # Scapy-based packet sniffer
│   ├── detector.py               # ML-based anomaly detection
│   ├── templates/
│   │   └── dashboard.html        # Dashboard HTML template
│   └── static/                   # (Optional) CSS/JS files
│
├── run.py                        # Entry point to start Flask app
├── requirements.txt              # Project dependencies
├── README.md                     # This file
└── LICENSE                       # (Optional) License
```

---

## 📦 Installation

### 🔧 Prerequisites
- Python 3.7+
- Internet connection (for installing packages)

### 🐍 Setup
```bash
git clone https://github.com/yourusername/smart-network-analyzer.git
cd smart-network-analyzer

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Running the App

```bash
python run.py
```

Then open your browser and visit: [http://localhost:5000](http://localhost:5000)

> The app starts sniffing packets and detecting anomalies immediately.

---

## 📈 Live Dashboard Preview

The dashboard shows:
- ✅ Total packets captured
- 🚨 Number of detected anomalies

You can refresh it every second for live monitoring. Easy to expand with charts or graphs.
