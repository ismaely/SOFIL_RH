/**
 * @File   : mestrado.js
 * @Author : Gunza Ismael (7ilipe@gmail.com)
 * @Link   : 
 * @Date   : 08/11/2019, 20:33:54
 */


var total_curso = $('#total_curso').text();
var total_especialidade = $('#total_especialidade').text();
var total_masculino = $('#total_masculino').text();
var total_femenino = $('#total_femenino').text();
var titulo = $('#titulo').text();
    Highcharts.chart('mestrado_container', {
        chart: {
            type: 'pie',
            options3d: {
                enabled: true,
                alpha: 46,
                beta: 0
            }
        },
        title: {
            text: titulo
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                depth: 35,
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                }
            }
        },

        series: [{
            name: 'Percentagem',
            colorByPoint: true,
            data: [
              {
                name: 'Masculino',
                y: Number(total_masculino),
                sliced: true,
                selected: true
            }, {
                name: 'Feminino',
                y: Number(total_femenino),
                
            }]
        }]

    });

