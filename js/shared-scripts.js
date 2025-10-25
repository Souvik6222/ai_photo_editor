// Shared JavaScript for all pages

// Create animated particles
const particles = document.getElementById('particles');
if (particles) {
    function createParticles() {
        for (let i = 0; i < 15; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.top = Math.random() * 100 + '%';
            particle.style.animationDelay = Math.random() * 5 + 's';
            particle.style.animationDuration = (10 + Math.random() * 10) + 's';
            particles.appendChild(particle);
        }
    }
    createParticles();
}

// Sidebar toggle logic is handled in theme.js (with overlay and scroll lock)
const menuToggle = document.getElementById('menuToggle');
const sidebar = document.getElementById('sidebar');

// Utility Functions
function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
}

function showError(message) {
    const error = document.getElementById('error');
    const success = document.getElementById('success');
    if (error) {
        error.textContent = '❌ ' + message;
        error.style.display = 'block';
        if (success) success.style.display = 'none';
        setTimeout(() => {
            error.style.display = 'none';
        }, 5000);
    }
}

function showSuccess(message = '✅ Processing completed successfully!') {
    const success = document.getElementById('success');
    const error = document.getElementById('error');
    if (success) {
        success.textContent = message;
        success.style.display = 'block';
        if (error) error.style.display = 'none';
        setTimeout(() => {
            success.style.display = 'none';
        }, 3000);
    }
}
