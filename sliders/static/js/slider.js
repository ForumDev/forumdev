/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

var enableSubmit = function(ele,oncl) {
    $(ele).removeAttr("disabled");
}

function highlightNext(ele) {
//    var par = event.target;
//    if (par.disabled === true) { return false; }
    var nav = document.getElementById("slider-nav");
    var children = nav.children;
    for (var i = 0; i < children.length; i++) {
      var li = children[i];
      if (li.className.indexOf("active") > -1) {
          li.className=li.className.replace("active","");
          if (i == children.length-1) {
              children[0].className += ' active';
              break;
          } else {
              children[i+1].className += ' active';
              break;
          }
      }
    }
//    var that = ele;
//    var oncl = ele.onclick;
//    ele.onclick = function(){ return false; };
////    $(ele).attr("disabled", true);
//    setTimeout(function() { enableSubmit(that,oncl) }, 1000);
//    par.disabled = true;
//    window.setTimeout(function(){}, 10000);
//    par.disabled = false;
//    return true;
}


function highlightLast(ele) {
//    var par = event.target;
//    if (par.disabled === true) { return false; }
    var that = ele;
    $(ele).attr("disabled", true);
    setTimeout(function() { enableSubmit(that) }, 1000);
    
    var nav = document.getElementById("slider-nav");
    var children = nav.children;
    for (var i = 0; i < children.length; i++) {
      var li = children[i];
      if (li.className.indexOf("active") > -1) {
          li.className=li.className.replace("active","");
          if (i == 0) {
              children[children.length-1].className += ' active';
              break;
          } else {
              children[i-1].className += ' active';
              break;
          }
      }
    }
//    par.disabled = true;
//    window.setTimeout(function(){}, 10000);
//    par.disabled = false;
//    return true;
}

jQuery(document).ready(function($) {
    $('#slider').bjqs({
        'height' : 350,
        'width' : '99%',
        'responsive' : true,
        'showcontrols' : true,
        'usecaptions' : true,
        'hoverpause' : true,
        'centermarkers': false,
        'showmarkers': false,
        'automatic': false,
        'nexttext': '<div id="slide-next" onClick="highlightNext(this);">Next</div>',
        'prevtext': '<div id="slide-prev" onClick="highlightLast(this);">Prev</div>'
        
    });
});