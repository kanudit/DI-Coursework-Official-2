//Daily Challenge: Not Bad

let sentence = "The car is not bad, I love it";
//indexof() will give me a number value for where the string starts
let wordNot = sentence.indexOf("not");

let wordBad = sentence.indexOf("bad");


if (wordBad > wordNot) {

    //swaps out strings
    console.log(sentence.replace("not bad", "good"));
}