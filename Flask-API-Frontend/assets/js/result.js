$(function (){

    var $results = $('#results')

    $.ajax({
        type: 'GET',
        url: 'http://localhost/average',
        success: function(data) {
            $results.append('<li><b>Sem 1:</b> ' + data.average[0] + '</li>');
            $results.append('<li><b>Sem 2:</b> ' + data.average[1] + '</li>');
            $results.append('<li><b>Sem 3:</b> ' + data.average[2] + '</li>');
            $results.append('<li><b>Sem 4:</b> ' + data.average[3] + '</li>');
        }
    })
})
