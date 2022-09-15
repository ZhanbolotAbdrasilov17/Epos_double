document.addEventListener('DOMContentLoaded', function () {
  var parent = document.querySelector('.myBtnContainer');
  parent.addEventListener('click', function (event) {
    // Change active button class
    Array.from(parent.children).forEach(function (currentValue) {
      currentValue.classList.remove('active');
    });
    event.target.classList.add('active');

    // Set slide filter by class name
    Array.from(document.querySelectorAll('.swiper-slide')).forEach(function (
      currentValue
    ) {
      if (
        (event.target.innerText.toLowerCase() ||
          event.target.textContent.toLowerCase()) == 'all'
      ) {
        currentValue.classList.remove('hidden');
      } else {
        if (
          !currentValue.classList.contains(
            event.target.innerText.toLowerCase() ||
              event.target.textContent.toLowerCase()
          )
        ) {
          currentValue.classList.add('hidden');
          // console.log(allSlides)
        } else {
          currentValue.classList.remove('hidden');
        }
      }
      mySwiper.update();
      // mySwiper.updateSize();
      // mySwiper.updateSlides();
      mySwiper.updateSlidesClasses();
      mySwiper.slideTo(0);
    });
  });
});

var mySwiper = new Swiper('.swiper-container', {
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  breakpoints: {
    640: {
      slidesPerView: 1,
      spaceBetween: 0,
    },
    768: {
      slidesPerView: 2,
      spaceBetween: 10,
    },
    1024: {
      slidesPerView: 3,
      spaceBetween: 20,
    },
    1280: {
      slidesPerView: 4,
      spaceBetween: 20,
    },
  },
});

var mySwiper2 = new Swiper('.swiper-container2', {
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  breakpoints: {
    640: {
      slidesPerView: 1,
      spaceBetween: 0,
    },
    768: {
      slidesPerView: 2,
      spaceBetween: 10,
    },
    1024: {
      slidesPerView: 3,
      spaceBetween: 20,
    },
    1280: {
      slidesPerView: 4,
      spaceBetween: 20,
    },
  },
});

var mySwiper2 = new Swiper('.swiper-container3', {
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  breakpoints: {
    640: {
      slidesPerView: 1,
      spaceBetween: 0,
    },
    768: {
      slidesPerView: 2,
      spaceBetween: 10,
    },
    1024: {
      slidesPerView: 3,
      spaceBetween: 20,
    },
    1280: {
      slidesPerView: 4,
      spaceBetween: 20,
    },
  },
});
