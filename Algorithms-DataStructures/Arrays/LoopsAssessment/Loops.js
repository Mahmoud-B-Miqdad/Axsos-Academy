// 1. Print Numbers (1 to 10)
console.log("--- 1. Numbers 1 to 10 ---");
for (let i = 1; i <= 10; i++) {
    console.log(i);
}

// 2. Reverse Counting (10 to 1)
console.log("\n--- 2. Reverse Counting 10 to 1 ---");
for (let i = 10; i >= 1; i--) {
    console.log(i);
}

// 3. Even Numbers (between 1 and 20)
console.log("\n--- 3. Even Numbers 1 to 20 ---");
for (let i = 2; i <= 20; i += 2) {
    console.log(i);
}

// 4. Odd Numbers (between 1 and 20)
console.log("\n--- 4. Odd Numbers 1 to 20 ---");
for (let i = 1; i <= 20; i += 2) {
    console.log(i);
}

// 5. Sum of Numbers (1 to 10)
console.log("\n--- 5. Sum of Numbers 1 to 10 ---");
let sum = 0;
for (let i = 1; i <= 10; i++) {
    sum += i;
}
console.log("Total Sum:", sum);

// 6. FizzBuzz (1 to 30)
console.log("\n--- 6. FizzBuzz 1 to 30 ---");
for (let i = 1; i <= 30; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
        console.log("FizzBuzz");
    } else if (i % 3 === 0) {
        console.log("Fizz");
    } else if (i % 5 === 0) {
        console.log("Buzz");
    } else {
        console.log(i);
    }
}