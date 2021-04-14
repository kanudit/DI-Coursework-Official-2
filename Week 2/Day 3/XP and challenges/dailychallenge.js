//step 1
let asterikLine = "*";


do {
    console.log(asterikLine);
    asterikLine = asterikLine + " *";

}
while (asterikLine.length < 13);


/* This is what I did by myself. I really had trouble with this day

for (let asterikRow = 0; asterikRow < 6; asterikRow++) {
    //you need to create a starting point for my column
    nestedAsterikLine = "";

    for (let asterikColumn = 0; asterikRow < 6; asterikColumn++) {
        nestedAsterikLine += nestedAsterik;
    }
    console.log(nestedAsterikLine);
}*/


//A roommate helped me with this. step 2
for (i = 1; i <= 6; i++) {
    let asterikLine = "";


    for (j = 1; j <= i; j++) {
        asterikLine += "*";
    }
    console.log(asterikLine);
}