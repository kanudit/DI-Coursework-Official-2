/*let mumAge = function parentsAge(myAge) {

    let mummyAge = myAge * 2.1;
    let dadAge = mummyAge + 5;
    return console.log("my mum is " + mummyAge + " and my dad is " + dadAge);

}


console.log(mumAge);

*/
//no 'breaks' in function. Just a 

//functions thatre stored witin a variable dont need a 'name' because they are invoked in the variable

//let username = prompt("username");
//let password = prompt("password");
/*const userInfo = (username, password) => {
    console.log(username, password);

}

userInfo(username,
    password); */

//methods are actions thatre stored in properties as function definitions




//XP 1 : keyLess Car

function checkDriverAge(userAge = prompt("how old are you?")) {
    if (userAge < 18) {
        return alert("Sorry, you are too young to drive this car. Powering off");
    }
    if (userAge > 18) {
        return alert("You're old enough to drive, powering on. Enjoy the ride!");
    }
    if (userAge = 18) {
        return alert("Congrats on you first year of driving");

    }
}
checkDriverAge();


//XP2 is quarters + dimes + nickels + pennies >= item cost

let quarters = 0.25;
let dimes = 0.10;
let nickels = 0.05;
let pennies = 0.01;
let cost = prompt("how much dud it cos?");
let numQuarters = prompt("how many quarters do you have?");
let numDimes = prompt("how many dimes do you have?");
let numNickels = prompt("how many nickelss do you have?");
let numPennies = prompt("how many pennies do you have?");

let myChange = [quarters * numQuarters, dimes * numDimes, nickels * numNickels, pennies * numPennies];
console.log(myChange);
let pocketChange = (myChange[0] + myChange[1] + myChange[2] + myChange[3]);
console.log(pocketChange);
//for (let i = 0; i < myChange.Length; i++) {}

function haveEnoughMoney(pocketChange) {
    if ((myChange[0] + myChange[1] + myChange[2] + myChange[3]) >= cost) {
        return alert("You have enough");
    } else {
        return alert("Go home broke boi.");
    }
}

haveEnoughMoney();

//xp3

let multipleOf = 23;
let stopAt = 500; //possible to make prompt/input




//declaring and defining the function
let multipleOfTwentyThree = function (multipleOf, stopAt) {

    //setting the inital value of the numberList
    let numberList = "";
    let sum = 0;
    for (let i = 0; i < stopAt; i += multipleOf) {

        //initial value and add i which is 0+multipleOf
        numberList += i + " ";

        sum += i;

    }
    console.log("Outcome: " + numberList + "Sum:" + sum);
}
//call to function
multipleOfTwentyThree(multipleOf, stopAt);

//xp4 //What would parameters be here?


let checkBasket = function () {

    let amazonBasket = {
        glasses: 1,
        books: 2,
        floss: 100
    };
    let answer = prompt("what do you need") in amazonBasket;
    if (answer === true) {
        alert("You have it ")
    } else {
        alert("You don't have it");
    }

}

//call function
checkBasket();





//xp5

let stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry": 1
}

let prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry": 10
}

let shoppingList = ["banana", "orange", "apple"];

let myBill = function () {

    //item must be on stock
    // if item in stock find the price


    //let inStock = shoppingList;
    let billTotal = 0;

    for (let item of shoppingList) {
        if (item in stock) {
            if (stock[item] > 0) {
                let itemPrice = prices[item];
                console.log(item + " " + itemPrice);
                billTotal += itemPrice;
            } else {
                alert(item + " is out of stock");
            }



        } else {
            alert(item + "  we dont sell that");
        }
    }
    console.log("shopping list cost: " + billTotal);
    alert("your total is " + billTotal);


}
myBill();



//xp6



let bill = +prompt("how much was the bill?");
let tipAmount = function (bill) {


    if (bill < 50) {
        tipAmount = bill * 0.2
        alert("your tip has to be " + tipAmount + " making your bill: " + (bill + tipAmount));
    };



    if (bill >= 50 && bill < 200) {
        tipAmount = bill * 0.15;
        alert("your tip has to be " + tipAmount + " making your bill: " + (bill + tipAmount));
    };



    if (bill >= 200) {
        tipAmount = bill * 0.1;
        alert("your tip has to be " + tipAmount + " making your bill: " + (bill + tipAmount));
    };



} //remove commen below
tipAmount(bill)


//xp 7



let hotel_cost = function () {

    let numberOfNights = +prompt("How many nights?");

    // if its NaN or 0 prompt again
    while (numberOfNights <= 0 || isNaN(numberOfNights)) {

        //this is resetting numberOfNights otherwise you'll get stuck in the prompt.
        numberOfNights = +prompt("Please enter a number");
        console.log("number of nights: " + numberOfNights);

    }


    return numberOfNights * 140;

}

//let hotelCost = hotel_cost();




//this will become the argument



//desti will recieve the value of destination
plane_ride_cost = function () {

    let destination = prompt("Where to go?");
    //console.log(typeof destination);
    while (!isNaN(destination || destination === 0)) {
        destination = prompt("try again")
    }

    console.log("Destination: " + destination);

    let london = 183;
    let paris = 220;
    let elsewhere = 300;

    let ticketPrice = 0;
    //the switch sets the ticket price
    switch (destination.toLowerCase()) {
        case "london":

            ticketPrice = london;
            break;
        case "paris":
            ticketPrice = paris;
            break;
        default:
            ticketPrice = elsewhere;

    }
    console.log("ticketPrice to " + destination + " costs: " + ticketPrice);
    return ticketPrice;
}

// let ticketPrice = plane_ride_cost();


let rental_car_cost = function () {
    let carRentDays = +prompt("How many days will you be driving?");


    // if its NaN or 0 prompt again
    while (carRentDays <= 0 || isNaN(carRentDays)) {

        //this is resetting carRentDays otherwise you'll get stuck in the prompt.
        carRentDays = +prompt("Please enter a number");

    }
    console.log("Rental days: " + carRentDays);
    let rentPrice = carRentDays * 40;
    if (carRentDays > 10) {
        console.log("prediscount: " + rentPrice);
        discountedRentPrice = rentPrice * 0.95;
        console.log("Discounted Price: " + discountedRentPrice);
    }
    return rentPrice;

};
//let carCost = rental_car_cost();

let total_vacation_cost = function () {

    let hotelCost = hotel_cost();
    console.log("hotel cost: " + hotelCost);
    let ticketPrice = plane_ride_cost();
    console.log("plane cost: " + ticketPrice);
    let carCost = rental_car_cost();
    console.log("Car cost: " + carCost);

    let costOfVacation = hotelCost + ticketPrice + carCost;

    return costOfVacation;
}
let myVacationCost = total_vacation_cost();
console.log("Total Price: " + myVacationCost);
alert("Total Price: " + myVacationCost);