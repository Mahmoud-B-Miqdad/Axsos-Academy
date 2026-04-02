// 1
function changeBackground(element) {
    element.style.backgroundColor = "#3b4598";
}

function restoreOrigin(element) {
    element.style.backgroundColor = "#284bf9";
}


// 2
const aboutButton = document.querySelector("#about-btn");
const aboutimg = document.querySelector(".about-img");
const aboutParagraph = document.querySelector("#about-parag");
const aboutTitle = document.querySelector("#about-title");

aboutButton.addEventListener("click", function() {
    if (aboutButton.innerText === "Change Back") {
        aboutButton.innerText = "Make A Change"; 
        aboutimg.src = "./assests/about.jpg";
        aboutTitle.textContent = "Who we are";
        aboutParagraph.textContent = "We are a forward-thinking company dedicated toproviding innovative solutions that fuel business growth. With a focus on modern technologies and strategic insights, we help businesses streamline their operations, enhance customer experiences, and scale efficiently. Whether you're looking to improve your digital presence, optimize processes, or drive new revenue streams"
        return;
    }
    else{
        aboutButton.innerText = "Change Back"; 
        aboutimg.src = "./assests/alt-features.png";
        aboutTitle.textContent = "What we do";
        aboutParagraph.textContent = "At our company, innovation drives everything we do. We specialize in leveraging cutting-edge technologies and strategic expertise to empower businesses to grow smarter and faster. From enhancing digital experiences and optimizing internal workflows to unlocking new revenue opportunities"
    }
});



// 3
function addService(element) {
    const cardContainer = document.querySelector(".card-container");
    const newCard = document.createElement("div");
    newCard.classList.add("card");
    const newImg = document.createElement("img");
    newImg.src = "./assests/features.png";
    newImg.alt = "new service image";
    const newParagraph = document.createElement("p");
    newParagraph.textContent = "Our new service offers cutting-edge solutions to help your business thrive in the digital age. With a focus on innovation and customer satisfaction, we provide tailored strategies that drive growth and success.";
    
    newCard.appendChild(newImg);
    newCard.appendChild(newParagraph);
    cardContainer.appendChild(newCard);

    cardContainer.style.justifyContent = "flex-start";
}
