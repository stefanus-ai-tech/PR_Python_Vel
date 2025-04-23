// Create a paragraph element
const p = document.createElement("p");
p.textContent = "Hello, world!";
document.body.appendChild(p);

// Create a button element
const button = document.createElement("button");
button.textContent = "Ubah Warna";
document.body.appendChild(button);

// Add an event listener to the button
button.addEventListener("click", () => {
    p.style.color = "red";
});
