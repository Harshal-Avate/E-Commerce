# Accounts App

## Overview
The `accounts` app handles user authentication, registration, login, logout, and user profile management for the E-Commerce platform.

## Features
- Custom user model (if applicable) or default Django User mapping.
- Registration workflows including validation.
- Login and Logout session management.
- User profile updates and history.

## Key Components
- **Models**: Defines user-related database tables.
- **Views**: Handles authentication logic, form processing, and profile rendering.
- **Forms**: Contains `UserCreationForm` and custom authentication forms.
- **URLs**: Maps endpoints like `/login/`, `/signup/`, `/logout/`, etc.
