document.getElementById("generateButton").addEventListener("click", function () {
    const baseColor = document.getElementById("baseColor").value;
    const colorScheme = document.getElementById("colorScheme").value;
    const paletteContainer = document.getElementById("paletteContainer");
    paletteContainer.innerHTML = ""; // Clear previous palette
    if (isValidHex(baseColor)) {
        // Make a POST request to the Flask server
        fetch('/generate_palette', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ baseColor, colorScheme }),
        })
        .then(response => response.json())
        .then(palette => displayPalette(palette))
        .catch(error => console.error('Error:', error));
    } else {
        alert("Please enter a valid HEX color code.");
    }
});
function isValidHex(hex) {
    return /^#([0-9A-Fa-f]{3}){1,2}$/.test(hex);
}
function displayPalette(palette) {
    const paletteContainer = document.getElementById("paletteContainer");
    palette.forEach(color => {
        const colorBlock = document.createElement("div");
        colorBlock.className = "color-block";
        colorBlock.style.backgroundColor = color;
        paletteContainer.appendChild(colorBlock);
    });
}
