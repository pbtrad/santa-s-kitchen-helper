let registrationForm = document.getElementById("registration-form")
let logInForm = document.getElementById("login-form")

if (logInForm == null) {
    document.getElementById("register-submit").addEventListener("click", submitRegistration);
    document.getElementById("InputEmail").addEventListener("change", emailValidationStep);
    document.getElementById("InputPassword").addEventListener("change", passwordValidationStep);
    document.getElementById("inputUserName").addEventListener("change", usernameValidationStep);
    document.getElementById("InputPassword2").addEventListener("change", sPasswordValidationStep);
} else if (registrationForm == null) {
    document.getElementById("login-submit").addEventListener("click", submitLogin);
    document.getElementById("InputEmail").addEventListener("change", emailValidationStep);
    document.getElementById("InputPassword").addEventListener("change", passwordValidationStep);
}

/**
 * Prevents default behaviour and calls username validation function.
 * @param {Change event} event 
 */
function usernameValidationStep(event) {
    event.preventDefault();

    let usernameField = document.getElementById("inputUserName");
    let usernameCheck = usernameValidation(usernameField);
}

/**
 * Gets username from username field
 * Checks if it is empty and, if not,
 * if username field passes regex.
 */
function usernameValidation(username) {
    let regUser = /^[a-zA-Z]{5,15}$/;
    if (username.value.trim() === ""){
        document.getElementById("username-validation-field").innerHTML = "Username cannot be empty.";
        document.getElementById("inputUserName").style.border = "2px solid red";
    } else if (!regUser.test(username.value)){
        document.getElementById("username-validation-field").innerHTML = "Username must have between 5-15 letters. Acceptable: a-z, A-Z";
        document.getElementById("inputUserName").style.border = "2px solid red";
    } else if (regUser.test(username.value)){
        document.getElementById("username-validation-field").innerHTML = "&nbsp;&nbsp;";
        document.getElementById("inputUserName").style.border = "2px solid green";
        return true;
    }
}

/**
 * Prevents default behaviour and calls email validation function.
 * @param {Change event} event 
 */
function emailValidationStep(event) {
    event.preventDefault();

    let emailField = document.getElementById("InputEmail");
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
        document.getElementById("email-validation-field").innerHTML = "&nbsp;&nbsp;";
        document.getElementById("InputEmail").style.border = "2px solid green";
        return true;
    }
}

/**
 * Prevents default behaviour and calls password validation function.
 * @param {Change event} event 
 */
function passwordValidationStep(event) {
    event.preventDefault();

    let passwordField = document.getElementById("InputPassword");
    let passwordCheck = passwordValidation(passwordField);
}
/**
 * Gets password from password field
 * Checks if it is empty and, if not,
 * if password field passes regex.
 */
function passwordValidation(password) {
    let regPass = /^(?=.*\d)(?=.*[a-zA-Z]).{8,50}$/;
    if (password.value.trim() === ""){
        document.getElementById("password-validation-field").innerHTML = "Password cannot be empty.";
        document.getElementById("InputPassword").style.border = "2px solid red";
    } else if (!regPass.test(password.value)){
        document.getElementById("password-validation-field").innerHTML = "Password must have more than 8 letters and at least 1 number. Acceptable: a-z, A-Z, 0-9";
        document.getElementById("InputPassword").style.border = "2px solid red";
    } else if (regPass.test(password.value)){
        document.getElementById("password-validation-field").innerHTML = "&nbsp;&nbsp;";
        document.getElementById("InputPassword").style.border = "2px solid green";
        return true;
    }
}

/**
 * Prevents default behaviour and calls second password validation function.
 * @param {Change event} event 
 */
function sPasswordValidationStep(event) {
    event.preventDefault();

    let fPassword = document.getElementById("InputPassword");
    let sPassword = document.getElementById("InputPassword2");
    let sPasswordCheck = sPasswordValidation(fPassword, sPassword);
}

/**
 * Gets second password from matching field
 * Checks if it is empty and, if not,
 * if second password matches first.
 */
function sPasswordValidation(password, check) {
    if (check.value.trim() === ""){
        document.getElementById("password-repeat-validation-field").innerHTML = "Password cannot be empty.";
        document.getElementById("InputPassword2").style.border = "2px solid red";
    } else if (password.value != check.value){
        document.getElementById("password-repeat-validation-field").innerHTML = "Passwords do not match.";
        document.getElementById("InputPassword2").style.border = "2px solid red";
    } else if (password.value == check.value){
        document.getElementById("password-repeat-validation-field").innerHTML = "&nbsp;&nbsp;";
        document.getElementById("InputPassword2").style.border = "2px solid green";
        return true;
    }
}

function submitRegistration(event) {
    event.preventDefault();
    let usernameField = document.getElementById("inputUserName");
    let emailField = document.getElementById("InputEmail");
    let passwordField = document.getElementById("InputPassword");
    let sPassword = document.getElementById("InputPassword2");
    let usernameCheck = usernameValidation(usernameField);
    let emailCheck = emailValidation(emailField);
    let passwordCheck = passwordValidation(passwordField);
    let sPasswordCheck = sPasswordValidation(passwordField, sPassword);

    if (usernameCheck == true && emailCheck == true && passwordCheck == true && sPasswordCheck == true) {
        document.getElementById("registration-form").submit()
    }
}

function submitLogin(event) {
    event.preventDefault();
    let emailField = document.getElementById("InputEmail");
    let passwordField = document.getElementById("InputPassword");
    let emailCheck = emailValidation(emailField);
    let passwordCheck = passwordValidation(passwordField);

    if (emailCheck == true && passwordCheck == true) {
        document.getElementById("login-form").submit();
    }
}