# LuxMarket E-Commerce Platform

A premium, modern e-commerce platform built with a robust Django backend and a beautifully designed HTML/CSS/Bootstrap frontend. LuxMarket delivers a high-end shopping experience featuring interactive product galleries, secure user authentication, and an efficient checkout pipeline.

---

## 🚀 Features

### Frontend (User Interface)
The frontend is designed with a focus on "Premium Retail" aesthetics, utilizing heavy glassmorphism, dynamic spacing, and soft micro-animations.
* **Responsive Design:** Fully responsive layout built on top of **Bootstrap 5** alongside custom Vanilla CSS for granular control.
* **LuxMarket Standard Theme (`style.css`):** A clean, professional palette of deep slate, professional blue, and off-white.
* **Antigravity Experience (`antigravity.css`):** An alternate "zero-gravity" space-tech theme featuring floating elements, neon accents, and interactive starry backgrounds.
* **Advanced Product Media:** Support for primary product images, multiple gallery thumbnails, and HTML5 video playback seamlessly integrated with a side-scrolling Javascript viewer.
* **Real-time Search:** Dynamic search bar seamlessly integrated into the navigation header.

### Backend (Django API & Logic)
Powered by **Django 4.2**, the backend is partitioned into distinct modular Apps for scalability.
* **`apps.products`:** Manages the product catalog. Features a `Product` model with an inline `ProductImage` gallery relationship. Supports dynamic search filtering (Name & Description).
* **`apps.accounts`:** Handles user registration, authentication, login/logout, and profile administration using robust Django sessions.
* **`apps.cart`:** Stores temporary shopping sessions securely without forcing immediate user registration until checkout.
* **`apps.orders`:** Manages the checkout flow, storing comprehensive shipping addresses, updating item stock quantities dynamically, and generating Order IDs.

### Admin Dashboard
* **Enhanced Model Management:** Contains custom `ModelAdmin` registrations. The product panel includes an inline gallery editor and explicit UI action buttons specifically for administrative control, preventing UI crossover.

---

## 🛠️ Technology Stack

* **Backend Framework:** Python / Django 4.2
* **Frontend Structure:** HTML5 (Django Templates)
* **Frontend Styling:** Vanilla CSS3, Bootstrap 5.3
* **Typography & Icons:** Google Fonts (Inter, JetBrains Mono), FontAwesome 6
* **Database:** SQLite3 (Default for development)
* **Media Management:** Local File System (`/media/` root)

---

## ⚙️ Installation & Setup

### Prerequisites
* Python 3.10+
* Virtual Environment (recommended)

### Installation Steps

1. **Navigate to the Backend Directory:**
   ```bash
   cd backend
   ```

2. **Install Dependencies:**
   *(Ensure you have Django installed in your environment)*
   ```bash
   pip install django pillow
   ```
   *(Pillow is required for handling `ImageField` models)*

3. **Apply Database Migrations:**
   Run the following to initialize your SQLite database and apply all app schemas:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a Superuser (Admin Dashboard Access):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the Development Server:**
   ```bash
   python manage.py runserver 8000
   ```
   *The server will be available at `http://127.0.0.1:8000/`*

---

## 📁 Project Structure

```text
E-Commerce/
│
├── backend/                  # Core Django Project
│   ├── core/                 # Main Settings & URL Router
│   ├── apps/                 # Modular Django Apps
│   │   ├── accounts/         # User Authentication
│   │   ├── cart/             # Session-based Cart
│   │   ├── orders/           # Checkout & Receipts 
│   │   └── products/         # Master Catalog & Media
│   └── manage.py             # Django Execution Script
│
├── frontend/                 # Complete HTML Layouts
│   └── templates/            # Django Template Integrations
│       ├── base.html         # Master Layout Structure
│       ├── antigravity.html  # Alternative Easter-egg UI
│       └── ...               # App-specific HTML renders
│
├── static/                   # Global Static Assets
│   ├── css/                  # Compiled & Custom Styles
│   │   ├── style.css         # Main LuxMarket Theme
│   │   └── antigravity.css   # Dark Tech Theme
│   └── js/                   # Frontend logic
│
└── media/                    # User & Admin Uploads
    └── products/             # High-res Images & Videos
```

---

## 📝 Roadmap / Future Enhancements
* Incorporate Razorpay / Stripe gateway for the Digital Payments selection.
* Enhance user profiles to allow historical receipt downloads in PDF format.
* Switch database backend from SQLite to PostgreSQL for production deployment.
