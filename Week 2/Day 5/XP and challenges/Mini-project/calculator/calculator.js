//declaring variable, the first number needs to be stored in a data structure
let firstNum = []
let secondNum;
let operation;

//define the functions.. number(argument from the html)
function number(num) {
    //takes the argument(num) and pushes it to the array firstNum
    firstNum.push(num);
    console.log(firstNum);

}

function operator(op) {
    //setting the secondnum to the joined stringe of firstNum array. Must be turned into a number parse
    secondNum = parseInt(firstNum.join(""))
    //sets the firstNumb to empty so we can add another number
    firstNum = [];
    //op is the argument from operation of the html
    operation = op;
    console.log(operation);
}
//on press of equal button join array of firstNum then check ifs, we are checking for the op of operator
function equal(equal) {
    firstNum = parseInt(firstNum.join(""));
    if (operation === "+") {
        console.log(firstNum + secondNum)
    } else if (operation === "-") {
        console.log(Math.abs(firstNum - secondNum))
    } else if (operation === "*") {
        console.log(firstNum * secondNum)
    } else {
        console.log(firstNum / secondNum)
    }
}