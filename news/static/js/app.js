// cache the DOM
const updateUserEl = document.querySelector('#update_user');
const updateUserFormEl = document.querySelector('#user_update_form');
const miniatureImgEls = document.getElementsByClassName('miniature_img');





$(document).ready(function () {
  // replace bad picture link with default image
  Array.from(miniatureImgEls).forEach((el) => {
    if (el.width < 249 && el.height < 179) {
      el.src = "/static/default.jpeg"
    }
  });

  // remove flash message
  setTimeout(function () {
    $('.alert').alert('close');
  }, 2000);
});

//  open update user form
if (updateUserEl) {
  updateUserEl.addEventListener('click', (event) => {
    event.preventDefault();
    updateUserFormEl.classList.toggle('hidden');
  });
}