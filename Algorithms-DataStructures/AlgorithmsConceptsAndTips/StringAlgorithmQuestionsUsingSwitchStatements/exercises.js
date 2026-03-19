// 1. Convert a Letter Grade to Feedback
function getGradeFeedback(grade) {
    let upperGrade = grade.toUpperCase();

    switch (upperGrade) {
        case 'A':
            return "Excellent";
        case 'B':
            return "Good job";
        case 'C':
            return "You passed";
        case 'D':
            return "Need improvement";
        case 'F':
            return "Failed";
        default:
            return "Invalid grade";
    }
}

// 2. Count Character Types in a String
function countCharacterTypes(str) {
    let counts = {
        vowels: 0,
        digits: 0,
        spaces: 0,
        others: 0
    };

    let vowelsList = "aeiou";

    for (let i = 0; i < str.length; i++) {
        let char = str[i];
        let lowerChar = char.toLowerCase();

        switch (true) {
            case (char === " "):
                counts.spaces++;
                break;

            case (char >= "0" && char <= "9"):
                counts.digits++;
                break;

            case (vowelsList.indexOf(lowerChar) !== -1):
                counts.vowels++;
                break;

            default:
                counts.others++;
        }
    }

    return counts;
}


console.log("--- Test Question 1 ---");
console.log("Grade B:", getGradeFeedback("B")); // "Good job"
console.log("Grade a:", getGradeFeedback("a")); // "Excellent"
console.log("Grade Z:", getGradeFeedback("Z")); // "Invalid grade"

console.log("\n--- Test Question 2 ---");
console.log(countCharacterTypes("Hi 123!")); 
// { vowels: 1, digits: 3, spaces: 1, others: 3 }