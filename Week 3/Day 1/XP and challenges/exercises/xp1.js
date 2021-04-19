let div = document.getElementsByTagName('div')[0];

//navbar[0] selects the navbar variable in position 1, we are changing the attribute id
div.setAttribute("id", "socialNetworkNavigation");


//working inside out here
//creating the anchor tag
let a = document.createElement("a");
//text of anchor tag
a.innerHTML = "Logout";
//setting the attributes of the anchor tag
a.setAttribute("href", "#");

//my anchor is complete at this point 


//creats the list element
let li = document.createElement("li");
//adding the anchor to the list element
li.appendChild(a);

//selecting the ul
let ul = document.getElementsByTagName("ul")[0];
//adding the li to il
ul.appendChild(li);