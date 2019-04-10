url = 'http://localhost:8080/api/forecasts';

function log_header_click() {
    $.getJSON(url, function (data) {
    message = data["predictions"];
    insert_predictions(message);
})
}

function insert_predictions(msg) {
    $.each(msg, function (index) {
            p = $('#' + (index + 1));
            p.html(this);
           })
    
}