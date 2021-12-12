document.getElementById("FORMIDHERE").addEventListener("submit", validationStep);
document.getElementById("EMAILFIELDIDHERE").addEventListener("change", emailValidation);
document.getElementById("PASSWORDFIELDIDHERE").addEventListener("change", passwordValidation);

/**
 * Gets email from email field
 * Checks if it is empty and, if not,
 * if email field passes regex.
 */
function emailValidation() {
    email = document.getElementById("EMAILFIELDIDHERE");
    let regEmail = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/;
    if (email.value.trim() === ""){
        document.getElementById("email-validation-message").innerHTML = "Email cannot be empty.";
        document.getElementById("EMAILFIELDIDHERE").style.border = "2px solid red";
    } else if (!regEmail.test(email.value)){
        document.getElementById("email-validation-message").innerHTML = "Please provide a valid email.";
        document.getElementById("EMAILFIELDIDHERE").style.border = "2px solid red";
    } else if (regEmail.test(email.value)){
        document.getElementById("email-validation-message").innerHTML = " ";
        document.getElementById("EMAILFIELDIDHERE").style.border = "2px solid green";
    }
}

/**
 * Gets password from password field
 * Checks if it is empty and, if not,
 * if password field passes regex.
 */
function passwordValidation(password) {
    password = document.getElementById("");
    let regPass = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/;
    if (email.value.trim() === ""){
        document.getElementById("pass-validation-message").innerHTML = "Password cannot be empty.";
        document.getElementById("").style.border = "2px solid red";
    } else if (!regPass.test(email.value)){
        document.getElementById("pass-validation-message").innerHTML = "Password must have more than 8 letters and at least 1 number. Acceptable: a-z, A-Z, 0-9";
        document.getElementById("").style.border = "2px solid red";
    } else if (regPass.test(email.value)){
        document.getElementById("pass-validation-message").innerHTML = " ";
        document.getElementById("InputEmail").style.border = "2px solid green";
    }
}

const showEdit = () => {
    let form = document.getElementById('edit-profile-form');
    form.classList.toggle('hide');
}


