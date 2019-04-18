jQuery(document).ready(function(){

    $(".card").click(function() {
        var nodo = $(this).attr("id");
        $(".cards").append($("#" + nodo));
    });

});
