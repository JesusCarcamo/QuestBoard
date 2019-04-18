jQuery(document).ready(function(){
    if($("#ingresar").delay("slow").is(":visible"))
    {
        $("#match").hide();
        $("#tablero").hide();
        $("#otro").hide();
        $("#salir").hide();
        $("#menu").css("top", "35%");
    }
});

$(function() {
    $("#cuatro").click(function() {
        $("#match").hide();
        $("#tablero").hide();
        $("#otro").hide();
        $("#menu").css("top", "35%");
        $("#salir").hide();
        $("#ingresar").show();
    });
});
