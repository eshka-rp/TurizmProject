let button3 = document.getElementById("give")
let navig = document.querySelector(".navigation")

button3.addEventListener("click", give_navigation)

function give_navigation() {
    navig.classList.toggle("give_a_navigation")
}