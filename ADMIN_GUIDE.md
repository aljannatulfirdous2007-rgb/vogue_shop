# 👑 VOGUE E-COMMERCE ADMIN PANEL GUIDE

## 🎯 **ACCESSING THE ADMIN PANEL**

### **URL:** http://127.0.0.1:8000/admin/

### **Login Credentials:**
```
Username: admin
Email: admin@vogueshop.com
Password: VogueAdmin2024!
```

---

## 📦 **WHAT YOU CAN MANAGE IN ADMIN**

### **1. PRODUCTS MANAGEMENT** 🛍️

#### **Categories:**
- Add/Edit/Delete product categories
- Create parent-child relationships (e.g., Bags → Shoulder Bags)
- Set category active/inactive status
- Auto-generate slugs from names

**How to add a category:**
1. Go to Products → Categories → ADD
2. Enter name (e.g., "Shoulder Bags")
3. Select parent category if applicable (e.g., "Bags")
4. Check "Is active" to show on website
5. Click SAVE

#### **Products:**
- Complete product catalog management
- Multiple images per product
- Size & color variants
- Pricing with compare-at prices (sale pricing)
- Inventory tracking (SKU, stock quantity)
- Luxury details (material, made in, designer bio)
- Featured/New Arrival flags

**Product Fields Explained:**
- **Name:** Product title (e.g., "GG Marmont Matelassé Bag")
- **Brand:** Designer name (e.g., "Gucci")
- **Category:** Select from dropdown
- **Price:** Current selling price
- **Compare at Price:** Original price (shows discount)
- **Sizes:** JSON array (e.g., `["XS", "S", "M", "L", "XL"]`)
- **Colors:** JSON array (e.g., `["Black", "Red", "Navy"]`)
- **Material:** e.g., "100% Calfskin Leather"
- **Made In:** e.g., "Italy", "France"
- **Stock Quantity:** Number of items available
- **Is Featured:** Show on homepage
- **Is New Arrival:** Add "NEW" badge
- **Is On Sale:** Highlight discounted items

**Adding Product Images:**
1. Scroll to "Product Images" section
2. Click "ADD PRODUCT IMAGE"
3. Upload image or enter URL
4. Set as main image if needed
5. Can add multiple images (colors, angles, details)

---

### **2. SHOPPING CART** 🛒

#### **Carts:**
- View all user carts
- See total items and subtotal amounts
- Monitor cart activity

#### **Cart Items:**
- See what's in each cart
- Check quantities, sizes, colors
- Identify popular products

**Use Case:** Track abandoned carts for marketing campaigns

---

### **3. ORDERS** 📦

#### **Orders:**
- Order number (auto-generated: ORD-YYYYMMDD-XXXX)
- Customer information
- Order status workflow:
  - Pending → Processing → Shipped → Delivered
- Payment status (Paid/Unpaid)
- Total amount
- Order date

**Order Management:**
1. Click on an order
2. Change status dropdown
3. Update payment status
4. Save changes

#### **Order Items:**
- Individual products in each order
- Quantity and price at time of purchase
- Product variants (size/color)

#### **Addresses:**
- Shipping addresses
- Billing addresses
- Search by city/state

---

### **4. PAYMENTS** 💳

#### **Payment Records:**
- Transaction IDs
- Stripe payment intent IDs
- Payment amounts
- Payment methods (Credit Card, PayPal, etc.)
- Payment status
- Linked orders

**Integration Ready:**
- Stripe API keys configured in settings
- Payment intent creation endpoint ready
- Test mode enabled with test keys

---

### **5. REVIEWS & WISHLIST** ⭐

#### **Reviews:**
- All customer reviews
- Star ratings (1-5)
- Verified purchase badges
- Approval status (moderation)
- Customer names

**Moderation Workflow:**
1. Go to Reviews → Reviews
2. Read review content
3. Check "Is approved" for good reviews
4. Uncheck to hide inappropriate reviews
5. Reviews appear on product pages only if approved

#### **Wishlists:**
- User saved products
- Count of products per wishlist
- Browse by user

---

### **6. HOMEPAGE CONTENT** 🏠

#### **Banners:**
- Hero banner images
- Title and subtitle text
- Call-to-action buttons
- Link URLs
- Priority ordering
- Active/inactive toggle

**Creating a Homepage Banner:**
1. Go to Shop → Banners → ADD
2. Upload image (recommended: 1920x800px)
3. Enter title (e.g., "SPRING COLLECTION 2024")
4. Add subtitle (e.g., "Discover the latest trends")
5. Set priority (1 = highest, shows first)
6. Check "Is active"
7. Optional: Add button text and link URL
8. SAVE

**Current Sample Banner:**
- Title: "THE NEW LUXURY"
- Subtitle: "Discover timeless elegance"
- Image: Fashion editorial photography

#### **Featured Collections:**
- Curated product groups
- Collection title and description
- Select multiple products
- Active/inactive status

**Example Use:**
- "Summer Essentials" collection
- "Party Season Edit" collection
- "Investment Pieces" collection

#### **Newsletter Subscriptions:**
- Customer email list
- Subscription status
- Signup dates

**Export for Email Marketing:**
1. Go to Newsletter Subscriptions
2. Filter by "Is subscribed"
3. Export emails for Mailchimp/SendGrid

---

### **7. USERS** 👥

#### **User Accounts:**
- Username and email
- First & last name
- Staff status (admin access)
- Superuser privileges
- Account active/inactive
- Date joined

**User Management:**
- Create new customers manually
- Reset passwords
- Deactivate accounts
- Grant staff access

**User Groups & Permissions:**
- Assign to groups
- Granular permissions
- Custom roles possible

---

## 🎨 **ADMIN FEATURES**

### **Bulk Actions:**
- Select multiple items
- Delete selected
- Update status in bulk

### **Search:**
- Search by name, email, product name
- Fast filtering across large datasets

### **Filters:**
- Filter by status, date, category
- Combine multiple filters

### **Export:**
- Export filtered data to CSV
- Useful for analytics

### **Rich Text Editing:**
- Formatted product descriptions
- HTML support in some fields

---

## 📊 **ADMIN PANEL NAVIGATION**

### **Left Sidebar Menu:**

```
📦 PRODUCTS
  ├── Categories
  └── Products

🛒 CART
  ├── Carts
  └── Cart Items

📦 ORDERS
  ├── Orders
  ├── Order Items
  ├── Shipping Addresses
  └── Billing Addresses

💳 PAYMENTS
  └── Payments

⭐ REVIEWS & WISHLIST
  ├── Reviews
  └── Wishlists

🏪 SHOP
  ├── Banners
  ├── Featured Collections
  └── Newsletter Subscriptions

👥 USERS
  └── Users
```

---

## 🔧 **ADMIN CUSTOMIZATION TIPS**

### **Add More Staff Users:**
1. Go to Users → ADD USER
2. Enter username and email
3. Set password
4. Check "Staff status" for admin access
5. Check "Superuser status" for full control
6. SAVE

### **Create Product Variants:**
In Product admin:
```json
Sizes: ["35", "36", "37", "38", "39", "40"]
Colors: ["Black", "Nude", "Red"]
```

### **Set Up a Sale:**
1. Edit products
2. Set "Compare at Price" higher than "Price"
3. Check "Is on sale"
4. Discount percentage auto-calculated

### **Feature Products on Homepage:**
1. Edit product
2. Check "Is featured"
3. Appears in "Featured Collection" section

### **Add New Arrivals:**
1. Edit product
2. Check "Is new arrival"
3. Gets "NEW" badge on frontend

---

## 🚀 **COMMON TASKS**

### **Task 1: Add a New Product**
1. Products → Products → ADD
2. Fill in basic info (name, brand, category)
3. Set pricing ($2,590.00)
4. Add compare-at price if on sale ($2,890.00)
5. Add sizes: `["One Size"]` or `["S", "M", "L"]`
6. Add colors: `["Black", "Tan"]`
7. Write description
8. Add material: "100% Leather"
9. Add made in: "Italy"
10. Upload product images
11. Set flags (Featured, New Arrival)
12. SAVE

### **Task 2: Create Homepage Banner**
1. Shop → Banners → ADD
2. Upload hero image
3. Title: "NEW SEASON"
4. Subtitle: "Shop the latest trends"
5. Button text: "SHOP NOW"
6. Link: "/products"
7. Priority: 1 (highest)
8. Is active: ✓
9. SAVE

### **Task 3: Approve a Review**
1. Reviews → Reviews
2. Find pending review
3. Read content
4. Check "Is approved"
5. SAVE

### **Task 4: Process an Order**
1. Orders → Orders
2. Click order number
3. Change status: "Processing"
4. When shipped: Change to "Shipped"
5. When delivered: Change to "Delivered"
6. Mark as paid if not already

### **Task 5: Manage Inventory**
1. Products → Products
2. Filter by category or brand
3. Check stock quantities
4. Update low stock items
5. Set to inactive if out of stock

---

## 🎯 **BEST PRACTICES**

### **Product Photos:**
- Use high-resolution images (min 1000x1000px)
- Multiple angles (front, back, detail)
- Lifestyle shots (on model/in use)
- Consistent background (white or lifestyle)
- Show texture and details

### **Product Descriptions:**
- Start with key features
- Include measurements/dimensions
- Mention materials and care
- Add designer/story context
- Use luxury language ("exquisite", "craftsmanship")

### **Pricing Strategy:**
- Always show compare-at price for sales
- Calculate discount % automatically
- Use .00 or .95 endings (luxury standard)
- Round to nearest $5 or $10

### **Category Organization:**
- Keep hierarchy shallow (2-3 levels max)
- Clear, descriptive names
- Don't overlap categories
- Use slugs for SEO

### **Inventory Management:**
- Update stock regularly
- Set low stock alerts
- Remove out-of-stock items or mark inactive
- Track bestsellers

---

## 🔐 **SECURITY TIPS**

### **Staff Access:**
- Only grant staff status to trusted users
- Use groups for permission control
- Regularly review staff list
- Remove inactive staff accounts

### **Data Protection:**
- Never share admin credentials
- Use strong passwords
- Enable 2FA if available
- Log out after each session

### **Backup Strategy:**
- Regular database backups
- Export important data
- Keep backup of product images

---

## 📈 **ANALYTICS & REPORTING**

### **Track in Admin:**
- Most viewed products
- Best-selling categories
- Average order value
- Customer retention
- Cart abandonment rate

### **Export Data For:**
- Monthly sales reports
- Inventory planning
- Customer segmentation
- Marketing campaigns

---

## 🆘 **TROUBLESHOOTING**

### **Issue: Can't upload images**
**Solution:** Check `MEDIA_ROOT` and `MEDIA_URL` in settings.py

### **Issue: Products not showing on frontend**
**Solution:** Ensure "Is active" is checked

### **Issue: Cart not updating**
**Solution:** Check browser console for errors, verify API endpoints

### **Issue: Reviews not appearing**
**Solution:** Must be marked "Is approved" in admin

---

## 🎉 **YOU'RE READY!**

Your admin panel is fully configured and ready to manage your luxury fashion e-commerce empire!

**Access it anytime at:** http://127.0.0.1:8000/admin/

**Need help?** The admin interface has built-in help tooltips and Django's excellent documentation.

---

**Happy Selling! 👗👠👜**
