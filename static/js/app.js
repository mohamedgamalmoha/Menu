const swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    spaceBetween: 60,
    loop: true,
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
    },
    navigation: {
        nextEl: ".next",
        prevEl: ".prev",
    },
    breakpoints: {
        640: {
            slidesPerView: 2,
            spaceBetween: 20,
        },
        768: {
            slidesPerView: 4,
            spaceBetween: 40,
        },
        1024: {
            slidesPerView: 6,
            spaceBetween: 50,
        },
    },
});

const navOpener = document.getElementById("toggler")
const navCloser = document.querySelectorAll(".navCloser")
const mobNav = document.getElementById("mobNav")
const mobileNav = () => {
    navOpener.addEventListener('click', () => {
        mobNav.classList.toggle('mobileNavCloser')
        document.body.style.overflowY = 'hidden';
    })

    for (let i = 0; i < navCloser.length; i++) {
        navCloser[i].addEventListener('click', () => {
            mobNav.classList.toggle('mobileNavCloser');
            document.body.style.overflowY = 'auto';
        })

    }

}

mobileNav()