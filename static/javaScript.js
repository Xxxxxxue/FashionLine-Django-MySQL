/*Function for slider background*/
function SliderCapa() {
    $('.carousel-item').addClass('slidercapa');
    //var elemento = document.getElementById("carousel-home");
    //elemento.className += " slidercapa";
    console.log("hola");
}

/*funciones login y register*/
function register() {
    //conseguir valores
    var usuario = $('#Email').val();
    var password = $('#Password1').val();
    var password1 = $('#Password2').val();

    //comprobaciones
    if(password != password1) {
        $('#span1').text('Las contraseñas no se coinciden');
        return false;
    }
    if(password.length < 4) {
        $('#span1').text('La contraseña debe tener minimo 4 digitos');
        return false;
    }
    //hacer que la conraseña sea protegida  md5js
    /*hex_pwd = hex_md5(password);
    $('#Password1').val(hex_pwd);
    console.log(hex_pwd);*/
    return true;
}
function login() {
    var password = $('#Password1').val();
    if(password.length < 4) {
        $('#span1').text('La contraseña debe tener minimo 4 digitos');
        return false;
    }
    return true;
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

/*Funcion para la apariencia de las detalles de producto, parate descripcion y devolucion*/
function clickDescrip() {
    $('.descripcion').show();
     $('.devolucion').hide();
}
function clickDevolu() {
    $('.descripcion').hide();
     $('.devolucion').show();
}

/*funcion para valoracion media*/
function valoracionMedia() {
    num = $('.valoracion-media').text();
    num = parseFloat(num)
    num = Math.ceil(num);

    for (i=1;i<=num;i++) {
        console.log(i);
        document.getElementById('estrella'+i).style.color = "orange";
    }
}
window.onload = valoracionMedia;
