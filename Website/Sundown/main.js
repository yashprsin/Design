const scroll = new LocomotiveScroll({
    el: document.querySelector('#main'),
    smooth: true
});

let elementjs = document.querySelector(".element-container");
let fixedImage = document.querySelector(".fixed-image");
elementjs.addEventListener("mouseenter",function(){
    fixedImage.style.display = "block"
});
elementjs.addEventListener("mouseleave",function(){
    fixedImage.style.display = "none"
});

let elements = document.querySelectorAll(".element");
// console.log(elements);
elements.forEach(function(cls){
    cls.addEventListener("mouseenter", function(){
        let image = cls.getAttribute("data-image");
        fixedImage.style.backgroundImage = `url(${image})`;
    })
});
function swiperAnimation() {
    var swiper = new Swiper(".mySwiper", {
        slidesPerView: "auto",
        centeredSlides: true,
        spaceBetween: 100,
    });
}