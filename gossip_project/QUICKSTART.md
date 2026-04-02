# 🚀 Quick Start - Gossip Project

## Server is Running! ✅

The API is live at: **http://127.0.0.1:8000/**

---

## 🔐 Login Credentials

**Admin Panel:** http://127.0.0.1:8000/admin/

- **Username:** `QueenBee`
- **Password:** `PlasticsRule2024!`

---

## 📡 API Endpoints Summary

### 1️⃣ Get JWT Token
```
POST /api/token/
Body: {"username": "QueenBee", "password": "PlasticsRule2024!"}
Response: {"access": "...", "refresh": "..."}
```

### 2️⃣ Refresh Token
```
POST /api/token/refresh/
Body: {"refresh": "your_refresh_token"}
Response: {"access": "new_access_token"}
```

### 3️⃣ List All Gossip (needs token)
```
GET /api/gossip/
Header: Authorization: Bearer your_access_token
```

### 4️⃣ Create Gossip (needs token)
```
POST /api/gossip/new/
Header: Authorization: Bearer your_access_token
Body: {"title": "Headline", "content": "The full story..."}
```

---

## 🎯 Postman Quick Test

### Step 1: Get Token
1. Method: POST
2. URL: `http://127.0.0.1:8000/api/token/`
3. Body → raw → JSON:
```json
{"username": "QueenBee", "password": "PlasticsRule2024!"}
```
4. Click Send
5. Copy the `access` token

### Step 2: Test Protected Endpoint
1. Method: GET
2. URL: `http://127.0.0.1:8000/api/gossip/`
3. Authorization tab → Type: Bearer Token
4. Paste access token
5. Click Send

### Step 3: Create Gossip
1. Method: POST
2. URL: `http://127.0.0.1:8000/api/gossip/new/`
3. Authorization: Bearer Token (paste token)
4. Body → raw → JSON:
```json
{
    "title": "My First Gossip!",
    "content": "This is the beginning of some spicy tea..."
}
```
5. Click Send

---

## 💡 Pro Tips

- Access tokens expire after **5 minutes** ⏰
- Use refresh token to get new access tokens without logging in again
- Always include the `Bearer` prefix in Authorization header
- Check Django admin at http://127.0.0.1:8000/admin/ to see your gossip in the database!

---

## 🆘 Common Issues

**401 Unauthorized?** → Check if token is expired or missing

**400 Bad Request?** → Make sure title and content are included in POST body

**Can't connect?** → Make sure server is running: `python manage.py runserver`

---

**You're ready to spill some tea! ☕💅**
