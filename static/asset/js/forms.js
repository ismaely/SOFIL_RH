/**
 * @File   : forms.js
 * @Author : Gunza Ismael (7ilipe@gmail.com)
 * @Link   : 
 * @Date   : 27/06/2019, 01:26:48
 */


$('#id_categoria').click(troca_categoria);

if($('#id_escolha_docente_funcionario').val() == "DOCENTE") {
    document.getElementById('cat_docente').style.display = '';
}
if($('#id_escolha_docente_funcionario').val() == "FUNCIONARIO") {
    document.getElementById('cat_funcionario').style.display = '';
}


function troca_categoria (){
    if ($('#id_escolha_docente_funcionario').val() == "DOCENTE") {
         document.getElementById('cat_docente').style.display = '';
         document.getElementById('cat_funcionario').style.display = 'none';
     }
    
      if ($('#id_escolha_docente_funcionario').val() == "FUNCIONARIO") {
           document.getElementById('cat_funcionario').style.display = '';
           document.getElementById('cat_docente').style.display = 'none';
       }

}
