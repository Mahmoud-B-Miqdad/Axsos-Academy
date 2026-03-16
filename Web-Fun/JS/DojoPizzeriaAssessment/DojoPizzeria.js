function pizzaOven(crustType, sauceType, cheeses, toppings) {
    var pizza = {};
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
}

var pizza1 = pizzaOven(
    "deep dish", 
    "traditional", 
    ["mozzarella"], 
    ["pepperoni", "sausage"]);
var pizza2 = pizzaOven(
    "hand tossed",
     "marinara", 
     ["mozzarella", "feta"], 
     ["mushrooms", "olives", "onions"]);

var pizza3 = pizzaOven(
     "thin crust",
     "BBQ sauce", 
     ["cheddar"], 
     ["grilled chicken", "red onions"]);
var pizza4 = pizzaOven(
    "stuffed crust", 
    "white garlic sauce", 
    ["parmesan", "mozzarella"], 
    ["shrimp", "spinach", "roasted garlic"]
);


console.log("Pizza 1:", pizza1);
console.log("Pizza 2:", pizza2);

console.log("Pizza 3:", pizza3);
console.log("Pizza 4:", pizza4);


// ---------------------------------------------------------
// (Bonus Challenge)
function randomPizza() {
    var crusts = 
    ["thin crust", "deep dish", "hand tossed", "stuffed crust"];
    var sauces = 
    ["traditional", "marinara", "white sauce", "barbecue"];
    var cheeseOptions = 
    ["mozzarella", "cheddar", "feta", "parmesan"];
    var toppingOptions = 
    ["pepperoni", "sausage", "mushrooms", "olives", "onions", "peppers", "pineapple"];

    function getRandom(arr) {
        return arr[Math.floor(Math.random() * arr.length)];
    }

    return pizzaOven(
        getRandom(crusts),
        getRandom(sauces),
        [getRandom(cheeseOptions)], 
        [getRandom(toppingOptions), getRandom(toppingOptions)] 
    );
}

console.log("Random Pizza Selection:", randomPizza());