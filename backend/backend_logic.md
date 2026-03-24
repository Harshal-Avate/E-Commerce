# 🛠️ Backend Logic Overview: E-Commerce Platform

This document explains the backend architecture, data flow, and core logic of the E-Commerce platform. The backend is built using **Django**, a high-level Python web framework that encourages rapid development and clean, pragmatic design.

---

## 🏗️ Core Technologies
- **Python 3.x**: The core programming language.
- **Django**: The web framework used for handling requests, routing, and database interactions.
- **SQLite**: The database used for storing product, user, and order information.
- **Django Sessions**: Used for temporary data storage (like the shopping cart).

---

## 🗄️ Database Models (Data Layer)

The data is organized into several key models across different applications:

### 1. **Products App (`apps/products`)**
- **Category**: Groups products (e.g., Electronics, Clothing).
- **Product**: Stores product details (name, description, price, stock, image, video).
- **ProductImage**: A gallery for additional product photos.

### 2. **Accounts App (`apps/accounts`)**
- Uses **Django's Built-in User Model** for authentication:
  - Username, Email, Password.
  - Handles signup and login functionality.

### 3. **Orders App (`apps/orders`)**
- **Order**: Stores main order data (user, total price, status, shipping address).
- **OrderItem**: Links specific products and their quantities to an order.

---

## 🧠 Business Logic (The "How It Works")

### 🛍️ 1. Product Management
- **Browsing**: The `product_list` view fetches all products from the database. It handles **searching** (`?q=...`) and **filtering** by category (`?category=...`).
- **Detail View**: The `product_detail` view fetches a single product by its ID to show more information.

### 🛒 2. Shopping Cart (Session-Based)
The cart does **not** use the database to store items immediately. Instead, it uses **Django Sessions**:
- **Storage**: When a user adds an item, it's stored in `request.session['cart']` as a dictionary `{ "product_id": quantity }`.
- **Logic**:
  - `add_to_cart`: Checks if the product is in stock, then adds/updates the quantity in the session.
  - `increase_quantity`/`decrease_quantity`: Updates the session dictionary directly.
  - `remove_from_cart`: Deletes the product ID key from the session dictionary.
  - `get_cart_data`: A helper function that takes the session data and fetches full product objects from the database to calculate the total price.

### 💳 3. Checkout & Order Processing
The `checkout` view (in `apps/orders`) is the most complex logic:
1. **Validation**: Checks if the user is logged in (`@login_required`) and if the cart is not empty.
2. **Data Collection**: Collects shipping address and other details from a POST form.
3. **Transaction**:
   - Creates a new `Order` record.
   - For every item in the cart, it creates an `OrderItem` linked to the new `Order`.
   - **Stock Reduction**: Subtracts the purchased quantity from the product’s `stock` field.
4. **Cleanup**: Clears the session cart (`request.session['cart'] = {}`).
5. **Success**: Redirects the user to an order success page.

### 🔐 4. Authentication
- **Signup**: Uses `UserCreationForm` to create new user records.
- **Login/Logout**: Handled by Django's auth system, ensuring users must be logged in to access the checkout and their order history.

---

## 🔄 The Request Lifecycle
1. **User Action**: User clicks "Add to Cart".
2. **URL Routing**: Django matches the URL to the `add_to_cart` view.
3. **View Logic**: The view updates the session and potentially adds a "Success" message.
4. **Database Query**: Product details are fetched to verify stock.
5. **Template Rendering**: Django renders the HTML template and sends it back to the browser.
6. **User Visibility**: The user sees the updated cart with their items.

---

## 📂 Project Structure (Summary)
- `core/`: Project settings and global URL configurations.
- `apps/`: Modular components (Accounts, Products, Cart, Orders).
- `media/`: Storage for uploaded product images and videos.
- `templates/`: (Located within apps or core) The HTML files that display data.

---
*Created on: 2026-03-24*
