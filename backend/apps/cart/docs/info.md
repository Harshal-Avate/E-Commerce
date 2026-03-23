# Cart App

## Overview
The `cart` app maintains the state of a user's shopping cart, allowing them to temporarily store items they wish to purchase.

## Features
- Add items to the cart.
- Remove items from the cart.
- Adjust quantity of items in the cart (increment/decrement).
- Calculate total prices (including subtotal, taxes, shipping).
- Link cart to session (for anonymous users) or database (for authenticated users).

## Key Components
- **Views**: Handles cart mutation requests like adding or removing items.
- **Context Processors**: Exposes global cart variables (like item counts) directly to templates (e.g., `global_cart_count`).
- **URLs**: Routes actions like `/add/<int:product_id>/`, `/cart/`, etc.
