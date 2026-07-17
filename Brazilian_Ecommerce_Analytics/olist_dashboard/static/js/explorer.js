$(document).ready(function () {

    $("#datasetTable").DataTable({

        pageLength: 10,

        lengthMenu: [10, 25, 50, 100],

        scrollX: true,

        ordering: true,

        searching: true,

        info: true

    });

});