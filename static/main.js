$(document).ready(function(){
            $("#test").click(function(){
              $('#test').addClass("red");
            });
            });
// $( document ).ready( function() {
//     $("#addButton").click(function(event) {
//         event.preventDefault();
//         sample();
//     }
//     function sample(){$("#addButton").click(function(){
//                $('#test').addClass('red');
//             });
    // function create() {
    //     $.ajax({
    //         url: "/add",
    //         type: "POST",
    //         dataType: "json",
    //         data: { "title": $("#title").val()},
    //     })
    //     .done(function(response) {
    //         var $template = "<article class='entry'"+
    //                           "id='"+response.id+"'>"+
    //                           "<a href='/detail/"+response.id+"'"+
    //                           "class='title'>"+
    //                           "<h3>"+response.title+"</h3></a>"+
    //                           "<p class='dateline'>"+response.date+"</p>"
    //         $(".entry").prepend($template);
    //         $('#title').val('');
    //     })

    //     .fail(function(response) {
    //         alert("error");
    //     })
    };


