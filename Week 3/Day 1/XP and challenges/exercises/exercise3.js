//make blue
let div = document.getElementsByTagName('div');

console.log(div);

div[0].style.backgroundColor = 'blue';
//remove john
let userList = document.getElementsByTagName('ul');

let users = userList[0].getElementsByTagName('li');

let john = users[0];

console.log(john);

userList[0].removeChild(john);

//add border to pete

let pete = users[0]; //bc john was removed pete moved up in the array
console.log(pete);
pete.style.border = "thick solid #0000FF";

let body = document.body;

console.log(body);
body.style.fontSize = "50px";