// 1. Display odd numbers from 1 to 20
console.log("--- 1. Odd numbers from 1 to 20 ---");
for (let i = 1; i <= 20; i++) {
    if (i % 2 !== 0) {
        console.log(i);
    }
}

// 2. Decreasing multiples of 3
console.log("\n--- 2. Decreasing multiples of 3 (100 down to 0) ---");
for (let i = 100; i >= 0; i--) {
    if (i % 3 === 0) {
        console.log(i);
    }
}

// 3. Print the given sequence
console.log("\n--- 3. Print the given sequence ---");
for (let i = 4; i >= -3.5; i -= 1.5) {
    console.log(i);
}

// 4. Sigma
console.log("\n--- 4. Sigma (Sum of 1 to 100) ---");
let sigma = 0;
for (let i = 1; i <= 100; i++) {
    sigma += i;
}
console.log("The total sum is:", sigma); 

// 5. Factorial
console.log("\n--- 5. Factorial (Product of 1 to 12) ---");
let product = 1;
for (let i = 1; i <= 12; i++) {
    product *= i;
}
console.log("The final product is:", product); 