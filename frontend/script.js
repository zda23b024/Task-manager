// Toggle About Me visibility
function toggleAbout() {
    const about = document.getElementById("aboutMe");
    about.style.display = (about.style.display === "none") ? "block" : "none";
}

// Highlight Skills table briefly
function highlightSkills() {
    const table = document.getElementById("skillsTable");
    table.style.backgroundColor = "#a8e6cf"; // light green
    setTimeout(() => {
        table.style.backgroundColor = "";
    }, 1000);
}

// Toggle Dark Mode / Light Mode
function toggleTheme() {
    const body = document.body;
    if (body.style.backgroundColor === "white" || body.style.backgroundColor === "") {
        body.style.backgroundColor = "#2c3e50"; // dark background
        body.style.color = "black";              // dark text
    } else {
        body.style.backgroundColor = "white";   // light background
        body.style.color = "black";             // text remains dark
    }
}


// Click counter
let counter = 0;
function countClicks() {
    counter++;
    document.getElementById("clickCount").textContent = "Clicks: " + counter;
}

// Contact form validation
const form = document.getElementById("contactForm");
form.addEventListener("submit", function(event) {
    event.preventDefault();
    const name = form.querySelector('input[type="text"]').value;
    const email = form.querySelector('input[type="email"]').value;
    if (name === "" || email === "") {
        alert("Please fill in all fields!");
    } else {
        alert("Thank you, " + name + "! Message sent.");
        form.reset();
    }
});
