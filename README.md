# Django Middleware Project

## 📋 Features

- ✅ Custom User Model with Email Login
- ✅ IP Logging Middleware (logs each request IP)
- ✅ Rate Limiting Middleware (based on user role)
- ✅ Role-based access (Gold/Silver/Bronze/Guest)
- ✅ Register/Login/Logout API
- ✅ Admin Panel Integration

---

## 🧱 User Roles & Limits

| Role           | Requests per minute |
|----------------|---------------------|
| Unauthenticated | 1                  |
| Bronze         | 2                   |
| Silver         | 5                   |
| Gold           | 10                  |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip
- virtualenv (recommended)

### Setup

```bash
git clone <repo-url>
cd myproject
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
