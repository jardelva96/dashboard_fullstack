# **Fullstack Dashboard with Python** 🚀

Welcome to my **interactive dashboard** project! This is a demonstration of my skills in fullstack development using **Python** and modern technologies like **FastAPI**, **Streamlit**, and **PostgreSQL**. I designed this project as part of my portfolio to highlight my expertise in backend and frontend development, containerization, and database integration.

---

## **📌 Technologies I Used**
- **Language**: Python (3.9+).
- **Backend**: FastAPI - A lightweight and efficient framework for building REST APIs.
- **Frontend**: Streamlit - A Python library for creating interactive dashboards.
- **Database**: PostgreSQL - A relational database for storing and managing data.
- **Containers**: Docker and Docker Compose - For orchestrating the backend, frontend, and database.
- **Version Control**: Git and GitHub - For managing and collaborating on the project.

---

## **⚙️ Features I Built**
- **Dynamic Data Entry**: I created a user-friendly interface to add data to the database.
- **Interactive Visualizations**: I implemented dynamic charts (bar charts, line charts, etc.) using data from PostgreSQL.
- **Fullstack Architecture**:
  - A backend API built with FastAPI to handle data and integrations.
  - A frontend dashboard built with Streamlit for visualization and interaction.
- **Scalable Design**: The project is modular and ready for future enhancements.

---

## **📂 Project Structure**

```plaintext
dashboard_fullstack/
├── backend/                    # Backend built with FastAPI
│   ├── app/
│   │   ├── __init__.py         # Python package initializer
│   │   ├── main.py             # Entry point for the API
│   │   ├── models.py           # SQLAlchemy models
│   │   ├── database.py         # Database connection logic
│   │   ├── services.py         # Business logic for handling data
│   │   └── routers/            # Organized routes
│   │       ├── __init__.py
│   │       └── charts.py       # Endpoints for chart-related data
│   ├── Dockerfile              # Docker configuration for the backend
│   └── requirements.txt        # Backend dependencies
├── frontend/                   # Frontend built with Streamlit
│   ├── dashboard.py            # Interactive dashboard interface
│   ├── Dockerfile              # Docker configuration for the frontend
│   └── requirements.txt        # Frontend dependencies
├── docker-compose.yml          # Container orchestration with Docker Compose
└── README.md                   # Project documentation
