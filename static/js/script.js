// Smooth transitions and premium UI interactions
document.addEventListener('DOMContentLoaded', function() {
    // 1. Initial greeting for smooth experience
    console.log("LuxMarket Frontend Initialized. Welcome to a premium experience.");

    // 2. Navbar glass effect on scroll
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('glass-scrolled', 'navbar-light', 'bg-white', 'shadow-lg');
            navbar.style.paddingTop = '10px';
            navbar.style.bottomPadding = '10px';
        } else {
            navbar.classList.remove('glass-scrolled', 'shadow-lg');
            navbar.style.paddingTop = '15px';
            navbar.style.bottomPadding = '15px';
        }
    });

    // 3. Simple Product Card Animation on hover (CSS is handling most of it)
    const productCards = document.querySelectorAll('.product-card');
    productCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            // Additional custom JS animations can go here
        });
    });

    // 4. Form Validation placeholder (Minimalist)
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', (e) => {
            // Example: Show loading state
            const submitBtn = loginForm.querySelector('button[type="submit"]');
            submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status"></span> Logging In...';
        });
    }

    // 5. Success Message Auto-Hide
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
});
