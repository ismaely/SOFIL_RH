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


    // função que vai pegar todas as especialidade e disciplinas em atraso de cada curso,  atraves do id do curso
    if ($('.ajax_curso_especialidade').val() > 0) {
        //var valor_curso = $('.ajax_curso').val();
        $.ajax({
            url: '/secretaria/recebe_idCurso_retornaEspecialidade_ajax/',
            type: 'POST',
            data: JSON.stringify({ 'id': $('.ajax_curso_especialidade').val() }),
            dataType: 'json',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            },
            success: function (data) {
                var nova_escolhas = document.getElementById("id_especialidade");
                var cadeira = document.getElementById("id_cadeira_atraso_1");
                var cadeira2 = document.getElementById("id_cadeira_atraso_2");
                var cadeira3 = document.getElementById("id_cadeira_atraso_3");
                var cadeira4 = document.getElementById("id_cadeira_atraso_4");
                var cont = 1;
                while (nova_escolhas.options.length) {
                    nova_escolhas.remove(0);
                }
                // especialidade
                for (let k = 0; k < data.resposta.length; k++) {
                    var resp = data.resposta[k];
                    var novos = ""
                    if (cont == 1) {
                        novos = new Option("------", "");
                        nova_escolhas.options.add(novos)
                    }
                    novos = new Option(resp[1], resp[0]);
                    nova_escolhas.options.add(novos)
                    cont = cont + 1;
                }
                while (cadeira.options.length) {
                    cadeira.remove(0);
                }
                // modulos disciplina
                cont = 1;
                for (let k = 0; k < data.modulos.length; k++) {
                    var resp = data.modulos[k];
                    var novos = ""
                    if (cont == 1) {
                        novos = new Option("------", "");
                        cadeira.options.add(novos);
                    }
                    novos = new Option(resp[1], resp[0]);
                    cadeira.options.add(novos);
                    cont = cont + 1;
                }
                while (cadeira2.options.length) {
                    cadeira2.remove(0);

                }
                cont = 1;
                for (let k = 0; k < data.modulos.length; k++) {
                    var resp = data.modulos[k];
                    var novos = ""
                    if (cont == 1) {
                        novos = new Option("------", "");
                        cadeira2.options.add(novos);
                    }
                    novos = new Option(resp[1], resp[0]);
                    cadeira2.options.add(novos);
                    cont = cont + 1;
                }
                while (cadeira3.options.length) {
                    cadeira3.remove(0);

                }
                cont = 1;
                for (let k = 0; k < data.modulos.length; k++) {
                    var resp = data.modulos[k];
                    var novos = ""
                    if (cont == 1) {
                        novos = new Option("------", "");
                        cadeira3.options.add(novos);
                    }
                    novos = new Option(resp[1], resp[0]);
                    cadeira3.options.add(novos);
                    cont = cont + 1;
                }
                while (cadeira4.options.length) {
                    cadeira4.remove(0);

                }
                cont = 1;
                for (let k = 0; k < data.modulos.length; k++) {
                    var resp = data.modulos[k];
                    var novos = ""
                    if (cont == 1) {
                        novos = new Option("------", "");
                        cadeira4.options.add(novos);
                    }
                    novos = new Option(resp[1], resp[0]);
                    cadeira4.options.add(novos);
                    cont = cont + 1;
                }
            },
            error: function () {
                console.log('erro interno')
            }
        });

        if ($('.ajax_curso_especialidade').val() == 1 || $('.ajax_curso_especialidade').val() == 2) {
            $(".ajax_especialidade").attr("disabled", "disabled");
        } else {
            $(".ajax_especialidade").removeAttr("disabled", "disabled");
        }

    }



    //unção que vai receber o id do  ano e vai retorna os semestre
    $('.ajax_ano').click(function () {
        //var valor_curso = $('.ajax_curso').val();
        var nova_escolhas = document.getElementById("id_semestre");
        if($('.ajax_ano').val() > 0){
        $.ajax({
            url: '/secretaria/recebe_ano_retornaSemestre_ajax/',
            type: 'POST',
            data: JSON.stringify({ 'id': $('.ajax_ano').val() }),
            dataType: 'json',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            },
            success: function (data) {
                
                while (nova_escolhas.options.length) {
                    nova_escolhas.remove(0);
                }
                for (let k = 0; k < data.resposta.length; k++) {
                    var resp = data.resposta[k];
                    var novos = new Option(resp[1], resp[0]);
                    nova_escolhas.options.add(novos)
                }
            },
            error: function () {
                console.log('erro interno')
            }
        });
      }else{
        
        while (nova_escolhas.options.length) {
            nova_escolhas.remove(0);
        }
      }

    });


    // matricula ---função que vai pegar todas as especialidade e disciplinas em atraso de cada curso,  atraves do id do curso
    $('.ajax_curso_especialidade').click(function () {
        //var valor_curso = $('.ajax_curso').val();
        $.ajax({
            url: '/secretaria/recebe_idCurso_retornaEspecialidade_ajax/',
            type: 'POST',
            data: JSON.stringify({ 
                'id': $('.ajax_curso_especialidade').val()
                 }),
            dataType: 'json',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            },
            success: function (data) {
                var nova_escolhas = document.getElementById("id_especialidade");
                var ano = document.getElementById("id_ano");
                var cadeira = document.getElementById("id_cadeira_atraso_1");
                var cadeira2 = document.getElementById("id_cadeira_atraso_2");
                var cadeira3 = document.getElementById("id_cadeira_atraso_3");
                var cadeira4 = document.getElementById("id_cadeira_atraso_4");
                var cont = 1;
                while (nova_escolhas.options.length) {
                    nova_escolhas.remove(0);
                }
                // especialidade
                for (let k = 0; k < data.resposta.length; k++) {
                    var resp = data.resposta[k];
                    var novos = ""
                    if (cont == 1) {
                        novos = new Option("------", "");
                        nova_escolhas.options.add(novos)
                    }
                    novos = new Option(resp[1], resp[0]);
                    nova_escolhas.options.add(novos)
                    cont = cont + 1;
                }
                // ANO
                while (ano.options.length) {
                    ano.remove(0);
                }
                cont = 1;
                for (let k = 0; k < data.ano.length; k++) {
                    var resp = data.ano[k];
                    var novos = ""
                    if (cont == 1) {
                        novos = new Option("------", "");
                        ano.options.add(novos);
                    }
                    novos = new Option(resp[1], resp[0]);
                    ano.options.add(novos);
                    cont = cont + 1;
                }


                while (cadeira.options.length) {
                    cadeira.remove(0);
                }
                // modulos disciplina em atraso
                cont = 1;
                for (let k = 0; k < data.modulos.length; k++) {
                    var resp = data.modulos[k];
                    var novos = ""
                    if (cont == 1) {
                        novos = new Option("------", "");
                        cadeira.options.add(novos);
                    }
                    novos = new Option(resp[1], resp[0]);
                    cadeira.options.add(novos);
                    cont = cont + 1;
                }
                while (cadeira2.options.length) {
                    cadeira2.remove(0);

                }
                // modulos disciplina em atraso
                cont = 1;
                for (let k = 0; k < data.modulos.length; k++) {
                    var resp = data.modulos[k];
                    var novos = ""
                    if (cont == 1) {
                        novos = new Option("------", "");
                        cadeira2.options.add(novos);
                    }
                    novos = new Option(resp[1], resp[0]);
                    cadeira2.options.add(novos);
                    cont = cont + 1;
                }
                while (cadeira3.options.length) {
                    cadeira3.remove(0);

                }
                // modulos disciplina em atraso
                cont = 1;
                for (let k = 0; k < data.modulos.length; k++) {
                    var resp = data.modulos[k];
                    var novos = ""
                    if (cont == 1) {
                        novos = new Option("------", "");
                        cadeira3.options.add(novos);
                    }
                    novos = new Option(resp[1], resp[0]);
                    cadeira3.options.add(novos);
                    cont = cont + 1;
                }
                while (cadeira4.options.length) {
                    cadeira4.remove(0);

                }
                // modulos disciplina em atraso
                cont = 1;
                for (let k = 0; k < data.modulos.length; k++) {
                    var resp = data.modulos[k];
                    var novos = ""
                    if (cont == 1) {
                        novos = new Option("------", "");
                        cadeira4.options.add(novos);
                    }
                    novos = new Option(resp[1], resp[0]);
                    cadeira4.options.add(novos);
                    cont = cont + 1;
                }
            },
            error: function () {
                console.log('erro interno')
            }
        });

        if ($('.ajax_curso_especialidade').val() == 1 || $('.ajax_curso_especialidade').val() == 2) {
            var semestre = document.getElementById("id_semestre");
            var ano = document.getElementById("id_ano");
            
            while (semestre.options.length) {
                semestre.remove(0);
            }
            while (ano.options.length) {
                ano.remove(0);
            }
            $(".ajax_especialidade").attr("disabled", "disabled");
            $("#id_ano").attr("disabled", "disabled");
            $("#id_semestre").attr("disabled", "disabled");
        } else {
            $(".ajax_especialidade").removeAttr("disabled", "disabled");
            $("#id_ano").removeAttr("disabled", "disabled");
            $("#id_semestre").removeAttr("disabled", "disabled");
        }

    });


    /** FUNÇÃO QUE VAI BUSCAR OS CURSOS ,ESPECIALIDADE, ANO, SEMESTRE, QDO SELECIONAR O GRAU ACADEMICO, NA LISTA NOMINAL */

    $('.grau_ajax').click(function () {
        //var valor_curso = $('.ajax_curso').val();
        if ($('.grau_ajax').val()){
        $.ajax({
            url: '/secretaria/recebe_grau_academico_ajax/',
            type: 'POST',
            data: JSON.stringify({'id': $('.grau_ajax').val() }),
            dataType: 'json',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            },
            success: function (data) {
                var curso = document.getElementById("id_curso");

                var cont = 1;
                while (curso.options.length) {
                    curso.remove(0);
                }
                for (let k = 0; k < data.cursos.length; k++) {
                    var resp = data.cursos[k];
                    var novos = ""
                    if (cont == 1) {
                        novos = new Option("------", "");
                        curso.options.add(novos)
                    }
                    novos = new Option(resp[1], resp[0]);
                    curso.options.add(novos)
                    cont = cont + 1;
                }

            },
            error: function () {
                console.log('erro interno')
            }
        });

        if ($('.grau_ajax').val() == 1) {
            var especialidade = document.getElementById("id_especialidade");
            while (especialidade.options.length) {
                especialidade.remove(0);
            }
            $("#id_especialidade").attr("disabled", "disabled");
            $("#id_ano").attr("disabled", "disabled");
            $("#id_semestre").attr("disabled", "disabled");
        } else {
            $("#id_especialidade").removeAttr("disabled", "disabled");
            $("#id_ano").removeAttr("disabled", "disabled");
            $("#id_semestre").removeAttr("disabled", "disabled");
        }
     }

    });


/** função que vai buscar o municipoio em função da naturalidade */
    $('.ajax_naturalidade').click(function () {
        $.ajax({
            url: '/secretaria/recebe_naturalidade_retorna_municipio_ajax/',
            type: 'POST',
            data: JSON.stringify({'id': $('.ajax_naturalidade').val() }),
            dataType: 'json',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            },
            success: function (data) {
                var municipio= document.getElementById("id_municipio");

                var cont = 1;
                while (municipio.options.length) {
                    municipio.remove(0);
                }
                for (let k = 0; k < data.muncipios.length; k++) {
                    var resp = data.muncipios[k];
                    var novos = ""
                   
                    novos = new Option(resp[1], resp[0]);
                    municipio.options.add(novos)
                    cont = cont + 1;
                }

            },
            error: function () {
                console.log('erro na busca do municipio')
            }
        });
       

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




// para meter as letras maiusculas
$(function () {
    $('.maiuscula').keyup(function () {
        this.value = this.value.toLocaleUpperCase();
    });
});