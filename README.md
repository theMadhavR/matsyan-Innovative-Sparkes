
# 🚀 SmartNavFish: AI-Powered Navigation for Sustainable Fishing  

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python" alt="Python"/>
  <img src="https://img.shields.io/badge/FastAPI-0.95-green?logo=fastapi" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/PostgreSQL-13+-blue?logo=postgresql" alt="PostgreSQL"/>
  <img src="https://img.shields.io/badge/MongoDB-5+-green?logo=mongodb" alt="MongoDB"/>
  <img src="https://img.shields.io/badge/Deployed-Vercel-black?logo=vercel" alt="Vercel"/>
</div>

---

## 🌊 Project Description  
**SmartNavFish** is an intelligent platform that empowers fishermen with AI-driven route optimization, real-time marine law alerts, and safety features. Our solution reduces fuel costs by 30% and increases catch efficiency — all while promoting sustainable fishing practices.

---

## ❓ Problem Statement  

| Traditional Fishing Challenges | Our Solution |
|-------------------------------|--------------|
| 🎣 40% of time wasted searching for fish | 🧠 AI-powered heatmaps and route optimization |
| ⛽ High fuel costs from inefficient routes | 🛣️ Fuel-efficient pathfinding algorithms |
| ⚖️ Unintentional violation of marine laws | 📢 Real-time regulatory boundary alerts |
| 🆘 No emergency systems at sea | 🚨 GPS-enabled SOS with automated distress signals |

---

## 🛠️ Tech Stack  

### Core Technologies  

<div align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/5968/5968350.png" width="60" title="Python"/>
  <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="120" title="FastAPI"/>
  <img src="https://www.postgresql.org/media/img/about/press/elephant.png" width="60" title="PostgreSQL"/>
  <img src="https://cdn.iconscout.com/icon/free/png-256/mongodb-5-1175140.png" width="60" title="MongoDB"/>
</div>

### Key Features Implementation  

| Feature | Technology Used |
|---------|-----------------|
| Real-time Maps | Mapbox GL JS + PostGIS |
| AI Predictions | Scikit-learn + TensorFlow Lite |
| Offline Mode | SQLite + Hive (Flutter) |
| SOS System | Twilio API + Firebase |
| Weather Data | OpenWeatherMap + World Tides API |
| Authentication | JWT + OAuth2 |

---

## ⚡ Installation & Setup  

### Prerequisites  

```bash
Python 3.9+
PostgreSQL 13+
MongoDB 5+
```

### 1. Clone Repository  

```bash
git clone https://github.com/matsyan-Innovative-Sparkes/smartnavfish.git
cd smartnavfish
```

### 2. Set Up Environment  

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies  

```bash
pip install -r requirements.txt
```

### 4. Configure Databases  

```bash
# PostgreSQL Setup
createdb SmartNavFish-Fishing Route Optimizer
psql -U postgres -d smartnavfish -c "CREATE EXTENSION postgis;"

# MongoDB Setup (ensure service is running)
```

### 5. Run Migrations  

```bash
alembic upgrade head
```

---

## 🏃 How to Run  

### Development Mode  

```bash
uvicorn app.main:app --reload
```

### Production Deployment  

```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
```

---

## 📸 Visual Showcase  

### Web Interface  
![Dashboard Preview](https://example.com/smartnavfish-demo.gif)  
*Real-time fishing heatmap with optimized routes*

---

## 🌐 Live Deployment  

🔗 [smartnavfish.vercel.app](https://smartnavfish.vercel.app)

---

## 🎥 Demo Video  

📺 [Watch on YouTube](https://youtube.com/smartnavfish-demo)

---

## 👥 Team Innovative Sparkes  

| Member | Role | Contribution |
|--------|------|--------------|
| Krishna N | DevOps Engineer | Cloud Deployment |
| Miracline Gladys J | UI/UX Expert | Flutter Mobile App |
| Karthika V | Data Scientist | ML Model Training |
| Madhav R | Team Lead | AI Architecture & Backend |

---

<div align="center">
  <h3>🚢 Helping Fishermen Navigate Smarter</h3>
</div>
