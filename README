# 🛠️ Tinkuy E-commerce Backend

## 🚀 Inicio Rápido

Sigue los pasos a continuación para poner en funcionamiento tu servidor Django:

### 1. CREA UN ENTORNO VIRTUAL

```bash
virtualenv venv
```

### 2. ACTIVA EL ENTORNO VIRTUAL EN WINDOWS


```bash
    venv\scripts\activate
```

### 3. INSTALA REQUIREMENTS.TXT


```bash
    pip install -r requirements.txt
```

### 4. MIGRA LA BASE DE DATOS


```bash
    py manage.py makemigrations
    py manage.py migrate
```


### 5. CREA UN SUPERUSUARIO (ADMIN)


```bash
   py manage.py createsuperuser --username admin --email admin@example.com
```

### 6.  INSERTA DATOS DE EJEMPLO


```bash
    from shop.models import Category, Product, Order
from django.contrib.auth.models import User

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

# Crear usuario de prueba para las órdenes
user1, created = User.objects.get_or_create(username='usuario1', defaults={'email': 'usuario1@example.com', 'password': 'testpass123'})

# Crear órdenes
Order.objects.get_or_create(
    user=user1,
    is_paid=True
)

Order.objects.get_or_create(
    user=user1,
    is_paid=False
)

```

### 5. EJECUTA EL SERVIDOR


```bash
    py manage.py runserver
```

📧 Credenciales de Administrador
USERNAME: admin
PASSWORD: admin
