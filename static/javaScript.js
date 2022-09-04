/*Function for slider background*/
function SliderCapa() {
    $('.carousel-item').addClass('slidercapa');
    //var elemento = document.getElementById("carousel-home");
    //elemento.className += " slidercapa";
    console.log("hola");
}

function reiniciar() {
    location.reload();
}
/*funciones login y register*/
var timeoutID;
function register() {
    //conseguir valores
    var password = $('#Password1').val();
    var password1 = $('#Password2').val();

    clearTimeout(timeoutID);
    timeoutID = setTimeout(function(){
        //comprobaciones

        if(password != password1) {
            $('#span1').text('Las contraseñas no se coinciden');
            return false;
        }
        if(password.length < 4) {
            $('#span1').text('La contraseña debe tener minimo 4 digitos');
            return false;
        }

        if(password == password1) {
            $('#span1').text('');
            return true;
        }
    },500)

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

/*funcion pasar direccion a modal*/
function diradd() {
    console.log("add direccion")
    document.getElementById('edit-dir').action = "/user/profile/direccion/0";
}
function dirEdit(id,calle,localidad,provincia,pais,cp,elegido) {
    console.log(id);
    document.getElementById('edit-dir').action= "/user/profile/direccion/"+id;
    document.getElementById('calle').value = calle;
    document.getElementById('localidad').value = localidad;
    document.getElementById('provincia').value = provincia;
    document.getElementById('pais').value = pais;
    document.getElementById('cp').value = cp;
    if (elegido=='True'){
        document.getElementById('elegido').checked=elegido;
    }
}
function checkdir() {
    if (document.getElementById('elegido').checked)
        document.getElementById('elegido').value='True';
    else
       document.getElementById('elegido').value='False';
}

/*funcion pasar producto a modal*/
function calPrecio(oferta) {
    precio = document.getElementById('precio').value
    var pactual = precio
    if (oferta >= 1)
        pactual = precio - oferta
    else
        pactual = precio * (1-oferta)
    document.getElementById('pactual').value = pactual
}
function productAdd(sexo,page) {
    document.getElementById('edit-producto').action = "/user/myproduct/edit/"+sexo+"/"+page+"/0"
}

function productEdit(id,nombre,descripcion,referencia,precio,coste,oferta,pactual,iva,cantidad,sexo,page) {
    console.log(id);
    document.getElementById('edit-producto').action= "/user/myproduct/edit/"+sexo+"/"+page+"/"+id;
    document.getElementById('nombre').value = nombre;
    document.getElementById('descripcion').value = descripcion;
    document.getElementById('referencia').value = referencia;
    document.getElementById('coste').value = coste;
    document.getElementById('precio').value = precio;
    document.getElementById('oferta').value = oferta;
    document.getElementById('pactual').value = pactual;
    document.getElementById('iva').value = iva;
    document.getElementById('cantidad').value = cantidad;
    document.getElementById('sex').value = sexo;

}
/*modal diseno*/
function disenoAdd(sexo,page) {
    document.getElementById('edit-diseno').action = "/user/mydisign/edit/"+sexo+"/"+page+"/0"
}

function disenoEdit(id,nombre,descripcion,precio,sexo,page) {
    console.log(id);
    document.getElementById('edit-diseno').action= "/user/mydisign/edit/"+sexo+"/"+page+"/"+id;
    document.getElementById('nombre').value = nombre;
    document.getElementById('descripcion').value = descripcion;
    document.getElementById('precio').value = precio;
    document.getElementById('sex').value = sexo;

}