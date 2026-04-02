# 📂 Gossip Project - Complete File Structure

```
gossip_project/
│
├── 📁 gossip_env/                                    [Virtual Environment]
│   ├── Scripts/
│   │   ├── activate.bat                             # Activate for CMD
│   │   ├── Activate.ps1                             # Activate for PowerShell ⭐
│   │   ├── python.exe                               # Python executable
│   │   └── pip.exe                                  # Pip executable
│   ├── Lib/
│   │   └── site-packages/                           # Installed packages
│   │       ├── django/                              # Django 6.0.3
│   │       ├── rest_framework/                      # DRF 3.17.1
│   │       └── rest_framework_simplejwt/            # SimpleJWT 5.5.1
│   └── include/
│
├── 📁 gossip_project/                                [Main Project Folder] ⭐
│   │
│   ├── 📁 gossip_project_core/                       [Django Settings Package]
│   │   ├── __init__.py                              # Makes this a Python package
│   │   ├── settings.py                              # ⚙️ DJANGO CONFIGURATION
│   │   │   ├── INSTALLED_APPS configuration
│   │   │   ├── REST_FRAMEWORK settings
│   │   │   ├── SIMPLE_JWT configuration
│   │   │   ├── Database settings (SQLite)
│   │   │   └── Security settings
│   │   │
│   │   ├── urls.py                                  # 🔗 MAIN URL ROUTING
│   │   │   ├── /admin/ → Admin panel
│   │   │   ├── /api/token/ → JWT obtain endpoint
│   │   │   ├── /api/token/refresh/ → JWT refresh endpoint
│   │   │   └── /api/gossip/ → Gossip app URLs
│   │   │
│   │   ├── wsgi.py                                  # WSGI application (for deployment)
│   │   └── asgi.py                                  # ASGI application (for async)
│   │
│   ├── 📁 gossip/                                    [💅 GOSSIP APP]
│   │   ├── migrations/                              # Database migrations
│   │   │   ├── 0001_initial.py                      # Initial migration (Gossip model)
│   │   │   └── __init__.py
│   │   │
│   │   ├── __init__.py                              # Python package marker
│   │   │
│   │   ├── models.py                                # 📰 DATA MODEL
│   │   │   └── Gossip class
│   │   │       ├── title (CharField, max 200)
│   │   │       ├── content (TextField)
│   │   │       ├── posted_by (ForeignKey to User)
│   │   │       └── created_at (DateTimeField, auto)
│   │   │
│   │   ├── views.py                                 # 👀 API VIEWS
│   │   │   ├── GossipListAPIView (GET)
│   │   │   │   └── Lists all gossip (authenticated)
│   │   │   └── GossipCreateAPIView (POST)
│   │   │       └── Creates new gossip (authenticated)
│   │   │
│   │   ├── serializers.py                           # 📦 DATA SERIALIZATION
│   │   │   └── GossipSerializer
│   │   │       ├── Converts model ↔ JSON
│   │   │       ├── Read-only posted_by
│   │   │       └── Read-only created_at
│   │   │
│   │   ├── urls.py                                  # 🗺️ APP URL PATTERNS
│   │   │   ├── '' → GossipListAPIView
│   │   │   └── 'new/' → GossipCreateAPIView
│   │   │
│   │   ├── admin.py                                 # 🎛️ ADMIN PANEL CONFIG
│   │   │   └── GossipAdmin class
│   │   │       ├── list_display
│   │   │       ├── list_filter
│   │   │       ├── search_fields
│   │   │       └── ordering
│   │   │
│   │   ├── apps.py                                  # App configuration
│   │   ├── tests.py                                 # Unit tests (empty)
│   │   └── models.py, views.py, etc.
│   │
│   ├── manage.py                                    # 🔧 Django Management Script
│   │   ├── makemigrations
│   │   ├── migrate
│   │   ├── runserver
│   │   ├── createsuperuser
│   │   └── Other Django commands
│   │
│   ├── db.sqlite3                                   # 💾 SQLite Database
│   │   ├── auth_user table
│   │   ├── gossip_gossip table
│   │   ├── django_session table
│   │   └── Other Django tables
│   │
│   ├── set_password.py                              # 🔐 Password Setup Script
│   │   └── Sets superuser password to 'PlasticsRule2024!'
│   │
│   ├── setup.ps1                                    # 🚀 Automated Setup Script
│   │   └── Runs entire setup from scratch
│   │
│   ├── requirements.txt                             # 📋 Python Dependencies
│   │   ├── django==6.0.3
│   │   ├── djangorestframework==3.17.1
│   │   └── djangorestframework-simplejwt==5.5.1
│   │
│   ├── README.md                                    # 📖 Main Documentation (474 lines)
│   │   ├── Project overview
│   │   ├── Installation instructions
│   │   ├── API endpoint documentation
│   │   ├── Postman tutorial
│   │   ├── cURL examples
│   │   ├── Troubleshooting guide
│   │   └── Learning resources
│   │
│   ├── QUICKSTART.md                                # ⚡ Quick Reference Guide
│   │   ├── Server status
│   │   ├── Login credentials
│   │   ├── API endpoints summary
│   │   └── Postman quick test
│   │
│   ├── PROJECT_SUMMARY.md                           # 📊 Complete Summary
│   │   ├── What's been created
│   │   ├── How to use the API
│   │   ├── Technology stack
│   │   └── Next steps
│   │
│   └── FILE_STRUCTURE.md                            # 🗂️ This file!
│
└── 📄 Additional Files (in gossip_project_core/)
    ├── __pycache__/                                 # Python bytecode cache
    └── ...
```

---

## 🎯 Key Files Explained

### Configuration Files

#### `settings.py` ⭐
**What it does:** Controls all Django settings
**Key sections:**
- `INSTALLED_APPS` - Lists all installed apps
- `REST_FRAMEWORK` - DRF configuration
- `SIMPLE_JWT` - JWT token settings
- `DATABASES` - Database configuration

#### `urls.py` (project) ⭐
**What it does:** Routes URLs to views
**Endpoints:**
- `/admin/` - Admin panel
- `/api/token/` - Get JWT token
- `/api/token/refresh/` - Refresh token
- `/api/gossip/` - Gossip endpoints

---

### Gossip App Files

#### `models.py` ⭐
**What it does:** Defines database structure
**Model:** `Gossip`
- `title` - Headline (max 200 chars)
- `content` - Full story (text)
- `posted_by` - Who posted it (User FK)
- `created_at` - When posted (auto)

#### `views.py` ⭐
**What it does:** Handles HTTP requests
**Classes:**
- `GossipListAPIView` - GET all gossip
- `GossipCreateAPIView` - POST new gossip

#### `serializers.py` ⭐
**What it does:** Converts between Python and JSON
**Class:** `GossipSerializer`
- Serializes Gossip model to JSON
- Makes some fields read-only

#### `urls.py` (app) ⭐
**What it does:** Maps URLs to views for gossip app
**Patterns:**
- `''` → List gossip
- `'new/'` → Create gossip

---

### Helper Files

#### `manage.py` ⭐
**What it does:** Command-line utility for Django
**Commands:**
- `python manage.py runserver` - Start server
- `python manage.py makemigrations` - Create migrations
- `python manage.py migrate` - Apply migrations
- `python manage.py createsuperuser` - Create admin user

#### `set_password.py`
**What it does:** Sets superuser password programmatically

#### `setup.ps1`
**What it does:** Automates entire setup process

---

### Documentation Files

#### `README.md` ⭐
**Read this for:** Complete guide to the project
**Contains:** Installation, API docs, tutorials, troubleshooting

#### `QUICKSTART.md` ⭐
**Read this for:** Quick reference
**Contains:** Credentials, endpoints, quick Postman guide

#### `PROJECT_SUMMARY.md`
**Read this for:** Overview of what was created
**Contains:** Project statistics, features, next steps

---

## 🔄 Request Flow Diagram

```
Client Request (Postman/Browser/App)
        ↓
┌─────────────────────────────────────┐
│  Django Server (runserver)          │
│                                     │
│  1. urls.py (project)               │
│     /api/token/ → TokenObtainPair   │
│     /api/token/refresh/ → Refresh   │
│     /api/gossip/ → gossip.urls      │
│                                     │
│  2. gossip/urls.py                  │
│     GET / → GossipListAPIView       │
│     POST /new/ → GossipCreateAPIView│
│                                     │
│  3. views.py                        │
│     Check JWT token                 │
│     Verify authentication           │
│     Process request                 │
│                                     │
│  4. models.py                       │
│     Query database                  │
│     Gossip.objects.all()            │
│     or                              │
│     Gossip.objects.create()         │
│                                     │
│  5. serializers.py                  │
│     Convert to/from JSON            │
│                                     │
│  6. Return Response                 │
│     JSON data back to client        │
└─────────────────────────────────────┘
        ↓
Client receives response
```

---

## 📊 Database Schema

```
┌─────────────────────────────────────┐
│  auth_user (Django's built-in)      │
├─────────────────────────────────────┤
│  - id (PK)                          │
│  - username                         │
│  - password (hashed)                │
│  - email                            │
│  - first_name                       │
│  - last_name                        │
│  - is_staff (can access admin)      │
│  - is_superuser (full access)       │
│  - date_joined                      │
│  - last_login                       │
└─────────────────────────────────────┘
              ↓ (ForeignKey)
              ↓ posted_by
┌─────────────────────────────────────┐
│  gossip_gossip                       │
├─────────────────────────────────────┤
│  - id (PK)                          │
│  - title (VARCHAR 200)              │
│  - content (TEXT)                   │
│  - posted_by_id (FK → auth_user.id) │
│  - created_at (DATETIME)            │
└─────────────────────────────────────┘
```

---

## 🎨 Authentication Flow

```
┌─────────────────────────────────────────────┐
│  Step 1: Client sends credentials           │
│  POST /api/token/                           │
│  {                                          │
│    "username": "QueenBee",                  │
│    "password": "PlasticsRule2024!"          │
│  }                                          │
└─────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────┐
│  Step 2: Server validates & returns tokens  │
│  {                                          │
│    "access": "eyJhbGci...",  (5 min)        │
│    "refresh": "eyJhbGci..." (1 day)         │
│  }                                          │
└─────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────┐
│  Step 3: Client uses access token           │
│  GET /api/gossip/                           │
│  Header: Authorization: Bearer eyJhbGci...  │
└─────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────┐
│  Step 4: Server verifies token & responds   │
│  [                                          │
│    {                                        │
│      "id": 1,                               │
│      "title": "Regina Got Dumped!",         │
│      ...                                    │
│    }                                        │
│  ]                                          │
└─────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────┐
│  Step 5: When access token expires (5 min)  │
│  POST /api/token/refresh/                   │
│  {                                          │
│    "refresh": "eyJhbGci..."                 │
│  }                                          │
│                                              │
│  Returns: New access token                  │
└─────────────────────────────────────────────┘
```

---

## 🎯 Quick Reference

### URLs You Need to Know

| URL | Purpose | Auth Required? |
|-----|---------|----------------|
| `http://127.0.0.1:8000/admin/` | Admin panel | Yes (Django session) |
| `http://127.0.0.1:8000/api/token/` | Get JWT token | No |
| `http://127.0.0.1:8000/api/token/refresh/` | Refresh JWT | No |
| `http://127.0.0.1:8000/api/gossip/` | List gossip | Yes (JWT) |
| `http://127.0.0.1:8000/api/gossip/new/` | Create gossip | Yes (JWT) |

### HTTP Methods

- `GET` - Retrieve data
- `POST` - Create new data
- `PUT` - Update existing data (not implemented)
- `DELETE` - Delete data (not implemented)

### Status Codes

- `200 OK` - Successful GET request
- `201 Created` - Successful POST (creation)
- `400 Bad Request` - Invalid data
- `401 Unauthorized` - Missing or invalid token
- `403 Forbidden` - Valid token but no permission
- `404 Not Found` - Resource doesn't exist
- `500 Internal Server Error` - Server error

---

**This structure keeps everything organized and easy to navigate! 🎉**
