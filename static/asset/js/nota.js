/**
 * @File   : nota.js
 * @Author : Gunza Ismael (7ilipe@gmail.com)
 * @Link   : 
 * @Date   : 17/07/2019, 19:38:52
 */

$(function () {

    /**fazer uma busca sem fazer a escolher do curso e prencher os modulos  */
    if ($('.ajax_modulo').val() == 0 || $('.ajax_curso').val() != 0){
        var modulo = document.getElementById("id_modulo");
        if ($('.ajax_curso').val() > 0 ){
        $.ajax({
            url:  '/secretaria/recebe_id_curso_ajax/',
            type:  'POST',
            data: JSON.stringify({'id':$('.ajax_curso').val() }),
            dataType:  'json',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
              },
            success:  function (data) {
                var modulo = document.getElementById("id_modulo");
                while (modulo.options.length) {
                    modulo.remove(0);
                  }
                 for (let k = 0; k < data.resposta.length; k++) {
                    var resp = data.resposta[k];
                    var novos_moduloa = new Option(resp[1], resp[0]);
                    modulo.options.add(novos_moduloa)
            }
            },
            error:function(){
                console.log('erro interno')
            }
        });
        if($('.ajax_curso').val() == 1 || $('.ajax_curso').val() == 2){
            $(".ajax_especialidade").attr("disabled", "disabled");
        }else{
            $(".ajax_especialidade").removeAttr("disabled", "disabled");
        }

      }
    }

    /** quando escolher o curso e deve trazer todos modulos*/
    $('.ajax_curso').click(function() {
        var valor_curso = $('.ajax_curso').val();
        $.ajax({
            url:  '/secretaria/recebe_id_curso_ajax/',
            type:  'POST',
            data: JSON.stringify({'id':$('.ajax_curso').val() }),
            dataType:  'json',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
              },
            success:  function (data) {
                var modulo = document.getElementById("id_modulo");
                while (modulo.options.length) {
                    modulo.remove(0);
                  }
                 for (let k = 0; k < data.resposta.length; k++) {
                    var resp = data.resposta[k];
                    var novos_moduloa = new Option(resp[1], resp[0]);
                    modulo.options.add(novos_moduloa)
            }
            },
            error:function(){
                console.log('erro interno')
            }
        });

        if($('.ajax_curso').val() == 1 || $('.ajax_curso').val() == 2){
            $(".ajax_especialidade").attr("disabled", "disabled");
        }else{
            $(".ajax_especialidade").removeAttr("disabled", "disabled");
        }
    
    }); 


    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
      }

});