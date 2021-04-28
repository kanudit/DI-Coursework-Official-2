let colors = ["red", "yellow", "green", "blue", "orange", "black"]
let buttons = document.getElementById("buttons");
let board = document.getElementById("board");
let divColor;
let bigBoard = document.getElementById("big-board");

for (let i in colors) {
    let div = document.createElement("div");
    div.setAttribute("name", colors[i]);
    div.style.backgroundColor = colors[i];
    div.style.height = "20px";
    div.style.width = "40px";
    buttons.appendChild(div);
    div.addEventListener("click", function (e) {
        divColor = e.target.getAttribute("name");
    })

}

for (i = 0; i < 513; i++) {

    let boardDiv = document.createElement("div");
    boardDiv.style.height = "10px";
    boardDiv.style.width = "10px";
    boardDiv.style.border = "1px solid black";
    board.appendChild(boardDiv);
    boardDiv.addEventListener("mouseover", function (e) {
        //==clicked
        if (e.buttons == 1) {
            boardDiv.style.backgroundColor = divColor;

        }
    })


}

for (i = 0; i < 50; i++) {

    let bigSquare = document.createElement("div");
    bigSquare.style.height = "50px";
    bigSquare.style.width = "50px";
    bigSquare.style.border = "2px solid black";
    bigBoard.appendChild(bigSquare);
    bigBoard.addEventListener("mouseover", function (e) {
        //==clicked
        if (e.buttons == 1) {
            bigBoard.style.backgroundColor = divColor;

        }
    })

}