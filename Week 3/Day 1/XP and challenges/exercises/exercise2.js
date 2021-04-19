let firstList = document.getElementsByClassName("list")[0];

let pete = firstList.getElementsByTagName("li")[1];

pete.innerHTML = "Richard";

console.log(pete);


let myName = "Gregory";


let uls = document.getElementsByTagName("ul");
//item is a created variable
console.log(uls);

for (let ul of uls) {
    ul.firstElementChild.innerHTML = myName;
    console.log(ul);
}

//נשרף לי
// let li = document.createElement("li");
let message = "Hello Students";

for (item = 0; item < uls.length; item++) {
    let li = document.createElement("li");

    li.innerText = message;

    console.log(item, uls[item]);
    uls[item].appendChild(li);

}


let secondUl = document.getElementsByTagName("ul")[1];
let innerLi = secondUl.getElementsByTagName("li");
// let sarah = secondUl;

// for (i = 0; i < innerLi.length; i++) 

for (let item of innerLi) {
    if (item.innerText == "Sarah") {

        secondUl.removeChild(item);

        //console.log("poop");

    }
    console.log(item);

    // if (i == "Sarah") {
    //     secondUl[i].removeChild(li);
}





console.log(secondUl.length);