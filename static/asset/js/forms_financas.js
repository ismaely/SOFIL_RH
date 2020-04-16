/**
 * @File   : forms_financas.js
 * @Author : Gunza Ismael (7ilipe@gmail.com)
 * @Link   : 
 * @Date   : 02/08/2019, 00:19:57
 */

$(document).ready(function () {


 // quando ja estiver selecionado automaticamente o grau academico no pagamento
 if($('.ajax_grauPagamento').val() > 0){
    if($('.ajax_grauPagamento').val() == 1){
        document.getElementById('mestrado_div').style.display = 'none';
        document.getElementById('posGraduacao_div').style.display = '';

        if($('.ajax_parecela_mestrado').val() > 0){
            swal.fire({ 
                position: 'top-end', 
                type: 'info',
                title: 'Tens que remover a escolha feita antes, na parcela do mestrado!..',
                showConfirmButton: false,
                timer: 5500
             });
            $(".salavar").attr("disabled", "disabled");
        }
        else{
            $(".salavar").removeAttr("disabled", "disabled");
        }

    }
    if($('.ajax_grauPagamento').val() == 2){
        document.getElementById('mestrado_div').style.display = '';
        document.getElementById('posGraduacao_div').style.display = 'none';

        if($('.ajax_parecela_posgraduacao').val() > 0){
            swal.fire({ 
                position: 'top-end', 
                type: 'info',
                title: 'Tens que remover a escolha feita antes, na parcela de Pós-graduação!..',
                showConfirmButton: false,
                timer: 5500
             });
            $(".salavar").attr("disabled", "disabled");
        }
        else{
            $(".salavar").removeAttr("disabled", "disabled");
        }

    }

 }



    // quando selecionar o garu acdemico na formulario de pagamneto
    $('.ajax_grauPagamento').click(function () {

        if($('.ajax_grauPagamento').val() == 1){
            document.getElementById('mestrado_div').style.display = 'none';
            document.getElementById('posGraduacao_div').style.display = '';

            if($('.ajax_parecela_mestrado').val() > 0){
                swal.fire({ 
                    position: 'top-end', 
                    type: 'info',
                    title: 'Tens que remover a escolha feita antes, na parcela do mestrado!..',
                    showConfirmButton: false,
                    timer: 5500
                 });
                $(".salavar").attr("disabled", "disabled");
            }
            else{
                $(".salavar").removeAttr("disabled", "disabled");
            }

        }
        if($('.ajax_grauPagamento').val() == 2){
            document.getElementById('mestrado_div').style.display = '';
            document.getElementById('posGraduacao_div').style.display = 'none';

            if($('.ajax_parecela_posgraduacao').val() > 0){
                swal.fire({ 
                    position: 'top-end', 
                    type: 'info',
                    title: 'Tens que remover a escolha feita antes, na parcela de Pós-graduação!..',
                    showConfirmButton: false,
                    timer: 5500
                 });
                $(".salavar").attr("disabled", "disabled");
            }
            else{
                $(".salavar").removeAttr("disabled", "disabled");
            }

        }

    });

});