jQuery(document).ready(function(){

    $(".card").click(function() {
        var nodo = $(this).attr("id");
        console.log(nodo);
        $(".cards").append($("#" + nodo));
    });

});
