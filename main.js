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
        .done(function(response) {
            var $newElement = "<article class='entry' "+
                              "id='"+response.id+"'>"+
                              "<a href='/detail/"+response.id+"'"+
                              "class='title'"+
                              "<h3>"+response.title+"</h3></a>"+
                              "<p class='dateline'>"+response.created+"</p>"+
                              "<div class='entry_body'>"+
                              response.markdown+"</div></article>";
            $(".entry").prepend($newElement);
            $('#title').val('');
            $('#text').val('');
        })
