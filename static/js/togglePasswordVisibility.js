function initClick() {
    const togglePasswordButton = document.querySelector('#password-visibility');
    togglePasswordButton.addEventListener('click', togglePasswordVisibility);
}

function togglePasswordVisibility(clickEvent) {
    const toggleVisibilityButton = clickEvent.target;
    const passwordInput = document.querySelector('#password-input');
    const confirmPasswordInput = document.querySelector('#password2-input');

    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        if (confirmPasswordInput) {
            confirmPasswordInput.type = 'text';
        }
        toggleVisibilityButton.classList.add('fa-eye');
        toggleVisibilityButton.classList.remove('fa-eye-slash');
    } else {
        passwordInput.type = 'password';
        if (confirmPasswordInput) {
            confirmPasswordInput.type = 'password';
        }
        toggleVisibilityButton.classList.add('fa-eye-slash');
        toggleVisibilityButton.classList.remove('fa-eye');
    }
}

initClick();