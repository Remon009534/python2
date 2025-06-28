const btn = document.querySelector("#btn");

function Function()
{
    document.querySelector('h1').innerHTML = "REMON";
}
let counter = 0;

function count()
{
    let x = counter++;
    document.querySelector('h2').innerHTML = x;
}
function zero()
{
    counter = 0;
    let x = counter;
    document.querySelector('h2').innerHTML = x;
}
function negative()
{
    counter--;
    let x = counter;
    document.querySelector('h2').innerHTML = x;
}

btn.addEventListener("click", myFunction);

function myFunction()
{
    alert("Hello World");
}

var name = window.prompt("Enter your name:- ");

document.getElementById('name2').innerHTML = name;

var header = document.getElementById("header");

header.addEventListener("click", function() {
    alert("You clicked " + header.id);
});

window.open();