function loadingAlert() {
    alert("Loading weather report...");
}

function acceptCookies() {
    var cookieBar = document.querySelector("#cookie-bar");
    cookieBar.remove();
}

function convertTemp(element) {
    var allTemps = document.querySelectorAll(".high, .low");
    
    for(var i=0; i < allTemps.length; i++) {
        var currentTemp = parseInt(allTemps[i].innerText);
        
        if(element.value === "f") {
            var result = Math.round((currentTemp * 9/5) + 32);
            allTemps[i].innerText = result + "°";
        } else {
            var result = Math.round((currentTemp - 32) * 5/9);
            allTemps[i].innerText = result + "°";
        }
    }
}