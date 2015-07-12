$( document ).ready( function() {

    $("#addButton").click( function( event ) {
        event.preventDefault();
        create();
    });

    function create() {
        $.ajax({
            url: "/add",
            type: "POST",
            dataType: "json",
            data: { "title": $("#title").val(), "text": $("#text").val() },
        })

      