import os
import django

# Setup Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gossip_project_core.settings')
django.setup()

from products.models import Category, Product
from shop.models import Banner, FeaturedCollection

print("🌟 Seeding luxury fashion data...")

# Create Categories
categories_data = [
    ('Designers', ['Gucci', 'Prada', 'Chanel', 'Louis Vuitton']),
    ('Clothing', ['Dresses', 'Tops', 'Coats']),
    ('Shoes', ['Heels', 'Sneakers', 'Boots']),
    ('Bags', ['Handbags', 'Clutches', 'Totes']),
]

categories = {}
for parent_name, children in categories_data:
    parent_cat, _ = Category.objects.get_or_create(name=parent_name)
    categories[parent_name] = parent_cat
    for child in children:
        Category.objects.get_or_create(name=child, parent=parent_cat)

# Create Products with UNIQUE luxury images
products_data = [
    {
        'name': 'Gucci GG Marmont Bag',
        'brand': 'Gucci',
        'category': categories.get('Bags'),
        'price': 2590.00,
        'compare_at_price': 2890.00,
        'description': 'The iconic GG Marmont shoulder bag features a softly structured shape and an oversized flap closure with hearts on the back. The Double G hardware is inspired by an archival design from the 1970s.',
        'material': 'Matelassé chevron leather',
        'made_in': 'Italy',
        'sizes': ['One Size'],
        'colors': ['Black', 'Red', 'Nude'],
        'is_featured': True,
        'is_new_arrival': False,
        'image_url': 'https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=800&q=80',
    },
    {
        'name': 'Prada Re-Edition Nylon Mini Bag',
        'brand': 'Prada',
        'category': categories.get('Bags'),
        'price': 1350.00,
        'compare_at_price': 1450.00,
        'description': "A minimalist interpretation of functionality, this mini bag is crafted from Prada's signature nylon with Saffiano leather trim. Features the iconic enameled metal triangle logo.",
        'material': 'Recycled nylon with Saffiano leather',
        'made_in': 'Italy',
        'sizes': ['One Size'],
        'colors': ['Black', 'Pink', 'White'],
        'is_featured': True,
        'is_new_arrival': True,
        'image_url': 'https://images.unsplash.com/photo-1591561954557-26941169b49e?w=800&q=80',
    },
    {
        'name': 'Chanel Classic Flap Bag Medium',
        'brand': 'Chanel',
        'category': categories.get('Bags'),
        'price': 10200.00,
        'description': 'The epitome of Chanel elegance, this Medium Classic Flap bag is crafted from quilted caviar leather with gold-tone hardware. Features the iconic CC turn-lock closure and interwoven chain strap.',
        'material': 'Quilted caviar leather',
        'made_in': 'France',
        'sizes': ['Medium'],
        'colors': ['Black', 'Beige', 'Navy'],
        'is_featured': True,
        'is_new_arrival': False,
        'image_url': 'https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=800&q=80',
    },
    {
        'name': 'Valentino Silk Evening Gown',
        'brand': 'Valentino',
        'category': categories.get('Clothing'),
        'price': 4500.00,
        'compare_at_price': 5200.00,
        'description': 'An exquisite floor-length evening gown in luxurious silk chiffon. Adorned with hand-applied crystal embellishments along the neckline and cascading down the bodice.',
        'material': '100% Silk chiffon with Swarovski crystals',
        'made_in': 'Italy',
        'sizes': ['IT 38', 'IT 40', 'IT 42', 'IT 44'],
        'colors': ['Midnight Blue', 'Black', 'Burgundy'],
        'is_featured': True,
        'is_new_arrival': True,
        'image_url': 'https://images.unsplash.com/photo-1566174053879-31528523f8ae?w=800&q=80',
    },
    {
        'name': 'Christian Louboutin So Kate Pumps',
        'brand': 'Christian Louboutin',
        'category': categories.get('Shoes'),
        'price': 795.00,
        'description': 'The iconic So Kate pump features a sleek pointed toe and a dramatic 120mm stiletto heel. Crafted from glossy patent leather with the signature red lacquered sole.',
        'material': 'Patent leather',
        'made_in': 'Italy',
        'sizes': ['35', '36', '37', '38', '39', '40'],
        'colors': ['Black', 'Nude', 'Red'],
        'is_featured': True,
        'is_new_arrival': False,
        'image_url': 'https://images.unsplash.com/photo-1543163521-1bf539c55dd2?w=800&q=80',
    },
]

created_products = []
for data in products_data:
    if data['category']:
        product = Product.objects.create(**data)
        created_products.append(product)
        print(f"  ✓ Created: {product.name}")

# Create Banner
Banner.objects.get_or_create(
    title='New Season Arrivals',
    defaults={
        'subtitle': 'Discover the latest luxury trends',
        'cta_text': 'Shop Now',
    }
)

# Create Collection
collection, _ = FeaturedCollection.objects.get_or_create(
    name="Editor's Picks",
    description='Curated selection of coveted pieces'
)
collection.products.set(created_products[:4])

print("\n✨ Successfully seeded data!")
print(f"Products: {Product.objects.count()}")
print(f"Categories: {Category.objects.count()}")
