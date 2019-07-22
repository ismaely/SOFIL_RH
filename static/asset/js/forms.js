/**
 * @File   : forms.js
 * @Author : Gunza Ismael (7ilipe@gmail.com)
 * @Link   : 
 * @Date   : 27/06/2019, 01:26:48
 */

$(document).ready(function () {
// variavel

    // MASCAR
$('.mask-phone').mask('000-000-000');
$('.mask-bi').mask('000000000SS000');


});

// para meter as letras maiusculas
$(function() {
    $('.maiuscula').keyup(function() {
       this.value = this.value.toLocaleUpperCase();
    });
});