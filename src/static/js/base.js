$(function() {
    $(".icon").click(function() {
        var nodo = $(this).attr("id");

        if(nodo!="uno" && nodo!="cinco" && nodo!="cuatro")
        {
            $(".social").hide();
        }
        else
        {
            $(".social").show();
        }

        if(nodo=="seis" || nodo=="tres")
        {
            if(nodo=="seis")
            {
                $("html, body, .page").css("width", "90%");
            }

            $("body").css("overflow-y", "visible");
        }
        else
        {
            $("body").css("overflow-y", "hidden");
            $("html, body, .page").css("width", "100%");
        }
    });
});

jQuery(document).ready(function(){
    if($("#ingresar").delay("slow").is(":visible"))
    {
        $("#match").hide();
        $("#tablero").hide();
        $("#perfil").hide();
        $("#salir").hide();
        $("#menu").css("top", "35%");
    }
});

$(function() {
    $("#cuatro").click(function() {
        var nodo = $(this).attr("id");
        $("#match").hide();
        $("#tablero").hide();
        $("#perfil").hide();
        $("#menu").css("top", "35%");
        $("#salir").hide();
        $("#ingresar").show();
    });
});
