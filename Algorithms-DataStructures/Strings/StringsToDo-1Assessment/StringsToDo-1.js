// 1. Remove Blanks

function removeBlanks(str) {
    return str.split(" ").join("");
}

console.log(removeBlanks(" Pl ayTha tF u nkyM usi c ")); 

console.log(removeBlanks("I can not BELIEVE it's not BUTTER")); 

//************************************************************

// 2. Get Digits

function getDigits(str) {
    let digitsStr = "";

    for (let char of str) {
        if (!isNaN(char)) {
            digitsStr += char;
        }
    }

    return Number(digitsStr);
}

console.log(getDigits("abc8c0d1ngd0j0!8")); 

console.log(getDigits("0s1a3y5w7h9a2t4?6!8?0")); 

//************************************************************

// 3. Acronyms

function acronym(str) {
    let words = str.split(" ");
    let result = "";

    for (let word of words) {
        if (word.length > 0) {
            result += word[0].toUpperCase();
        }
    }

    return result;
}

console.log(acronym(" there's no free lunch - gotta pay yer way. ")); 

console.log(acronym("Live from New York, it's Saturday Night!")); 

//************************************************************

// 4. Count Non-Spaces

function countNonSpaces(str) {
    let count = 0;

    for (let char of str) {
        if (char !== " ") {
            count++;
        }
    }

    return count;
}

console.log(countNonSpaces("Honey pie, you are driving me crazy")); 

console.log(countNonSpaces("Hello world !")); 

//************************************************************

// 5. Remove Shorter Strings

function removeShorterStrings(arr, minLength) {
    let filteredArr = [];

    for (let str of arr) {
        if (str.length >= minLength) {
            filteredArr.push(str);
        }
    }

    return filteredArr;
}

console.log(removeShorterStrings(['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'], 4)); 

console.log(removeShorterStrings(['There', 'is', 'a', 'bug', 'in', 'the', 'system'], 3)); 

