$(function() {
    $(".btn").click(function() {
        $(".form-signin").toggleClass("form-signin-left");
        $(".form-signup").toggleClass("form-signup-left");
        $(".frame").toggleClass("frame-long");
        $(".signup-inactive").toggleClass("signup-active");
        $(".signin-active").toggleClass("signin-inactive");
        $(".forgot").toggleClass("forgot-left");
        $(this).removeClass("idle").addClass("active");
    });
});

$(function() {
    $(".btn-signup").click(function() {
        $(".nav").toggleClass("nav-up");
        $(".success").toggleClass("success-left");
        $(".frame").toggleClass("frame-short");
        $(".btn-animate").toggleClass("btn-animate-grow");
        $(".welcome2").toggleClass("welcome-left");
        $(".cover-photo").toggleClass("cover-photo-down");
        $(".profile-photo").toggleClass("profile-photo-down");
        $(".btn-goback").toggleClass("btn-goback-up");
        $(".forgot").toggleClass("forgot-fade");
    });
});

$(function() {
    $(".btn-signin").click(function() {
        $(".btn-animate").toggleClass("btn-animate-grow");
        $(".welcome").toggleClass("welcome-left");
        $(".cover-photo").toggleClass("cover-photo-down");
        $(".frame").toggleClass("frame-short");
        $(".profile-photo").toggleClass("profile-photo-down");
        $(".btn-goback").toggleClass("btn-goback-up");
        $(".forgot").toggleClass("forgot-fade");
    });

});

$(function() {
    $(".btn-goback").click(function() {
        $("#match").show();
        $("#tablero").show();
        $("#perfil").show();
        $("#salir").show();
        $(".social").show();
        $("#menu").css("top", "25%");
        $("#ingresar").hide();
        $(".btn-animate").removeClass("btn-animate-grow");
        $(".welcome").removeClass("welcome-left");
        $(".cover-photo").removeClass("cover-photo-down");
        $(".frame").removeClass("frame-short");
        $(".profile-photo").removeClass("profile-photo-down");
        $(".btn-goback").removeClass("btn-goback-up");
        $(".forgot").removeClass("forgot-fade");
        $(".nav").removeClass("nav-up");
        $(".success").removeClass("success-left");
        $(".welcome2").removeClass("welcome-left");
    });

});
