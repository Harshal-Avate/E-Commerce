# Products App

## Overview
The `products` app serves as the core catalog of the E-Commerce platform. It manages inventory, categorization, pricing, and visual assets associated with everything available for purchase.

## Features
- Hierarchical category management.
- Product listings with rich descriptions, pricing, and stock availability.
- Multi-image or video gallery support for items.
- Advanced filtering or search logic for browsing.

## Key Components
- **Models**: `Category`, `Product` and related gallery models.
- **Views**: Renders `product_list` and `product_detail` pages with required filtering context.
- **URLs**: Routes paths such as `/`, `/<slug:category_slug>/`, `/product/<int:id>/`.
