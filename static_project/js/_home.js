$(document).ready(function(){

    // banner owl carousel
    $('#banner-area .owl-carousel').owlCarousel({
        rtl:true,
        loop:true,
        nav:true,
        items:1,
        autoplay:true,
        smartspeed:1200,
    
    })


    // emergency owl carousel
    $("#Emergency .owl-carousel").owlCarousel({
        loop: true,
        nav: true,
        rtl: true,
        dots: false,
        responsive : {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1000 : {
                items: 3
            },
            1400 : {
                items: 4
            },

        }
    });

});