document.getElementById("registration-form").addEventListener("submit", validationStep);
document.getElementById("InputEmail").addEventListener("change", emailValidationStep);
document.getElementById("InputPassword").addEventListener("change", passwordValidationStep);

function emailValidationStep(event) {
    event.preventDefault();

    emailField = document.getElementById("InputEmail");
    let emailCheck = emailValidation(emailField);
}

/**
 * Gets email from email field
 * Checks if it is empty and, if not,
 * if email field passes regex.
 */
function emailValidation(email) {
    let regEmail = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/;
    if (email.value.trim() === ""){
        document.getElementById("email-validation-field").innerHTML = "Email cannot be empty.";
        document.getElementById("InputEmail").style.border = "2px solid red";
    } else if (!regEmail.test(email.value)){
        document.getElementById("email-validation-field").innerHTML = "Please provide a valid email.";
        document.getElementById("InputEmail").style.border = "2px solid red";
    } else if (regEmail.test(email.value)){
        document.getElementById("email-validation-field").innerHTML = " ";
        document.getElementById("InputEmail").style.border = "2px solid green";
    }
}

function passwordValidationStep(event) {
    event.preventDefault();

    passwordField = document.getElementById("InputPassword");
    let emailCheck = emailValidation(emailField);
}
/**
 * Gets password from password field
 * Checks if it is empty and, if not,
 * if password field passes regex.
 */
function passwordValidation(password) {
    let regPass = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/;
    if (email.value.trim() === ""){
        document.getElementById("password-validation-field").innerHTML = "Password cannot be empty.";
        document.getElementById("InputPassword").style.border = "2px solid red";
    } else if (!regPass.test(email.value)){
        document.getElementById("password-validation-field").innerHTML = "Password must have more than 8 letters and at least 1 number. Acceptable: a-z, A-Z, 0-9";
        document.getElementById("InputPassword").style.border = "2px solid red";
    } else if (regPass.test(email.value)){
        document.getElementById("password-validation-field").innerHTML = " ";
        document.getElementById("InputPassword").style.border = "2px solid green";
    }
}

const showEdit = () => {
    let form = document.getElementById('edit-profile-form');
    form.classList.toggle('hide');
}


