$(document).ready(function() {
    $('#sub_form').submit(function(event){
        event.preventDefault()
        form = $("#sub_form")

        $.ajax({
            'url':'/ajax/newsletter/',
            'type': 'POST',
            'data': form.serialize(),
            'dataType': 'json',
            'success':function(data){
                alert(data['success'])
            }
        })// end of ajax method
        $('#id_your_name').val('')
        $('#id_email').val('')
    })//end of submit event
})//end of document ready function