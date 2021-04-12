//Exercise 1
let x = 5;
let y = 2;
if (x > y) {
    alert("x is the biggest number");
} else {
    alert("you messed with my code")
};

//Exercise 2 
newDog = "Chihuaha";

console.log(newDog.length);
console.log(newDog.toLowerCase());
console.log(newDog.toUpperCase());

if (newDog == "Chihuaha") {
    "I love Chihuahuas, Mexican food is my favorite";
} else {
    "I prefer cats, Chinese food is better"
};

//Exercise 3 
userEnteredNumber = +prompt("gimme yo digits");
dividedNumber = userEnteredNumber % 2;
console.log(dividedNumber);
if (dividedNumber == 1) {
    alert(userEnteredNumber + " " + "an odd number");
} else {
    alert(userEnteredNumber + " " + "It's an even number");
}

//Exercise 4 
//let whatHappens;
let direction = Forward;

switch (direction) {
    case "forward":
        whatHappens = "you encounter a monster";
        break;

    case "back":
        whatHappens = "you arrived home";
        break;

    case "right":
        whatHappens = "you found a river";
        break;
    case "left":
        whatHappens = "you run into a troll";
        break;


    default:
        whatHappens = "please enter a valid direction";
        break;
}

//Exercise 5

let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];

if (users == undefined) {
    console.log("no one is online.");
}

tallyOfUsersOnline = (users.length);
if (tallyOfUsersOnline == 1) {
    console.log(users[0]);
}
if (tallyOfUsersOnline == 2) {
    console.log(users[0], users[1]);
}
if (tallyOfUsersOnline >= 3) {
    console.log(users[0], users[1], "and",
        tallyOfUsersOnline - 2 + " more users are online!");
}