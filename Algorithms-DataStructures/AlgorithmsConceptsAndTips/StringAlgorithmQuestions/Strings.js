// 1. Reverse a String
function reverseString(str) {
    let reversed = "";
    for (let i = str.length - 1; i >= 0; i--) {
        reversed += str[i];
    }
    return reversed;
}

// 2. Count Vowels
function countVowels(str) {
    let count = 0;
    let lowerStr = str.toLowerCase();
    for (let i = 0; i < lowerStr.length; i++) {
        let char = lowerStr[i];
        if (char === 'a' || char === 'e' || char === 'i' || char === 'o' || char === 'u') {
            count++;
        }
    }
    return count;
}

// 3. Check Palindrome
function isPalindrome(str) {
    let lowerStr = str.toLowerCase();
    let reversed = reverseString(lowerStr); 
    return lowerStr === reversed;
}

// 4. Longest Word in a Sentence
function findLongestWord(sentence) {
    let words = sentence.split(" ");
    let longest = words[0];

    for (let i = 1; i < words.length; i++) {
        if (words[i].length > longest.length) {
            longest = words[i];
        }
    }
    return longest;
}


console.log("1. Reverse 'hello':", reverseString("hello")); // "olleh"

console.log("2. Vowels in 'hello':", countVowels("hello")); // 2

console.log("3. Is 'madam' palindrome?:", isPalindrome("madam")); // true
console.log("3. Is 'hello' palindrome?:", isPalindrome("hello")); // false

console.log("4. Longest word:", findLongestWord("I love solving algorithms")); // "algorithms"