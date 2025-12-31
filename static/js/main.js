// Form validation and interactivity
document.addEventListener('DOMContentLoaded', function() {
    // Add range sliders for better UX
    const rangeInputs = document.querySelectorAll('input[type="range"]');
    
    rangeInputs.forEach(input => {
        const valueDisplay = input.nextElementSibling;
        if (valueDisplay && valueDisplay.classList.contains('range-value')) {
            valueDisplay.textContent = input.value;
            input.addEventListener('input', function() {
                valueDisplay.textContent = this.value;
                // Add pulse animation
                valueDisplay.style.animation = 'none';
                setTimeout(() => {
                    valueDisplay.style.animation = 'pulse 0.3s ease';
                }, 10);
            });
        }
    });

    // Form submission with loading state
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(e) {
            const btn = form.querySelector('button[type="submit"]');
            const loading = document.querySelector('.loading');
            
            if (btn && loading) {
                btn.disabled = true;
                btn.textContent = 'Processing...';
                loading.classList.add('active');
            }
        });
    }

    // Add smooth scroll behavior
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add input focus animations
    const inputs = document.querySelectorAll('input, select');
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.style.transform = 'scale(1.02)';
        });
        
        input.addEventListener('blur', function() {
            this.parentElement.style.transform = 'scale(1)';
        });
    });

    // Add number input increment/decrement buttons
    const numberInputs = document.querySelectorAll('input[type="number"]');
    numberInputs.forEach(input => {
        // Add visual feedback on change
        input.addEventListener('change', function() {
            this.style.animation = 'none';
            setTimeout(() => {
                this.style.animation = 'pulse 0.3s ease';
            }, 10);
        });
    });
});

// Add pulse animation to CSS dynamically
const style = document.createElement('style');
style.textContent = `
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
`;
document.head.appendChild(style);

