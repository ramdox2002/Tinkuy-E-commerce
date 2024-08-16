import os
import django
from django.core.management import call_command
from django.contrib.auth.models import User
from django.db import IntegrityError
from shop.models import Category, Product, Order

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

# 1. Migrar la base de datos
print("Ejecutando migraciones...")
call_command('makemigrations', 'shop')
call_command('migrate')

# 2. Crear un superusuario
try:
    if not User.objects.filter(username='admin').exists():
        print("Creando usuario administrador...")
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
        print("Usuario administrador creado exitosamente.")
    else:
        print("El usuario administrador ya existe.")
except IntegrityError:
    print("Error: El usuario administrador ya existe.")

# 3. Insertar datos de ejemplo
print("Creando datos de ejemplo...")

# Crear categorías
category1, created = Category.objects.get_or_create(name='Herramientas')
category2, created = Category.objects.get_or_create(name='Pinturas')
category3, created = Category.objects.get_or_create(name='Materiales de Construcción')

# Crear productos
Product.objects.get_or_create(
    name='Martillo',
    description='Martillo de 500g con mango de madera',
    price=35.50,
    category=category1,
    image='products/martillo.avif'
)

Product.objects.get_or_create(
    name='Brocha',
    description='Brocha de 2 pulgadas para pintura',
    price=10.99,
    category=category2,
    image='products/brocha.jpg'
)

Product.objects.get_or_create(
    name='Cemento',
    description='Bolsa de cemento de 50kg',
    price=25.00,
    category=category3,
    image='products/cemento.webp'
)

# Obtener o crear un usuario de prueba para asociar con las órdenes
user1, created = User.objects.get_or_create(username='usuario1', defaults={'email': 'usuario1@example.com', 'password': 'testpass123'})

# Crear pedidos (órdenes)
Order.objects.get_or_create(
    user=user1,
    is_paid=True
)

Order.objects.get_or_create(
    user=user1,
    is_paid=False
)

print("Datos de ejemplo creados exitosamente.")
print("¡Configuración completada!")
