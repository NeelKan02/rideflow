# 🚗 RideFlow

> A smart car fleet & pooling management system with real-time tracking, auto ride assignment, and route optimization.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-In%20Development-yellow.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

---

## 📌 Overview

**RideFlow** is a full-stack car fleet and carpooling management platform designed for fleet operators, drivers, and riders. It enables managers to oversee their entire fleet in real time, while riders can request rides and get automatically assigned to the best available vehicle based on route, direction, and available seats.

---

## ✨ Features

### 👤 Multi-Role System
- **Manager/Operator** — Add and manage fleet, monitor live map, oversee all trips
- **Driver** — View assigned route, update trip status, see passenger list
- **Rider** — Request rides, set pickup/drop-off, track assigned vehicle in real time

### 🚘 Fleet Management
- Add, edit, and remove vehicles
- Assign drivers to vehicles
- Track vehicle availability and status

### 🤖 Smart Ride Assignment
- Riders submit pickup and destination
- System automatically finds cars with vacant seats heading in a similar direction
- Auto-assigns rider to the best-fit car
- Dynamically recalculates route to include new pickup points

### 📍 Real-Time Tracking
- Live GPS location of all vehicles on an interactive map
- Riders see ETA and live car location
- Manager dashboard with all vehicles on a live map

### 🛣️ Route & Time Optimization
- Optimized multi-stop routing
- ETA calculation per rider
- Dynamic re-routing when new riders are added

### 📊 Manager Dashboard
- Fleet status overview (active, idle, en-route)
- Rider status (waiting, picked up, dropped off)
- Trip history and analytics

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | React.js + Tailwind CSS |
| **Backend** | Python + FastAPI |
| **Database** | PostgreSQL + SQLAlchemy |
| **Real-time** | Socket.io |
| **Maps & Routing** | Leaflet.js + OpenRouteService |
| **Authentication** | Firebase Auth + JWT |
| **Hosting** | Vercel (Frontend) + Render (Backend) |

---

## 🗂️ Project Structure

```
rideflow/
├── frontend/                  # React.js frontend
│   ├── public/
│   └── src/
│       ├── components/        # Reusable UI components
│       ├── pages/             # Page-level components
│       ├── hooks/             # Custom React hooks
│       ├── context/           # Global state (Auth, Fleet, etc.)
│       ├── services/          # API call functions
│       └── utils/             # Helper functions
│
├── backend/                   # FastAPI backend
│   ├── app/
│   │   ├── api/               # API route handlers
│   │   ├── models/            # Database models (SQLAlchemy)
│   │   ├── schemas/           # Pydantic schemas
│   │   ├── services/          # Business logic
│   │   ├── core/              # Config, security, dependencies
│   │   └── main.py            # App entry point
│   ├── alembic/               # Database migrations
│   └── requirements.txt       # Python dependencies
│
├── docs/                      # Documentation & diagrams
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Node.js (v18+)
- Python (v3.10+)
- PostgreSQL
- Git

### 1. Clone the repository
```bash
git clone https://github.com/NeelKan02/rideflow.git
cd rideflow
```

### 2. Set up the Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env       # Add your environment variables
uvicorn app.main:app --reload
```

### 3. Set up the Frontend
```bash
cd frontend
npm install
cp .env.example .env       # Add your environment variables
npm run dev
```

### 4. Set up the Database
```bash
cd backend
alembic upgrade head
```

---

## 🗺️ Development Roadmap

- [x] Project setup & repository structure
- [ ] **Phase 1** — Authentication & User Roles (Manager, Driver, Rider)
- [ ] **Phase 2** — Fleet Management (Add/Edit/Remove Vehicles)
- [ ] **Phase 3** — Ride Request & Smart Auto-Assignment
- [ ] **Phase 4** — Maps & Route Display (Leaflet.js)
- [ ] **Phase 5** — Real-Time Tracking (Socket.io)
- [ ] **Phase 6** — Manager Dashboard & Analytics
- [ ] **Phase 7** — Mobile App (React Native)
- [ ] **Phase 8** — Deployment & Polish

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](https://github.com/NeelKan02/rideflow/issues).

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**NeelKan02**
- GitHub: [@NeelKan02](https://github.com/NeelKan02)

---

> 💡 *Built as a portfolio project to demonstrate full-stack development, real-time systems, and route optimization skills.*