// 1. Accessing Elements

let colors = ["red", "blue", "green", "yellow", "purple"];

console.log("First element:", colors[0]); 
console.log("Last element:", colors[colors.length - 1]);

console.log("Element at the second position:", colors[1]);

colors[2] = "orange";
//OR
colors.splice(2, 1, "orange");

console.log("Updated array (Manual):", colors); 

// ************************************************************

// 2. Traversing an Array 

let numbers = [10, 20, 30, 40, 50];

// a. write a program to print each element using a for loop.
console.log("Printing elements in order:");
for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}

// b. Write a for loop to print the elements in reverse order.
console.log("Printing elements in reverse order:");
for (let i = numbers.length - 1; i >= 0; i--) {
    console.log(numbers[i]);
}

// ************************************************************

// 3. Searching in an Array

let numbersToSearch = [5, 10, 15, 20, 25];
let target = 25;
let index = numbersToSearch.indexOf(target);

if (index !== -1) {
    console.log(`Found at position ${index}`);
} else {
    console.log("Not Found");
}

//OR
let isFound = false;

for (var i = 0; i < numbersToSearch.length; i++) {
    if (numbersToSearch[i] === target) {
        console.log(`Found at position ${i} => (Manual)`);
        isFound = true; 
        break; 
    }
}

if (!isFound) {
    console.log("Not Found => (Manual)");
}

// ************************************************************

// 4. Sorting an Array 

// a. Sort array
let scores = [50, 20, 70, 10, 40];

// Ascending order 
scores.sort((a, b) => a - b);
console.log("Ascending:", scores);

// Descending order 
scores.sort((a, b) => b - a);
console.log("Descending:", scores);

// b. Sort names in alphabetical order (ترتيب أبجدي)
let names = ["Shatha", "Sara", "Lina", "Sami", "Dalia"];
names.sort();
console.log("Names Alphabetical:", names);

// ************************************************************

// 5. Inserting Elements

let animals = ["dog", "cat", "rabbit"];

animals.push("elephant");

animals.unshift("lion");

animals.splice(2, 0, "tiger");

console.log("Animals after insertions:", animals);

// ************************************************************

// 6. Deleting Elements 

let fruits = ["apple", "banana", "cherry", "date"];

fruits.shift();

fruits.pop();

let bananaIndex = fruits.indexOf("banana");
if (bananaIndex !== -1) {
    fruits.splice(bananaIndex, 1);
}

console.log("Fruits after deletions:", fruits);

// ************************************************************

// 7. Combining Arrays 

let array1 = [1, 2, 3];
let array2 = [4, 5, 6];

let combinedArray = array1.concat(array2);

console.log("Combined Array:", combinedArray); 

//OR

let result = []; 

for (let i = 0; i < array1.length; i++) {
    result.push(array1[i]);
}

for (let i = 0; i < array2.length; i++) {
    result.push(array2[i]);
}

console.log("Combined Array (Manual):", result);

// ************************************************************

// 8. Splitting an Array 

let items = ["a", "b", "c", "d", "e"];

let firstPart = items.slice(0, 3);

let secondPart = items.slice(3);

console.log("First Part:", firstPart);  
console.log("Second Part:", secondPart); 

//OR

firstPart.length = 0;
secondPart.length = 0;

for (let i = 0; i < items.length; i++) {
    if (i < 3) {
        firstPart.push(items[i]);
    } 
    else {
        secondPart.push(items[i]);
    }
}

console.log("First Part (Manual):", firstPart);   
console.log("Second Part (Manual):", secondPart);

// ************************************************************

// 9. Filtering Elements 

let numbersList = [1, 5, 10, 15, 20, 25, 30];
let filteredNumbers = [];

for (let i = 0; i < numbersList.length; i++) {
    if (numbersList[i] > 15) {
        filteredNumbers.push(numbersList[i]);
    }
}

console.log("Filtered Array (> 15):", filteredNumbers); 

// ************************************************************

// 10. Advanced Challenge

// a. Remove duplicate elements from an array
let inputArr = [1, 2, 2, 2, 3, 4, 4, 5];
let uniqueArr = [];

for (let i = 0; i < inputArr.length; i++) {
    if (uniqueArr.indexOf(inputArr[i]) === -1) {
        uniqueArr.push(inputArr[i]);
    }
}
console.log("Unique Array:", uniqueArr); 


// b. Rotate an array to the right by n positions
let originalArray = [1, 2, 3, 4, 5];
let n = 2;

for (let i = 0; i < n; i++) {
    let lastElement = originalArray.pop(); 
    originalArray.unshift(lastElement);    
}

console.log("Rotated Array:", originalArray); 

// ************************************************************

// Bonus Challenge: Merge two sorted arrays without sort()

let arr1 = [1, 3, 5];
let arr2 = [2, 4, 6];
let merged = [];

i = 0; 
j = 0; 

while (i < arr1.length && j < arr2.length) {
    if (arr1[i] < arr2[j]) {
        merged.push(arr1[i]);
        i++; 
    } else {
        merged.push(arr2[j]);
        j++; 
    }
}

while (i < arr1.length) {
    merged.push(arr1[i]);
    i++;
}

while (j < arr2.length) {
    merged.push(arr2[j]);
    j++;
}

console.log("Final Sorted Merge:", merged); 
