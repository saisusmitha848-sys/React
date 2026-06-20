document.addEventListener("DOMContentLoaded", () => {

    console.log("AI Interview Coach Loaded");

    const form = document.querySelector("form");

    if (form) {
        form.addEventListener("submit", (event) => {

            const textareas = document.querySelectorAll("textarea");

            let valid = true;

            textareas.forEach((textarea) => {
                if (textarea.value.trim() === "") {
                    valid = false;
                }
            });

            if (!valid) {
                alert("Please answer all questions before submitting.");
                event.preventDefault();
            } else {
                alert("Interview Submitted Successfully!");
            }
        });
    }

});