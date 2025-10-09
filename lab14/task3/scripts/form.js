document.getElementById('regForm').addEventListener('submit', function(e) {
    e.preventDefault();
    let valid = true;

    // Name validation
    const name = document.getElementById('name');
    const nameError = document.getElementById('nameError');
    if (name.value.trim() === '') {
        nameError.textContent = 'Please enter your name.';
        valid = false;
    } else {
        nameError.textContent = '';
    }

    // Email validation
    const email = document.getElementById('email');
    const emailError = document.getElementById('emailError');
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (email.value.trim() === '') {
        emailError.textContent = 'Please enter your email.';
        valid = false;
    } else if (!emailPattern.test(email.value.trim())) {
        emailError.textContent = 'Please enter a valid email address.';
        valid = false;
    } else {
        emailError.textContent = '';
    }

    // Phone validation
    const phone = document.getElementById('phone');
    const phoneError = document.getElementById('phoneError');
    const phonePattern = /^[0-9]{10}$/;
    if (phone.value.trim() === '') {
        phoneError.textContent = 'Please enter your phone number.';
        valid = false;
    } else if (!phonePattern.test(phone.value.trim())) {
        phoneError.textContent = 'Please enter a valid 10-digit phone number.';
        valid = false;
    } else {
        phoneError.textContent = '';
    }

    // Session validation
    const session = document.getElementById('session');
    const sessionError = document.getElementById('sessionError');
    if (session.value === '') {
        sessionError.textContent = 'Please select a session.';
        valid = false;
    } else {
        sessionError.textContent = '';
    }

    // Success message
    if (valid) {
        document.getElementById('regForm').style.display = 'none';
        document.getElementById('successMessage').style.display = 'block';
    }
});