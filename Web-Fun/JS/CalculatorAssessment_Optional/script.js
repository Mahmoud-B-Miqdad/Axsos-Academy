let displayDiv = document.querySelector("#display");

let currentNumber = "";   
let previousNumber = "";  
let operator = "";        

function press(num) {
    currentNumber += num;
    displayDiv.textContent = currentNumber;
}

function clr() {
    currentNumber = "";
    previousNumber = "";
    operator = "";
    displayDiv.textContent = "0";
}

function setOP(op) {
    if (currentNumber === "") return; 
    operator = op;
    previousNumber = currentNumber;
    currentNumber = "";
}

function calculate() {
    let result;
    const num1 = parseFloat(previousNumber);
    const num2 = parseFloat(currentNumber);

    if (isNaN(num1) || isNaN(num2)) return;

    switch (operator) {
        case "+":
            result = num1 + num2;
            break;
        case "-":
            result = num1 - num2; 
            break;
        case "*":
            result = num1 * num2; 
            break;
        case "/":
            if (num2 === 0) {
                displayDiv.textContent = "Error";
                return;
            }
            result = num1 / num2;
            break; 
        default:
            return;
    }

    displayDiv.textContent = result;
    currentNumber = result.toString(); 
    operator = "";
}