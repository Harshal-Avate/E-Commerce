# Orders App

## Overview
The `orders` app is responsible for the checkout process, translating a user's cart into a permanent order record, and tracking its fulfillment status.

## Features
- Order creation from Cart data.
- Handling shipping addresses and billing information.
- Managing order statuses (Pending, Processed, Shipped, Delivered).
- Recording individual Order Items tied to a specific Order.

## Key Components
- **Models**: `Order` (stores customer details, date, status, total cost) and `OrderItem` (stores exact price and quantity of products at the time of purchase).
- **Views**: Generates checkout forms, processes finalized orders, and displays order history back to the user.
- **URLs**: Maps to routes like `/checkout/`, `/history/`, etc.
