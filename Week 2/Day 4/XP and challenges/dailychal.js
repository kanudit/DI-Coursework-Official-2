let sentence = prompt("input a sentence, seperate each word with a comma");
let sentenceArray = sentence.split(",");
console.log(sentenceArray);
//number of items in the array
let sentenceLength = sentenceArray.length;

let longestLength = 0; //0 bc we have no words yet, havent tested 

for (let i = 0; i < sentenceLength; i++) {

    // sentenceArray[i] is the "current" item in the loop
    if (sentenceArray[i].length > longestLength) {
        longestLength = sentenceArray[i].length;
    }
};
let asterisk = "*";


//top line
console.log(asterisk.repeat(longestLength + 4));


//content

let spaces = " ";

for (let word of sentenceArray) {

    console.log("* " + word + spaces.repeat(longestLength - word.length) + " *");
}








//bottom line
console.log(asterisk.repeat(longestLength + 4));