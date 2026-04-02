import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gossip_project_core.settings')
django.setup()

from products.models import Product

# Update existing products with unique images
products_images = [
    {
        'name': 'Gucci GG Marmont Bag',
        'image_url': 'https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=800&q=80',
        'description': 'The iconic GG Marmont shoulder bag features a softly structured shape and an oversized flap closure with hearts on the back.',
        'material': 'Matelassé chevron leather',
        'made_in': 'Italy',
        'sizes': ['One Size'],
        'colors': ['Black', 'Red', 'Nude'],
    },
    {
        'name': 'Prada Re-Edition Nylon Mini Bag',
        'image_url': 'https://images.unsplash.com/photo-1591561954557-26941169b49e?w=800&q=80',
        'description': "A minimalist interpretation of functionality, crafted from Prada's signature nylon with Saffiano leather trim.",
        'material': 'Recycled nylon with Saffiano leather',
        'made_in': 'Italy',
        'sizes': ['One Size'],
        'colors': ['Black', 'Pink', 'White'],
    },
    {
        'name': 'Chanel Classic Flap Bag Medium',
        'image_url': 'https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=800&q=80',
        'description': 'The epitome of Chanel elegance, this Medium Classic Flap bag is crafted from quilted caviar leather with gold-tone hardware.',
        'material': 'Quilted caviar leather',
        'made_in': 'France',
        'sizes': ['Medium'],
        'colors': ['Black', 'Beige', 'Navy'],
    },
    {
        'name': 'Valentino Silk Evening Gown',
        'image_url': 'https://images.unsplash.com/photo-1566174053879-31528523f8ae?w=800&q=80',
        'description': 'An exquisite floor-length evening gown in luxurious silk chiffon. Adorned with hand-applied crystal embellishments.',
        'material': '100% Silk chiffon with Swarovski crystals',
        'made_in': 'Italy',
        'sizes': ['IT 38', 'IT 40', 'IT 42', 'IT 44'],
        'colors': ['Midnight Blue', 'Black', 'Burgundy'],
    },
    {
        'name': 'Christian Louboutin So Kate Pumps',
        'image_url': 'https://images.unsplash.com/photo-1543163521-1bf539c55dd2?w=800&q=80',
        'description': 'The iconic So Kate pump features a sleek pointed toe and a dramatic 120mm stiletto heel with signature red sole.',
        'material': 'Patent leather',
        'made_in': 'Italy',
        'sizes': ['35', '36', '37', '38', '39', '40'],
        'colors': ['Black', 'Nude', 'Red'],
    },
]

print("🌟 Updating products with unique images...")

for img_data in products_images:
    try:
        product = Product.objects.get(name=img_data['name'])
        product.image_url = img_data['image_url']
        product.description = img_data['description']
        product.material = img_data['material']
        product.made_in = img_data['made_in']
        product.sizes = img_data['sizes']
        product.colors = img_data['colors']
        product.save()
        print(f"  ✓ Updated: {product.name}")
    except Product.DoesNotExist:
        print(f"  ✗ Not found: {img_data['name']}")

print("\n✨ Done!")
print(f"Total products: {Product.objects.count()}")
