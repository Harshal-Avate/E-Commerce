import os
import django
import sys
from pathlib import Path

# Add the project roots to sys.path
BASE_DIR = Path(__file__).resolve().parent / "backend"
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "apps"))

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from apps.products.models import Category, Product
from django.utils.text import slugify

def populate_categories():
    categories_data = [
        {"name": "Electronics", "description": "High-end gadgets and modern tech solutions."},
        {"name": "Fashion", "description": "Premium apparel and luxury accessories."},
        {"name": "Home & Living", "description": "Elegant decor and functional home essentials."},
        {"name": "Health & Beauty", "description": "Curated wellness and self-care products."},
    ]

    print("Populating categories...")
    for data in categories_data:
        cat, created = Category.objects.get_or_create(
            name=data["name"],
            defaults={
                "slug": slugify(data["name"]),
                "description": data["description"]
            }
        )
        if created:
            print(f"Created category: {cat.name}")
        else:
            print(f"Category already exists: {cat.name}")

    # Assign random categories to products that don't have one
    products_without_category = Product.objects.filter(category__isnull=True)
    all_cats = list(Category.objects.all())
    
    if products_without_category.exists() and all_cats:
        import random
        print(f"Assigning categories to {products_without_category.count()} products...")
        for product in products_without_category:
            random_cat = random.choice(all_cats)
            product.category = random_cat
            product.save()
            print(f"Assigned {random_cat.name} to {product.name}")

if __name__ == "__main__":
    populate_categories()
