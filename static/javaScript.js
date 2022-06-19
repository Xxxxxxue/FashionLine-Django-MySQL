/*Function for slider background*/
function SliderCapa() {
    $('.carousel-item').addClass('slidercapa');
    //var elemento = document.getElementById("carousel-home");
    //elemento.className += " slidercapa";
    console.log("hola");
}

/*Function for user navigation*/
var timer;
function BlockUserNav() {
    clearTimeout(timer);
    document.getElementById("navUser").style.display = "block";
    
}
function NoneUserNav() {
    timer = setTimeout(() => {
        document.getElementById("navUser").style.display = "none";
    }, 5000);
}

