const burger = document.getElementById('burger');
const navLinks = document.querySelector('.custom-header-fixed');

burger.addEventListener('click', () => {
  navLinks.classList.toggle('active');
});
