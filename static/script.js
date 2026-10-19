
document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const fileInput = document.querySelector('input[type="file"]');
    const analyzeButton = document.querySelector(
        'button[type="submit"], input[type="submit"]'
    );

    if (!form || !fileInput) {
        console.warn("Resume upload form or file input not found.");
        return;
    }

    // Show the selected resume filename
    const fileNameDisplay = document.createElement("p");
    fileNameDisplay.id = "selected-file-name";
    fileNameDisplay.style.marginTop = "10px";
    fileNameDisplay.style.fontSize = "14px";
    fileNameDisplay.setAttribute("aria-live", "polite");
    fileInput.insertAdjacentElement("afterend", fileNameDisplay);

    fileInput.setAttribute(
        "accept",
        ".pdf,.docx,application/pdf,application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    );

    fileInput.addEventListener("change", () => {
        const file = fileInput.files[0];

        if (!file) {
            fileNameDisplay.textContent = "";
            return;
        }

        const extension = file.name.split(".").pop().toLowerCase();

        if (!["pdf", "docx"].includes(extension)) {
            fileNameDisplay.textContent =
                "Please select a PDF or DOCX resume.";
            fileNameDisplay.style.color = "red";
            fileInput.value = "";
            return;
        }

        fileNameDisplay.textContent = "Selected file: " + file.name;
        fileNameDisplay.style.color = "green";
    });

    // Validate before submitting the resume
    form.addEventListener("submit", (event) => {
        const file = fileInput.files[0];

        if (!file) {
            event.preventDefault();
            alert("Please choose your resume file first.");
            return;
        }

        const extension = file.name.split(".").pop().toLowerCase();

        if (!["pdf", "docx"].includes(extension)) {
            event.preventDefault();
            alert("Only PDF and DOCX files are supported.");
            return;
        }

        if (analyzeButton) {
            analyzeButton.disabled = true;

            if (analyzeButton.tagName === "BUTTON") {
                analyzeButton.textContent = "Analyzing Resume...";
            } else {
                analyzeButton.value = "Analyzing Resume...";
            }
        }
    });
});
