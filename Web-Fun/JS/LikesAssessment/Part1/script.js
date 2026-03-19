let count = 3;

function addLike() {
    count++;
    
    const likeElement = document.querySelector("#like-count");
    likeElement.innerText = count;
}