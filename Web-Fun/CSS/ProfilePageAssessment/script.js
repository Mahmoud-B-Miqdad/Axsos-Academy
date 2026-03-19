const userName = document.querySelector("#user-name");
const userImge = document.querySelector("#user-img");
const userCity = document.querySelector("#user-city");
const editBtn = document.querySelector(".edit-link");
const requestCount = document.querySelector("#request-count");
const connectionCount = document.querySelector("#connection-count");

editBtn.addEventListener("click", function() {
    userName.innerText = "Shatha Bast"; 
    userCity.innerText = "Ramallah - west bank"; 
    userImge.src = "./imgs/Shatha Bast.jpg";
});

function acceptRequest(element) {
    const listItem = element.closest(".list-item");
    listItem.remove();

    let currentRequests = parseInt(requestCount.innerText);
    requestCount.innerText = currentRequests - 1;

    let currentConnections = parseInt(connectionCount.innerText);
    connectionCount.innerText = currentConnections + 1 + "+";
}

function ignoreRequest(element) {
    const listItem = element.closest(".list-item");
    listItem.remove();

    let currentRequests = parseInt(requestCount.innerText);
    requestCount.innerText = currentRequests - 1;
}

document.querySelectorAll(".btn-circle").forEach(button => {
    button.addEventListener("click", function() {
        if (this.innerText === "✔") {
            acceptRequest(this);
        } else if (this.innerText === "✖") {
            ignoreRequest(this);
        }
    });
});