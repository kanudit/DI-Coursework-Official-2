let wrapper = document.getElementById("wrapper");
console.log(wrapper);
let frame = 0;

function makeCircles() {


    // let circle = document.getElementById('circle');
    if (frame < 44) {
        let circle = document.createElement("div");
        circle.setAttribute("id", "circle");
        circle.style.backgroundImage = "url('https://i.gifer.com/1kW8.gif')";
        wrapper.appendChild(circle);
        console.log(circle);
        frame++;
    }
}

setInterval(makeCircles, 800);