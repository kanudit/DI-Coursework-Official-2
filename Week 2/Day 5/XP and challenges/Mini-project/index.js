let start = false;
// let userNumber = ""
let computerNumber = "";

let test = function (userNumber, computerNumber) {

    if (userNumber >= 0 && userNumber < 11 || userNumber != "") {

        if (userNumber > computerNumber) {
            userNumber = prompt("Your number is bigger, guess again");
            return test(userNumber, computerNumber);
        } else if (userNumber < computerNumber) {
            userNumber = prompt("Your number is smaller, guess again");
            return test(userNumber, computerNumber);

        } else if (userNumber == computerNumber) {

            alert("winner");
        } else {
            alert("error")
        }

    } else {
        alert("wrong number, put btw 0 and 10")
    }
}

let playTheGame = function () {
    if (start = confirm('Want to play?')) {
        let userNumber = prompt("put a number btw 1 n 10");
        let computerNumber = Math.round(Math.random() * 10);


        if (userNumber != isNaN(userNumber) && userNumber >= 1 && userNumber <= 10) {
            console.log("Computer's number: " + computerNumber);
            console.log("User's number: " + userNumber);

            test(userNumber, computerNumber);

        } else {
            alert("not a good number,bye")

        }
    } else {
        alert('silly goose')

    }

}