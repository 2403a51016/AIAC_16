// This file is intentionally left blank.

// Smooth scroll is handled by CSS, but you can add active nav highlighting if desired
document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('nav a');
    window.addEventListener('scroll', () => {
        let fromTop = window.scrollY + 80;
        navLinks.forEach(link => {
            const section = document.querySelector(link.hash);
            if (
                section.offsetTop <= fromTop &&
                section.offsetTop + section.offsetHeight > fromTop
            ) {
                link.style.background = 'var(--accent)';
                link.style.color = '#fff';
            } else {
                link.style.background = '';
                link.style.color = 'var(--accent)';
            }
        });
    });
});