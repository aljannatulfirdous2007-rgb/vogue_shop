# 💅 Gossip Project - Mean Girls Themed Django REST API

Welcome to the **Gossip Project** - where all the tea is spilled! ☕ This is a fun, beginner-friendly Django REST Framework project with JWT authentication, inspired by Mean Girls and luxury gossip culture.

## 🎭 Project Overview

This project demonstrates how to build a complete REST API with:
- ✅ **JWT Authentication** - Secure token-based auth (like VIP wristbands!)
- ✅ **Protected Endpoints** - Only authenticated users can access the gossip
- ✅ **CRUD Operations** - Create and list gossip posts
- ✅ **Django Admin** - Manage your gossip through the admin panel
- ✅ **Beginner-Friendly Code** - Extensive comments explaining everything

---

## 📁 Project Structure

```
gossip_project/
├── gossip_env/                      # Python virtual environment
├── gossip_project/                  # Main project folder
│   ├── gossip_project_core/         # Django settings & configuration
│   │   ├── settings.py              # ⚙️ App configurations & JWT settings
│   │   ├── urls.py                  # 🔗 Main URL routing
│   │   ├── wsgi.py                  # WSGI application
│   │   └── asgi.py                  # ASGI application
│   ├── gossip/                      # 💅 Our Gossip App
│   │   ├── models.py                # 📰 Gossip model definition
│   │   ├── views.py                 # 👀 APIView classes
│   │   ├── serializers.py           # 📦 Data serialization
│   │   ├── urls.py                  # 🗺️ App URL patterns
│   │   ├── admin.py                 # 🎛️ Admin panel configuration
│   │   └── migrations/              # Database migrations
│   ├── manage.py                    # Django management script
│   ├── set_password.py              # Script to set superuser password
│   └── db.sqlite3                   # SQLite database
```

---

## 🚀 Quick Start Guide

### Step 1: Activate Virtual Environment

**PowerShell (Windows):**
```powershell
cd "c:\Users\Al jannatul firdous\gossip_env"
.\Scripts\Activate.ps1
```

**Command Prompt (Windows):**
```cmd
cd c:\Users\Al jannatul firdous\gossip_env
Scripts\activate.bat
```

**Mac/Linux:**
```bash
cd /path/to/gossip_env
source bin/activate
```

### Step 2: Navigate to Project
```powershell
cd "c:\Users\Al jannatul firdous\my_unique_django_project\gossip_project"
```

### Step 3: Run the Server
```powershell
python manage.py runserver
```

Your API is now live at: **http://127.0.0.1:8000/** 🎉

---

## 🔐 Superuser Credentials

Access the Django admin panel at: **http://127.0.0.1:8000/admin/**

**Login Details:**
- **Username:** `QueenBee`
- **Password:** `PlasticsRule2024!`
- **Email:** `queenbee@plastics.com`

⚠️ **Important:** Change this password in production!

---

## 📡 API Endpoints

### 🔐 Authentication Endpoints

#### 1. **Obtain JWT Token** - POST `/api/token/`
Get your VIP pass to the party! This gives you an access token.

**Request:**
```json
POST /api/token/
Content-Type: application/json

{
    "username": "QueenBee",
    "password": "PlasticsRule2024!"
}
```

**Response:**
```json
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**What these tokens do:**
- `access` token: Your VIP wristband! Lasts 5 minutes. Use this to access protected endpoints.
- `refresh` token: Extend your VIP status! Lasts 1 day. Use this to get new access tokens.

---

#### 2. **Refresh JWT Token** - POST `/api/token/refresh/`
Your access token expired? No problem! Get a new one without logging in again.

**Request:**
```json
POST /api/token/refresh/
Content-Type: application/json

{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Response:**
```json
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

### 💅 Gossip Endpoints (Protected)

**All gossip endpoints require JWT authentication!** You need to include your access token in the Authorization header.

**Header Format:**
```
Authorization: Bearer <your_access_token>
```

---

#### 3. **List All Gossip** - GET `/api/gossip/`
See ALL the tea! Get a list of all gossip posts (newest first).

**Request:**
```
GET /api/gossip/
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Response:**
```json
[
    {
        "id": 1,
        "title": "Regina Got Dumped!",
        "content": "She just found out her boyfriend has been cheating on her with...",
        "posted_by": "QueenBee",
        "created_at": "2024-03-30T18:45:00Z"
    },
    {
        "id": 2,
        "title": "New Girl Transfers Here!",
        "content": "Some girl from Michigan just enrolled at our school...",
        "posted_by": "QueenBee",
        "created_at": "2024-03-30T17:30:00Z"
    }
]
```

---

#### 4. **Create New Gossip** - POST `/api/gossip/new/`
Time to spill some fresh tea! Create a new gossip post.

**Request:**
```json
POST /api/gossip/new/
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
    "title": "Karen Joined the Math Team!",
    "content": "She said she wants to improve her grades, but we all know she just wants to be closer to Jason!"
}
```

**Response (201 Created):**
```json
{
    "id": 3,
    "title": "Karen Joined the Math Team!",
    "content": "She said she wants to improve her grades, but we all know she just wants to be closer to Jason!",
    "posted_by": "QueenBee",
    "created_at": "2024-03-30T19:15:00Z"
}
```

**Response (400 Bad Request - if validation fails):**
```json
{
    "title": ["This field is required."],
    "content": ["Ensure this field has at least 1 character."]
}
```

---

## 📮 Postman Instructions

### Setting Up Postman

#### Step 1: Get Your JWT Token

1. Open Postman
2. Create a new **POST** request
3. URL: `http://127.0.0.1:8000/api/token/`
4. Go to the **Body** tab
5. Select **raw** and choose **JSON** from dropdown
6. Enter:
```json
{
    "username": "QueenBee",
    "password": "PlasticsRule2024!"
}
```
7. Click **Send**
8. Copy the `access` token from the response

---

#### Step 2: Set Up Authorization Header

For all gossip endpoints:

1. Create your request (GET or POST)
2. Go to the **Authorization** tab
3. Type: **Bearer Token**
4. Paste your access token in the **Token** field

OR manually add header:
- Key: `Authorization`
- Value: `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...`

---

#### Step 3: Test the Endpoints

**Test 1: List All Gossip**
- Method: `GET`
- URL: `http://127.0.0.1:8000/api/gossip/`
- Add Authorization header
- Click Send
- You should see a list of gossip posts!

**Test 2: Create New Gossip**
- Method: `POST`
- URL: `http://127.0.0.1:8000/api/gossip/new/`
- Add Authorization header
- Body (raw JSON):
```json
{
    "title": "Your spicy headline here!",
    "content": "Spill ALL the tea! Every delicious detail..."
}
```
- Click Send
- Success! Your gossip is now in the database! 🎉

---

## 🧪 Example cURL Commands

Prefer command line? Here are some cURL examples:

### Get JWT Token
```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"QueenBee\",\"password\":\"PlasticsRule2024!\"}"
```

### List All Gossip
```bash
curl -X GET http://127.0.0.1:8000/api/gossip/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN_HERE"
```

### Create New Gossip
```bash
curl -X POST http://127.0.0.1:8000/api/gossip/new/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d "{\"title\":\"Spicy Headline!\",\"content\":\"All the juicy details...\"}"
```

---

## 🗄️ Database Models

### Gossip Model

```python
class Gossip(models.Model):
    title = models.CharField(max_length=200)       # 📰 Catchy headline
    content = models.TextField()                    # 📝 Full story
    posted_by = models.ForeignKey(User, ...)        # 👤 Who spilled it
    created_at = models.DateTimeField(auto_now_add=True)  # ⏰ When posted
```

---

## 🛠️ Development Commands

### Make Migrations (after model changes)
```powershell
python manage.py makemigrations
```

### Apply Migrations
```powershell
python manage.py migrate
```

### Create Superuser
```powershell
python manage.py createsuperuser
```

### Run Development Server
```powershell
python manage.py runserver
```

### Run Tests
```powershell
python manage.py test
```

---

## 🎨 Customization Ideas

Want to make it even more fetch? Try:

1. **Add Ratings** - Let users rate gossip from 1-5 stars ⭐
2. **Add Comments** - Let people comment on gossip posts 💬
3. **Add Categories** - Organize gossip by type (Relationships, Fashion, Drama) 🏷️
4. **Add Images** - Upload screenshots to go with the tea 📸
5. **Add Likes** - Let users like their favorite gossip 👍
6. **Add User Profiles** - Customize user profiles with avatars and bios 👤

---

## 🔒 Security Notes

### For Development:
- ✅ DEBUG = True (shows detailed error pages)
- ✅ Simple password for testing
- ✅ SQLite database (file-based)

### For Production:
- ❌ Set DEBUG = False
- ❌ Use strong passwords
- ❌ Use environment variables for SECRET_KEY
- ❌ Switch to PostgreSQL or MySQL
- ❌ Enable HTTPS
- ❌ Use proper CORS settings
- ❌ Implement rate limiting

---

## 📚 Technologies Used

- **Python 3.x** - Programming language
- **Django 6.0.3** - Web framework
- **Django REST Framework 3.17.1** - API framework
- **djangorestframework-simplejwt 5.5.1** - JWT authentication
- **SQLite** - Database (development)

---

## 🆘 Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'django'"
**Solution:** Activate your virtual environment first!
```powershell
cd "c:\Users\Al jannatul firdous\gossip_env"
.\Scripts\Activate.ps1
```

### Problem: "Permission denied" when activating venv (PowerShell)
**Solution:** Change execution policy:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Problem: Token expired after 5 minutes
**Solution:** That's normal! Use the refresh endpoint to get a new access token:
```
POST /api/token/refresh/
{
    "refresh": "your_refresh_token"
}
```

### Problem: 401 Unauthorized on gossip endpoints
**Solution:** Make sure you're including the Authorization header with a valid token:
```
Authorization: Bearer your_access_token
```

---

## 📖 Learning Resources

### Django REST Framework:
- Official Docs: https://www.django-rest-framework.org/
- Tutorial: https://www.django-rest-framework.org/tutorial/quickstart/

### JWT Authentication:
- SimpleJWT Docs: https://django-rest-framework-simplejwt.readthedocs.io/
- What is JWT?: https://jwt.io/introduction

### Django Best Practices:
- Two Scoops of Django (book)
- Django Styleguide: https://github.com/HackSoftware/Django-Styleguide

---

## 🎯 Next Steps

Now that you've built this API, try:

1. ✨ Build a frontend with React/Vue to display the gossip
2. 📱 Create a mobile app using the API
3. 🔐 Add user registration endpoint
4. 👥 Add user profile management
5. 🔍 Add search and filtering to gossip list
6. 📊 Add analytics (most popular gossip, etc.)

---

## 💖 Credits

Made with 💕 and lots of ☕ by following the Django REST Framework best practices.

**Remember:** In the game of gossip, you either win or you die... but in this API, everyone wins! 💅

---

## 📞 Need Help?

If you get stuck:
1. Check the Django docs
2. Google your error message
3. Ask on Stack Overflow
4. Remember: The Plastics always help each other! 💪

**Happy Coding! 🎉**
