// document.getElementById("registration-form").addEventListener("submit", validationStep);
document.getElementById("InputEmail").addEventListener("change", emailValidationStep);
document.getElementById("InputPassword").addEventListener("change", passwordValidationStep);
document.getElementById("inputUserName").addEventListener("change", usernameValidationStep);

function usernameValidationStep(event) {
    event.preventDefault();

    usernameField = document.getElementById("inputUserName");
    let usernameCheck = usernameValidation(usernameField);
}

function usernameValidation(username) {
    let regUser = /^(?=.*[a-z])(?=.*[A-Z]).{5,15}$/;
    if (username.value.trim() === ""){
        document.getElementById("username-validation-field").innerHTML = "Username cannot be empty.";
        document.getElementById("inputUserName").style.border = "2px solid red";
    } else if (!regUser.test(username.value)){
        document.getElementById("username-validation-field").innerHTML = "Username must have between 5-15 letters. Acceptable: a-z, A-Z";
        document.getElementById("inputUserName").style.border = "2px solid red";
    } else if (regUser.test(username.value)){
        document.getElementById("username-validation-field").innerHTML = " ";
        document.getElementById("inputUserName").style.border = "2px solid green";
    }
}

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
    let passwordCheck = passwordValidation(passwordField);
}
/**
 * Gets password from password field
 * Checks if it is empty and, if not,
 * if password field passes regex.
 */
function passwordValidation(password) {
    let regPass = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/;
    if (password.value.trim() === ""){
        document.getElementById("password-validation-field").innerHTML = "Password cannot be empty.";
        document.getElementById("InputPassword").style.border = "2px solid red";
    } else if (!regPass.test(password.value)){
        document.getElementById("password-validation-field").innerHTML = "Password must have more than 8 letters and at least 1 number. Acceptable: a-z, A-Z, 0-9";
        document.getElementById("InputPassword").style.border = "2px solid red";
    } else if (regPass.test(password.value)){
        document.getElementById("password-validation-field").innerHTML = " ";
        document.getElementById("InputPassword").style.border = "2px solid green";
    }
}

// const showEdit = () => {
//     let form = document.getElementById('edit-profile-form');
//     form.classList.toggle('hide');
// }


