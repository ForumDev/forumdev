/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */



var x = document.getElementsByClassName("image-portada");
var i;
for (i = 0; i < x.length; i++) {
    if ((i+1) & 1) { // ODD
        x[i].style.cssFloat = "left";
    } else { // EVEN
        x[i].style.cssFloat = "right";
    }

}