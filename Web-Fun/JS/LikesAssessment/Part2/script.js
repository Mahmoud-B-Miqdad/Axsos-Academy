let likes = [9, 12, 9];

let likeDisplayElements = document.querySelectorAll(".like-count");

let likeButtons = document.querySelectorAll(".like-btn");

likeButtons.forEach((btn, index) => {
    btn.onclick = function() {
        likes[index]++;
        
        likeDisplayElements[index].innerText = likes[index];
    };
});