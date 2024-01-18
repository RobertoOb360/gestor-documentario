//Configuración para el datatable
(function () {
    $.extend($.fn.dataTable.defaults, {
        responsive: true,
        dom: '<"row"<"col-12 col-sm-6 col-md-4"B><"col-12 col-sm-6 col-md-8"f>>' +
            '<"row"<"col-12"t>>' +
            '<"row"<"col-12 col-md-6"l><"col-12 col-md-6"p>>',
        buttons: [
            // {
            //     text: 'Nuevo', // Cambiamos el texto del botón
            //     titleAttr: 'Nuevo', // Ponemos un texto al pasar el mouse
            //     className: 'btn btn-secondary', // Agregamos una clase de bootstrap al botón
            //     action: function (e, dt, button, config) {
            //         window.location.href = '/Tarea/TareaAdd'
            //     },
            // },
            {
                extend: 'excelHtml5', // Agregamos el botón de exportación a Excel
                text: 'Exportar', // Cambiamos el texto del botón
                titleAttr: 'Exportar a Excel', // Ponemos un texto al pasar el mouse
                title: 'Registro de Tareas', // Título personalizado para el archivo de Excel
                className: 'btn btn-secondary', // Agregamos una clase de bootstrap al botón
                exportOptions: {
                    columns: function (column, data, node) {
                        return (column !== 11); // Excluye la columna 7 (índice 6)
                    },
                    format: {
                        body: function (data, row, column, node) {
                            if (column === 4) { // Índice de la columna "Hito"
                                return (data == `<i class='fa-solid fa-flag' style="color: green;"></i>`) ? '1' : '0';
                            } else {
                                // Remover etiquetas HTML si existen en los datos
                                return data.replace(/<\/?[^>]+(>|$)/g, "");
                            }
                        }
                    }
                }
            },
            // {
            //     text: 'Reporte', // Cambiamos el texto del botón
            //     titleAttr: 'Reporte', // Ponemos un texto al pasar el mouse
            //     title: 'Reporte de Tareas', // Título personalizado para el archivo de Excel
            //     className: 'btn btn-secondary', // Agregamos una clase de bootstrap al botón
            //     action: function (e, dt, button, config) {
            //         FnGenerarReporte();
            //     },
            // }
        ],
        //order: [[2, 'asc'], [9, 'asc']], // Ordenar por la tercera columna en orden ascendente
        pageLength: 25,
        "language": {
            "lengthMenu": "Mostrar _MENU_ registros por pagina",
            "info": "Mostrando pagina _PAGE_ de _PAGES_",
            "infoEmpty": "No hay registros disponibles",
            "infoFiltered": "(filtrada de _MAX_ registros)",
            "loadingRecords": "Cargando...",
            "processing": "Procesando...",
            "search": "Buscar:",
            "zeroRecords": "No se encontraron registros coincidentes",
            "paginate": {
                "next": "Siguiente",
                "previous": "Anterior"
            },
        },
        lengthMenu: [[10, 25, 50, 100, 500, -1], [10, 25, 50, 100, 500, "Todos"]],
        // columnDefs: [
        //     { targets: [0, 1, 2, 4, 5, 6, 11], className: "text-center" },
        //     { targets: [0, 11], className: "text-center", "width": "3%" },
        //     { targets: [11], orderable: false },
        //     {
        //         targets: [1],
        //         render: function (data, type, row, meta) {
        //             if (data == 'EN ESPERA' || data == 'EN PROGRESO' || data == '25%' || data == '50%' || data == '75%') {
        //                 return '<span class="badge bg-warning" style="background-color: orange !important;">' + data + '</span>';
        //             } else if (data == 'PENDIENTE' || data == 'DESPLAZADA') {
        //                 return '<span class="badge bg-danger">' + data + '</span>';
        //             } else if (data == '100%') {
        //                 return '<span class="badge bg-success">' + data + '</span>';
        //             } else if (data == 'ANULADA' || data == 'NO EMPIEZA') {
        //                 return '<span class="badge bg-warning">' + data + '</span>';
        //             } else {
        //                 return '<span>' + data + '</span>';
        //             }
        //         }
        //     },
        //     {
        //         targets: [6],
        //         render: function (data, type, row, meta) {
        //             if (data == 'ALTA') {
        //                 return '<span class="badge bg-danger">' + data + '</span>';
        //             } else if (data == 'MEDIO') {
        //                 return '<span class="badge bg-warning">' + data + '</span>';
        //             } else if (data == 'BAJA') {
        //                 return '<span class="badge bg-success">' + data + '</span>';
        //             } else {
        //                 return '<span>' + data + '</span>';
        //             }
        //         }
        //     },
        //     {
        //         targets: 4, // Índice de la columna "Hito"
        //         render: function (data, type, row, meta) {
        //             if (type === 'display') {
        //                 if (data == 'true') {
        //                     return `<i class='fa-solid fa-flag' style="color: green;"></i>`;
        //                 } else {
        //                     return `<i class='fa-solid fa-flag' style="color: #D5D8DC;"></i>`;
        //                 }
        //             } else {
        //                 return data;
        //             }
        //         }
        //     }
        // ],
        // drawCallback: function (settings) {
        //     var rows = this.api().rows({ page: 'current' }).nodes();
        //     var counter = this.api().context[0]._iDisplayStart + 1;
        //     $.each(rows, function (index, row) {    // Reemplazando primera columna por numeración
        //         $('td:eq(0)', row).html(counter);
        //         counter++;
        //     });
        // },
    });
})();
var table1 = $('#table_id').DataTable();