/*------------------------------------------------------------------

@Author: CodeoStudio
@URL:    http://codeostudio.hr/

[Table of contents]

1. Sticky sidebar
2. Support for touch screens
3. Toggle primary nav
4. Clone stuff to offcanvas
5. Off-canvas menu sub-menus
6. Fit video
7. Magnific lightbox
8. Accordions
9. Tabs
10. Sticky header 

-------------------------------------------------------------------*/   

$(document).ready(function () {
    "use strict";
    // Sticky header 
    function stickyHeader() {
        if($("#cs-main-header").hasClass("cs-header-layout-1")) {
            $(".cs-sticky-sidebar").theiaStickySidebar({
                additionalMarginTop: 85
            });
        }
        if($("#cs-main-header").hasClass("cs-header-layout-2")) {
            $(".cs-sticky-sidebar").theiaStickySidebar({
                additionalMarginTop: 100
            });
        }
    }
    stickyHeader();
    // Accordions
    $(".cs-accordion-group").accordion({
        heightStyle: "content",
        collapsible: true,
        icons: false
    });
    // Popup image
    $(".cs-lightbox-image").magnificPopup({
        type: "image"
    });
    // Popu gallery
    $('.cs-lightbox-gallery').each(function() {
        $(this).magnificPopup({
            delegate: 'a',
            type: 'image',
            gallery: {
              enabled:true
            }
        });
    });
    // Tabs
    $(".cs-tab-group").tabs();
    // Support for touch screens for mobile menu
    $("#cs-primary-nav nav li:has(ul)").doubleTapToGo();
    // Toggle mobile nav
    $(".cs-toggle-mobile-nav, .cs-offcanvas-wrap .close").on("click", function () {
        $(".cs-offcanvas-wrap").toggleClass("active");
        $("body").toggleClass("active-offcanvas");
    });
    // Clone stuff to offcanvas
    $(".cs-menu-links nav").clone().appendTo(".cs-offcanvas-nav");
    $("#cs-site-logo").clone().appendTo(".cs-offcanvas-logo");
    // Off-canvas menu sub-menus
    $(".cs-offcanvas-nav .menu-item-has-children a").on("click", function () {
        event.stopPropagation();
        location.href = this.href;
    });
    $(".cs-offcanvas-nav .menu-item-has-children").on("click", function () {
        $(this).children("ul").toggle();
        $(".cs-offcanvas-nav nav").resize();
        $(this).toggleClass("show-sub-menu");
        return false;
    });
    // Toggle header search
    $(".cs-toggle-search").magnificPopup({
       type: "inline",
        preloader: false
    });
    // Sticky header 
    if($("#cs-main-header").hasClass("cs-header-layout-1")) {
        var initMenuPosition = $("#cs-main-header.cs-header-layout-1 #cs-primary-nav .cs-header-inner").offset().top;
        var headerHeightPx = $("#cs-main-header.cs-header-layout-1 #cs-primary-nav").height();
    }
    if($("#cs-main-header").hasClass("cs-header-layout-2")) {
        var initMenuPosition = $("#cs-main-header.cs-header-layout-2 .cs-header-inner").offset().top;
        var headerHeightPx = $("#cs-main-header.cs-header-layout-2").height();
    }
    $(window).scroll(function () {
        if ($(window).scrollTop() > initMenuPosition){
            $("#cs-main-header.cs-header-layout-1 #cs-primary-nav .cs-header-inner-fill").css("height", headerHeightPx);
            $("#cs-main-header.cs-header-layout-2 .cs-header-inner-fill").css("height", headerHeightPx);
            $("#cs-main-header.cs-header-layout-1 #cs-primary-nav .cs-header-inner-sticky").addClass("active");
            $("#cs-main-header.cs-header-layout-2 .cs-header-inner-sticky").addClass("active");
        } else {
            $("#cs-main-header.cs-header-layout-1 #cs-primary-nav .cs-header-inner-sticky").removeClass("active");
            $("#cs-main-header.cs-header-layout-2 .cs-header-inner-sticky").removeClass("active");
        }
    });
    // Initi Divit slider
    var galleryTop = new Swiper('.cs-divit-slider .gallery-top', {
        nextButton: '.cs-divit-slider .swiper-button-next',
        prevButton: '.cs-divit-slider .swiper-button-prev',
        spaceBetween: 0,
        effect: 'fade'
    });
    var galleryThumbs = new Swiper('.cs-divit-slider .gallery-thumbs', {
        slidesPerView: 3,
        slideToClickedSlide: true,
        centeredSlides: true,
        spaceBetween: 20,
        grabCursor: true
    });
    galleryTop.params.control = galleryThumbs;
    galleryThumbs.params.control = galleryTop;
    // Init big slider
    var swiper = new Swiper('.cs-big-slider .swiper-container', {
        pagination: '.cs-big-slider .swiper-pagination',
        slidesPerView: 1,
        paginationClickable: true,
        spaceBetween: 0,
        effect: 'fade',
        nextButton: '.cs-big-slider .swiper-button-next',
        prevButton: '.cs-big-slider .swiper-button-prev'
    });
    // Init carousel
    function carouselInit(csParam1, csParam2, csParam3, csParam4, csParam5) {
        var swiper = new Swiper('.cs-carousel-slider .swiper-container', {
            pagination: '.cs-carousel-slider .swiper-pagination',
            slidesPerView: csParam1,
            paginationClickable: true,
            spaceBetween: 20,
            nextButton: '.cs-carousel-slider .swiper-button-next',
            prevButton: '.cs-carousel-slider .swiper-button-prev',
            breakpoints: {
                480: {slidesPerView: csParam2},
                767: {slidesPerView: csParam3},
                1024: {slidesPerView: csParam4},
                1200: {slidesPerView: csParam5}
            }
        });
    }
    if ($(".cs-carousel-slider .swiper-container").attr('data-slides-visible') === '2') {
        carouselInit(2, 1, 1, 2, 2);
    } else if ($(".cs-carousel-slider .swiper-container").attr('data-slides-visible') === '3') {
        carouselInit(3, 1, 1, 2, 3);
    } else if ($(".cs-carousel-slider .swiper-container").attr('data-slides-visible') === '4') {
        carouselInit(4, 1, 1, 2, 4);
    }
    
});