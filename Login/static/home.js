// const sunIcon = document.querySelector('.sun-icon');
// const body = document.querySelector('body');

// sunIcon.addEventListener('click', function() {
//   if (body.classList.contains('light-mode')) {
//     body.classList.remove('light-mode');
//     body.classList.add('dark-mode');
//   } else {
//     body.classList.remove('dark-mode');
//     body.classList.add('light-mode');
//   }
// });
const sunIcon = document.querySelector('.sun-icon');
const body = document.querySelector('body');
const container = document.querySelector('.container');

sunIcon.addEventListener('click', function() {
  if (body.classList.contains('light-mode')) {
    body.classList.remove('light-mode');
    body.classList.add('dark-mode');
    container.classList.remove('light-mode');
    container.classList.add('dark-mode');
  } else {
    body.classList.remove('dark-mode');
    body.classList.add('light-mode');
    container.classList.remove('dark-mode');
    container.classList.add('light-mode');
  }
});

$('.carousel').carousel({
  interval: 5000,
  pause: 'hover',
  wrap: true
});

$('.carousel-control-prev, .carousel-control-next').on('mouseenter', function() {
  $(this).find('.carousel-control-prev-icon, .carousel-control-next-icon').addClass('animated bounce');
}).on('mouseleave', function() {
  $(this).find('.carousel-control-prev-icon, .carousel-control-next-icon').removeClass('animated bounce');
});
