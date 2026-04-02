"""
Management command to seed luxury fashion data
Usage: python manage.py seed_luxury_data
"""
from django.core.management.base import BaseCommand
from products.models import Category, Product, ProductImage
from shop.models import Banner, FeaturedCollection
from django.conf import settings
import random

class Command(BaseCommand):
    help = 'Seed database with luxury fashion data'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌟 Seeding luxury fashion data...')
        
        # Create Categories
        self.stdout.write('Creating categories...')
        designers = [
            ('Designers', ['Gucci', 'Prada', 'Chanel', 'Louis Vuitton', 'Hermès']),
            ('Clothing', ['Dresses', 'Tops', 'Bottoms', 'Outerwear']),
            ('Shoes', ['Heels', 'Flats', 'Sneakers', 'Boots']),
            ('Bags', ['Handbags', 'Clutches', 'Backpacks', 'Tote Bags']),
            ('Accessories', ['Jewelry', 'Watches', 'Scarves', 'Belts']),
        ]
        
        categories = {}
        for parent_name, children in designers:
            parent_cat, _ = Category.objects.get_or_create(
                name=parent_name,
                defaults={'description': f'Luxury {parent_name} collection'}
            )
            categories[parent_name] = parent_cat
            
            for child_name in children:
                child_cat, _ = Category.objects.get_or_create(
                    name=child_name,
                    parent=parent_cat,
                    defaults={'description': f'{child_name} collection'}
                )
        
        # Create Sample Products
        self.stdout.write('Creating luxury products...')
        
        product_data = [
            {
                'name': 'Gucci GG Marmont Matelassé Shoulder Bag',
                'brand': 'Gucci',
                'category': categories.get('Bags'),
                'price': 2590.00,
                'compare_at_price': 2890.00,
                'description': 'The GG Marmont small shoulder bag has a softly structured shape and an oversized flap closure with Double G hardware.',
                'material': 'Matelassé chevron leather',
                'made_in': 'Italy',
                'sizes': [],
                'colors': ['Black', 'Red', 'Nude'],
                'is_featured': True,
                'is_new_arrival': False,
            },
            {
                'name': 'Prada Re-Edition 2005 Nylon Mini Bag',
                'brand': 'Prada',
                'category': categories.get('Bags'),
                'price': 1350.00,
                'description': 'Re-edition of the iconic 2005 mini bag in nylon with leather details.',
                'material': 'Nylon and Saffiano leather',
                'made_in': 'Italy',
                'sizes': [],
                'colors': ['Black'],
                'is_featured': True,
                'is_new_arrival': True,
            },
            {
                'name': 'Chanel Classic Flap Bag Medium',
                'brand': 'Chanel',
                'category': categories.get('Bags'),
                'price': 10200.00,
                'description': 'The iconic Chanel Classic Flap Bag in quilted caviar leather with gold-tone hardware.',
                'material': 'Quilted caviar leather',
                'made_in': 'France',
                'sizes': [],
                'colors': ['Black', 'Beige'],
                'is_featured': True,
                'is_new_arrival': False,
            },
            {
                'name': 'Louis Vuitton Neverfull MM Monogram',
                'brand': 'Louis Vuitton',
                'category': categories.get('Bags'),
                'price': 2030.00,
                'description': 'The iconic Neverfull tote in classic monogram canvas. Roomy and versatile.',
                'material': 'Monogram canvas',
                'made_in': 'France',
                'sizes': ['MM', 'GM'],
                'colors': ['Brown'],
                'is_featured': True,
                'is_new_arrival': False,
            },
            {
                'name': 'Silk Evening Gown with Embellishments',
                'brand': 'Valentino',
                'category': categories.get('Clothing'),
                'price': 4500.00,
                'compare_at_price': 5200.00,
                'description': 'Stunning floor-length silk gown with hand-sewn crystal embellishments.',
                'material': '100% Silk',
                'made_in': 'Italy',
                'sizes': ['XS', 'S', 'M', 'L'],
                'colors': ['Black', 'Navy', 'Burgundy'],
                'is_featured': True,
                'is_new_arrival': True,
            },
            {
                'name': 'Cashmere Blend Coat',
                'brand': 'Max Mara',
                'category': categories.get('Clothing'),
                'price': 3200.00,
                'description': 'Luxurious cashmere blend coat with classic tailored fit.',
                'material': '90% Cashmere, 10% Wool',
                'made_in': 'Italy',
                'sizes': ['XS', 'S', 'M', 'L', 'XL'],
                'colors': ['Camel', 'Black', 'Grey'],
                'is_featured': False,
                'is_new_arrival': False,
            },
            {
                'name': 'Leather Stiletto Pumps',
                'brand': 'Christian Louboutin',
                'category': categories.get('Shoes'),
                'price': 795.00,
                'description': 'Iconic red sole pumps in smooth leather. 100mm heel.',
                'material': 'Leather',
                'made_in': 'Italy',
                'sizes': ['35', '36', '37', '38', '39', '40'],
                'colors': ['Black', 'Nude', 'Red'],
                'is_featured': True,
                'is_new_arrival': False,
            },
            {
                'name': 'Designer Sneakers',
                'brand': 'Balenciaga',
                'category': categories.get('Shoes'),
                'price': 995.00,
                'description': 'Chunky sneakers with exaggerated sole and mixed materials.',
                'material': 'Mesh, Leather, Rubber',
                'made_in': 'Italy',
                'sizes': ['35', '36', '37', '38', '39', '40', '41'],
                'colors': ['White', 'Black', 'Grey'],
                'is_featured': False,
                'is_new_arrival': True,
            },
        ]
        
        created_products = []
        for data in product_data:
            if data['category']:
                product = Product.objects.create(**data)
                created_products.append(product)
                self.stdout.write(f'  ✓ Created: {product.name}')
        
        # Create Featured Collection
        self.stdout.write('Creating featured collections...')
        collection, _ = FeaturedCollection.objects.get_or_create(
            name='Editor\'s Picks',
            defaults={
                'description': 'Curated selection of the season\'s most coveted pieces',
            }
        )
        collection.products.set(created_products[:4])
        
        # Create Homepage Banner
        self.stdout.write('Creating homepage banners...')
        Banner.objects.get_or_create(
            title='New Season Arrivals',
            defaults={
                'subtitle': 'Discover the latest luxury trends',
                'description': 'Shop the newest arrivals from top designers',
                'cta_text': 'Shop Now',
                'cta_link': '/products/?is_new_arrival=true',
            }
        )
        
        self.stdout.write(self.style.SUCCESS('\n✨ Successfully seeded luxury fashion data!'))
        self.stdout.write(f'Created {len(created_products)} products')
        self.stdout.write(f'Categories: {Category.objects.count()}')
        self.stdout.write(f'Banners: {Banner.objects.count()}')
