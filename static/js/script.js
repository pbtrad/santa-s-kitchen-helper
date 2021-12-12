document.getElementById("login-form").addEventListener("change", validationStep);
document.getElementById("login-form").addEventListener("submit", validationStep);

/**
 * Starts the validation for the form
 * @param {Automatically added} event 
 */
function validationStep(event) {
    event.preventDefault();

    let emailField = document.getElementById("InputEmail");
    let firstCheck = emailValidation(emailField);
    let secondCheck = passwordValidation(passwordField)
}

function emailValidation(email) {
    let regEmail = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/;
    if (email.value.trim() === ""){
        document.getElementById("email-validation-message").innerHTML = "Email cannot be empty.";
        document.getElementById("InputEmail").style.border = "2px solid red";
    } else if (!regEmail.test(email.value)){
        document.getElementById("email-validation-message").innerHTML = "Please provide a valid email.";
        document.getElementById("InputEmail").style.border = "2px solid red";
    } else if (regEmail.test(email.value)){
        document.getElementById("email-validation-message").innerHTML = "";
        document.getElementById("InputEmail").style.border = "2px solid green";
    }
}

const showEdit = () => {
    let form = document.getElementById('edit-profile-form');
    form.classList.toggle('hide');
}


