//for (let i = 25; i < 51; i = ++); {} a for..in loop gets the 
//statement1 is the starting point, Statement2 is the ending point; statement 3 is the increment we step by.

//in loops thru and gets the index. Gives us the position of the item 

//of gets the element and loops until .  Gives us the element.  
//i isnot a number- use parse int. I couldve parsed the length.

//exercise1
let colors = ['red', 'green', 'blue'];

for (i in colors) {
    console.log(`My #${parseInt(i)+1} choice is ${colors[i]}`);
}

//exercise2 cant use/ in \with object

let people = ["Greg", "Mary", "Devon", "James"];



if (people.includes("Greg")) {
    people.splice("Greg", 1);
}
//accesses the index of array of people
for (i in people) {
    if (people[i] === "James") {
        people[i] = "Jason"
    }
}
console.log(people);
people.push("גרג");
//people.forEach(element => console.log(element));
let arrayLength = people.length;
for (let i = 0; i < arrayLength; i++) {
    console.log(people[i]);
}

for (i in people) {
    if (people[i] === "Jason") {
        console.log(people[i]); //how do I log the value of i
        break;
    }
}

let peopleCopy = people.slice(1,
    3);
console.log(peopleCopy);

console.log(people.indexOf("Mary"));
console.log(people.indexOf("foo"));

let last = people[-1];
console.log(last); //y is this undefined?


//Exercise 3

let result = "stop";
let i = 0;

do {
    i = +prompt("enter more than 10");
    //checking what number is popping up for debug
    //alert(i);
} while (i < 10);

console.log(result);