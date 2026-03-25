// 1. Always Hungry

function alwaysHungry(arr) {
    let foodFound = false;

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === "food") {
            console.log("yummy");
            foodFound = true;
        }
    }

    if (!foodFound) {
        console.log("I'm hungry");
    }
}

alwaysHungry([3.14, "food", "pie", true, "food"]); 

alwaysHungry([4, 1, 5, 7, 2]); 

//*********************************************************

// 2. High Pass Filter

function highPass(arr, cutoff) {
    var filteredArr = [];
    
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > cutoff) {
            filteredArr.push(arr[i]);
        }
    }
    
    return filteredArr;
}

var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result); 


//*********************************************************

// 3. Better than average

function betterThanAverage(arr) {
    var sum = 0;
    for (var i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    
    var average = sum / arr.length;
    
    var count = 0;
    for (var j = 0; j < arr.length; j++) {
        if (arr[j] > average) {
            count++;
        }
    }
    
    return count;
}

var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result); 

//*********************************************************

// 4. Array Reverse

function reverse(arr) {
    for (var i = 0; i < Math.floor(arr.length / 2); i++) {
        var temp = arr[i];
        
        arr[i] = arr[arr.length - 1 - i];
        
        arr[arr.length - 1 - i] = temp;
    }
    
    return arr;
}

var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result); 

//*********************************************************

// 5. Fibonacci Array

function fibonacciArray(n) {
    var fibArr = [0, 1];
    
    while (fibArr.length < n) {
        var prev1 = fibArr[fibArr.length - 1];
        var prev2 = fibArr[fibArr.length - 2];
        
        fibArr.push(prev1 + prev2);
    }
    
    return fibArr;
}

var result = fibonacciArray(10);
console.log(result); 