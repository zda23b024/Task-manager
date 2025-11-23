// Toggle About Me visibility
function toggleAbout() {
    const about = document.getElementById("aboutMe");
    if (about.style.display === "none") {
        about.style.display = "block";
    } else {
        about.style.display = "none";
    }
}

// Highlight Skills table briefly
function highlightSkills() {
    const table = document.getElementById("skillsTable");
    table.style.backgroundColor = "#a8e6cf"; // light green
    setTimeout(() => {
        table.style.backgroundColor = "";
    }, 1000);
}
