function changeBackground(element) {
    element.style.backgroundColor = "#3b4598";
}

function restoreOrigin(element) {
    element.style.backgroundColor = "#284bf9";
}

const aboutButton = document.querySelector("#about-btn");
const aboutimg = document.querySelector(".about-img");

aboutButton.addEventListener("click", function() {
    if (aboutButton.innerText === "Change Back") {
        aboutButton.innerText = "Make A Change"; 
        aboutimg.src = "/assests/about.jpg";
        return;
    }
    else{
        aboutButton.innerText = "Change Back"; 
        aboutimg.src = "/assests/alt-features.png";
    }
});