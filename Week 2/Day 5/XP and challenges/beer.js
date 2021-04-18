//how many bottle on the wall do you have, 99. 99 is the only acceptable number.
let start = +prompt("how many bottles to get crunk?");
//subtrahend is the number we subtract by
let subtrahend = 1;

//first line stanza of song
console.log(start + " bottles of beer on the wall");
console.log(start + " bottles of beer on the wall");
console.log("Take " + subtrahend + " down, pass it around");

//loop for the song
let bottles = start - 1;
// console.log(start + " bottles of beer on the wall")
if (bottles > bottles - 1)
    do {
        console.log(bottles + " bottles of beer on the wall");
        console.log(bottles + " bottles of beer on the wall");
        console.log(bottles + " bottles of beer ");
        //bottles on the wall and bottle coming down are not related
        bottles--;
        subtrahend++;
        console.log("Take " + subtrahend + " down, pass it around");

    }
    //stop condition
    while (bottles > 0);
console.log("walk around,cant hear a sound, now its time to lay on the ground");