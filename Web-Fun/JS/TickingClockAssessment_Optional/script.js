function getSecondsSinceStartOfDay() {
    return new Date().getSeconds() + 
           new Date().getMinutes() * 60 + 
           new Date().getHours() * 3600;
}

const hourHand = document.querySelector("#hour");
const minuteHand = document.querySelector("#minutes");
const secondHand = document.querySelector("#seconds");

setInterval( function() {
    var time = getSecondsSinceStartOfDay();
    
    const secondsDegrees = ((time % 60) * 6) + 180; 
    const minutesDegrees = (( (time / 60) % 60) * 6) + 180;
    const hourDegrees = (( (time / 3600) % 12) * 30) + 180;

    secondHand.style.transform = `rotate(${secondsDegrees}deg)`;
    minuteHand.style.transform = `rotate(${minutesDegrees}deg)`;
    hourHand.style.transform = `rotate(${hourDegrees}deg)`;

}, 1000);