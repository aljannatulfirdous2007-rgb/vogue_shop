# 🧪 Testing Your Gossip API

## ✅ Your API is LIVE and working!

Base URL: `http://127.0.0.1:8000/`

---

## 🔐 Step 1: Get Your JWT Token

### Using cURL (Command Line):
```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"firdous\",\"password\":\"firdous\"}"
```

### Using Python:
```python
import requests

response = requests.post('http://127.0.0.1:8000/api/token/', json={
    'username': 'firdous',
    'password': 'firdous'
})

token = response.json()['access']
print(f"Your token: {token}")
```

### Response:
```json
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Copy the `access` token!**

---

## 📰 Step 2: List All Gossip

### cURL:
```bash
curl -X GET http://127.0.0.1:8000/api/gossip/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN_HERE"
```

### Python:
```python
headers = {'Authorization': f'Bearer {token}'}
response = requests.get('http://127.0.0.1:8000/api/gossip/', headers=headers)
print(response.json())
```

---

## ✨ Step 3: Create New Gossip

### cURL:
```bash
curl -X POST http://127.0.0.1:8000/api/gossip/new/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d "{\"title\":\"My First Gossip!\",\"content\":\"This is so exciting!\"}"
```

### Python:
```python
response = requests.post(
    'http://127.0.0.1:8000/api/gossip/new/',
    headers=headers,
    json={
        'title': 'My First Gossip!',
        'content': 'This is so exciting!'
    }
)
print(response.json())
```

---

## 🎯 Quick Test Script

Save this as `test_api.py` and run it:

```python
import requests

# Step 1: Get token
print("🔐 Getting JWT token...")
response = requests.post('http://127.0.0.1:8000/api/token/', json={
    'username': 'firdous',
    'password': 'firdous'
})

if response.status_code == 200:
    token = response.json()['access']
    print(f"✅ Token received!\n")
    
    # Step 2: List gossip
    print("📰 Listing all gossip...")
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get('http://127.0.0.1:8000/api/gossip/', headers=headers)
    
    if response.status_code == 200:
        gossips = response.json()
        if gossips:
            print(f"✅ Found {len(gossips)} gossip post(s):\n")
            for gossip in gossips:
                print(f"📝 {gossip['title']}")
                print(f"   By: {gossip['posted_by']}")
                print(f"   At: {gossip['created_at']}\n")
        else:
            print("ℹ️ No gossip yet. Let's create one!\n")
            
            # Step 3: Create gossip
            print("✨ Creating new gossip...")
            response = requests.post(
                'http://127.0.0.1:8000/api/gossip/new/',
                headers=headers,
                json={
                    'title': 'Testing the API!',
                    'content': 'This is my first gossip post using the API!'
                }
            )
            
            if response.status_code == 201:
                print("✅ Gossip created successfully!")
                print(f"   Title: {response.json()['title']}")
                print(f"   Content: {response.json()['content']}")
            else:
                print(f"❌ Error: {response.json()}")
    else:
        print(f"❌ Error listing gossip: {response.status_code}")
else:
    print(f"❌ Error getting token: {response.status_code}")
```

Run it:
```bash
cd "c:\Users\Al jannatul firdous\gossip_env"
.\Scripts\Activate.ps1
cd "c:\Users\Al jannatul firdous\my_unique_django_project\gossip_project"
python test_api.py
```

---

## 🎨 Want a Visual Frontend?

If you want a proper website (not just admin panel), I can create:

1. **Homepage** - Shows all gossip in a nice feed
2. **Create Form** - Beautiful form to submit gossip
3. **Authentication** - Login/logout UI
4. **Mean Girls Theme** - Pink, luxury gossip vibe!

Just ask and I'll build it for you! 💅☕
