const dynamicText = document.querySelector("h1 span");
const words = ["NotesNinja", "Knowledge", "the Future",];

// Variables to track the position and deletion status of the word
let wordIndex = 0;
let charIndex = 0;
let isDeleting = false;

const typeEffect = () => {
    const currentWord = words[wordIndex];
    const currentChar = currentWord.substring(0, charIndex);
    dynamicText.textContent = currentChar;
    dynamicText.classList.add("stop-blinking");

    if (!isDeleting && charIndex < currentWord.length) {
        // If condition is true, type the next character
        charIndex++;
        setTimeout(typeEffect, 200);
    } else if (isDeleting && charIndex > 0) {
        // If condition is true, remove the previous character
        charIndex--;
        setTimeout(typeEffect, 100);
    } else {
        // If word is deleted then switch to the next word
        isDeleting = !isDeleting;
        dynamicText.classList.remove("stop-blinking");
        wordIndex = !isDeleting ? (wordIndex + 1) % words.length : wordIndex;
        setTimeout(typeEffect, 1200);
    }
}

if (window.location.pathname == "/"){
    typeEffect();
}

// Popup
const overlay = document.getElementById("overlay");
const popup = document.getElementById("popup");
const closeBtn = document.getElementById("close-btn");
const body = document.querySelector("body");

// Check if a session cookie is set to determine if the popup should be displayed
const hasSeenPopup = sessionStorage.getItem("hasSeenPopup");

openPop = () => {
        overlay.style.display = "block";
        popup.style.display = "block";
        body.classList.add("blur");
}

if (!hasSeenPopup) {
    openPop();
}

closeBtn.addEventListener("click", function () {
    overlay.style.display = "none";
    popup.style.display = "none";
    body.classList.remove("blur");

    // Set a session cookie to remember that the popup has been seen
    sessionStorage.setItem("hasSeenPopup", true);
});

// JavaScript to handle the hamburger menu toggle
const hamburgerBtn = document.getElementById('hamburger-btn');
const navbar = document.querySelector('.navbar');

hamburgerBtn.addEventListener('click', () => {
    navbar.classList.toggle('active');
});

// Close the navbar when a link is clicked
document.querySelectorAll('.container a').forEach(link => {
    link.addEventListener('click', () => {
        navbar.classList.remove('active');
    });
});

// Close the navbar when clicking outside of it
document.addEventListener('click', (event) => {
    if (!navbar.contains(event.target) && !hamburgerBtn.contains(event.target)) {
        navbar.classList.remove('active');
    }
});
