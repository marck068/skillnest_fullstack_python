const registerForm = document.querySelector("#registerForm");
const userForm = document.querySelector("#userForm");
const statusMessage = document.querySelector("#statusMessage");

function showMessage(text) {
    if (!statusMessage) return;
    statusMessage.textContent = text;
}

function attachConfirmPassword(form) {
    if (!form) return;
    form.addEventListener("submit", (event) => {
        const password = form.querySelector('[name="password"]')?.value;
        const confirmPassword = form.querySelector('[name="confirmPassword"]')?.value;

        if (password && confirmPassword && password !== confirmPassword) {
            event.preventDefault();
            showMessage("Las contraseñas no coinciden.");
        }
    });
}

attachConfirmPassword(registerForm);
attachConfirmPassword(userForm);
