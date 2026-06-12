document.addEventListener("DOMContentLoaded", () => {
    const switchToSignUp = document.getElementById("switchToSignUp");
    const switchToSignIn = document.getElementById("switchToSignIn");
    const signInBox = document.querySelector(".sign-in-box");
    const signUpBox = document.querySelector(".sign-up-box");
    
    const registerForm = document.getElementById("registerForm");

    // Seamless interface state switching
    switchToSignUp.addEventListener("click", () => {
        signInBox.classList.add("view-hidden");
        signUpBox.classList.remove("view-hidden");
    });

    switchToSignIn.addEventListener("click", () => {
        signUpBox.classList.add("view-hidden");
        signInBox.classList.remove("view-hidden");
    });

    // Presentation utilities for showing and clearing error states
    const applyInputError = (inputNode, feedbackMessage) => {
        const fieldControlBlock = inputNode.parentElement;
        const targetErrorSpan = fieldControlBlock.querySelector(".client-error-text");
        targetErrorSpan.textContent = feedbackMessage;
        inputNode.style.borderColor = "#ef4444";
    };

    const dropInputError = (inputNode) => {
        const fieldControlBlock = inputNode.parentElement;
        const targetErrorSpan = fieldControlBlock.querySelector(".client-error-text");
        targetErrorSpan.textContent = "";
        inputNode.style.borderColor = "#e5e7eb";
    };

    // Strict client-side verification on registration attempts
    registerForm.addEventListener("submit", (event) => {
        let blockSubmission = false;

        const firstName = document.getElementById("first_name");
        const lastName = document.getElementById("last_name");
        const email = document.getElementById("reg_email");
        const birthday = document.getElementById("birthday");
        const password = document.getElementById("reg_password");
        const confirmPassword = document.getElementById("confirm_password");

        // First Name check
        if (firstName.value.trim().length < 2 || !/^[a-zA-Z]+$/.test(firstName.value)) {
            applyInputError(firstName, "Minimum 2 letters, characters only required.");
            blockSubmission = true;
        } else { dropInputError(firstName); }

        // Last Name check
        if (lastName.value.trim().length < 2 || !/^[a-zA-Z]+$/.test(lastName.value)) {
            applyInputError(lastName, "Minimum 2 letters, characters only required.");
            blockSubmission = true;
        } else { dropInputError(lastName); }

        // Format Regex Validation
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
            applyInputError(email, "Please supply a valid structured email address.");
            blockSubmission = true;
        } else { dropInputError(email); }

        // Date of birth & strict 13-year age filter
        if (!birthday.value) {
            applyInputError(birthday, "Date of birth field is mandatory.");
            blockSubmission = true;
        } else {
            const dateParsed = new Date(birthday.value);
            const todayDate = new Date();
            let calculatedAge = todayDate.getFullYear() - dateParsed.getFullYear();
            const monthDiff = todayDate.getMonth() - dateParsed.getMonth();
            
            if (monthDiff < 0 || (monthDiff === 0 && todayDate.getDate() < dateParsed.getDate())) {
                calculatedAge--;
            }
            if (calculatedAge < 13) {
                applyInputError(birthday, "Minimum requirements: Must be at least 13 years old.");
                blockSubmission = true;
            } else { dropInputError(birthday); }
        }

        // Length validation rules
        if (password.value.length < 8) {
            applyInputError(password, "Security rules: Password must span 8+ characters.");
            blockSubmission = true;
        } else { dropInputError(password); }

        // Matching confirmations check
        if (password.value !== confirmPassword.value) {
            applyInputError(confirmPassword, "Confirmation does not match original password.");
            blockSubmission = true;
        } else { dropInputError(confirmPassword); }

        if (blockSubmission) {
            event.preventDefault();
        }
    });

    // Sensei Bonus: Dynamic AJAX uniqueness verification on field blur
    document.getElementById("reg_email").addEventListener("blur", function() {
        const currentEmailInput = this.value;
        if (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(currentEmailInput)) {
            fetch(`/check-email?email=${currentEmailInput}`)
                .then(response => response.json())
                .then(data => {
                    if (data.exists) {
                        applyInputError(this, "This email address is already tied to an account.");
                    } else {
                        dropInputError(this);
                    }
                });
        }
    });
});