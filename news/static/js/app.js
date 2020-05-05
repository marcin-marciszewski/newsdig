// cache the DOM
const updateUserEl = document.querySelector('#update_user');
const updateUserFormEl = document.querySelector('#user_update_form');

// remove flash message
$(document).ready(function () {
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