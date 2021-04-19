let rocks = [{
    rock: "mercury",
    color: "red"
}, {
    rock: "venus",
    color: "green"
}, {
    rock: "earth",
    color: "blue"
}, {
    rock: "mars",
    color: "gray"
}, {
    rock: "jupiter",
    color: "orange"
}, {
    rock: "saturn",
    color: "yellow"
}, {
    rock: "uranus",
    color: "purple"
}, {
    rock: "neptune",
    color: "green"
}, {
    rock: "pluto",
    color: "purple"
}];

console.log(rocks);
//  "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto"];

//input array and then create div for each planet (item in the arra));

function genesis(rocks) {
    for (i in rocks) {
        //creating div
        let div = document.createElement("DIV");
        //assign class, rocks[i](is the item in array) gets the object, .rock + gives the string of rock
        div.className = rocks[i].rock + " planet";
        //ses the the style.backgroundColor to rocks[i] and the string in color
        div.style.backgroundColor = rocks[i].color;
        document.getElementsByClassName("listPlanets")[0].appendChild(div);
    }

}
document.body.onload = genesis(rocks);