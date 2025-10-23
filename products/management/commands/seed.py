from django.core.management.base import BaseCommand
from django.utils import timezone
from products.models import Product, Category


class Command(BaseCommand):
    help = "Seeds the database with sample product and category data"

    def handle(self, *args, **kwargs):
        sample_products = [
            {
                "name": "Laptop Pro 15",
                "description": "High-performance laptop with 16GB RAM and 512GB SSD.",
                "price": 1200.00,
                "category": "Electronics",
                "stock_quantity": 10,
                "image_url": "https://cdn.pixabay.com/photo/2016/03/27/07/12/apple-1282241_1280.jpg",
            },
            {
                "name": "Smartphone X",
                "description": "Latest model smartphone with 128GB storage and dual cameras.",
                "price": 850.00,
                "category": "Electronics",
                "stock_quantity": 25,
                "image_url": "https://cdn.pixabay.com/photo/2018/04/27/03/51/technology-3353701_1280.jpg",
            },
            {
                "name": "Wireless Mouse",
                "description": "Ergonomic wireless mouse with long battery life.",
                "price": 25.50,
                "category": "Accessories",
                "stock_quantity": 50,
                "image_url": "https://cdn.pixabay.com/photo/2021/04/07/16/13/gaming-mouse-6159550_1280.jpg",
            },
            {
                "name": "Mechanical Keyboard",
                "description": "RGB mechanical keyboard with tactile switches.",
                "price": 75.00,
                "category": "Accessories",
                "stock_quantity": 30,
                "image_url": "https://cdn.pixabay.com/photo/2024/04/17/01/59/mechanical-keyboard-8701176_1280.png",
            },
            {
                "name": "Laser Printer",
                "description": "Compact wireless laser printer ideal for home offices.",
                "price": 150.00,
                "category": "Office Equipment",
                "stock_quantity": 12,
                "image_url": "https://cdn.pixabay.com/photo/2013/07/13/13/32/printer-161063_1280.png",
            },
            {
                "name": "Smartwatch Fit 3",
                "description": "Fitness tracking smartwatch with heart rate monitor.",
                "price": 199.99,
                "category": "Wearables",
                "stock_quantity": 40,
                "image_url": "https://cdn.pixabay.com/photo/2015/06/25/17/21/smart-watch-821557_1280.jpg",
            },
            {
                "name": "Bluetooth Speaker",
                "description": "Portable Bluetooth speaker with rich sound and deep bass.",
                "price": 49.99,
                "category": "Audio",
                "stock_quantity": 60,
                "image_url": "https://cdn.pixabay.com/photo/2021/01/09/12/30/speaker-5902204_1280.jpg",
            },
            {
                "name": "4K Monitor 27\"",
                "description": "Ultra HD monitor with crisp color accuracy.",
                "price": 350.00,
                "category": "Electronics",
                "stock_quantity": 15,
                "image_url": "https://cdn.pixabay.com/photo/2012/04/13/17/00/lcd-32872_1280.png",
            },
            {
                "name": "USB-C Hub",
                "description": "7-in-1 USB-C hub with HDMI, SD card, and USB ports.",
                "price": 39.99,
                "category": "Accessories",
                "stock_quantity": 35,
                "image_url": "https://eu.targus.com/cdn/shop/products/hyper-usb-hubs-hyper-hyperdrive-5-port-usb-c-hub-35756470206662_1024x1024.jpg?v=1692797954",
            },
            {
                "name": "Gaming Headset",
                "description": "Over-ear gaming headset with noise cancellation and mic.",
                "price": 89.99,
                "category": "Audio",
                "stock_quantity": 20,
                "image_url": "https://cdn.pixabay.com/photo/2017/07/31/11/47/headphones-2557593_1280.jpg",
            },
        ]

        for data in sample_products:
            # Ensure the category exists
            category_obj, _ = Category.objects.get_or_create(name=data["category"])

            # Create or update the product
            product, created = Product.objects.update_or_create(
                name=data["name"],
                defaults={
                    "description": data["description"],
                    "price": data["price"],
                    "category": category_obj,
                    "stock_quantity": data["stock_quantity"],
                    "image_url": data["image_url"],
                    "created_at": timezone.now(),
                },
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"✅ Created: {product.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"🔁 Updated: {product.name}"))

        self.stdout.write(self.style.SUCCESS("🎉 Database seeding completed successfully!"))