// cache the DOM
const updateUserEl = document.querySelector('#update_user');
const updateUserFormEl = document.querySelector('#user_update_form');
const likeBtn = document.querySelector('.like');
const disLikeBtn = document.querySelector('.dislike');
//  open update user form
if (updateUserEl) {
  updateUserEl.addEventListener('click', (event) => {
    event.preventDefault();
    updateUserFormEl.classList.toggle('hidden');
  });
}

// // Like or dislike news
// sessionStorage.removeItem('like');
// $(document).ready(function () {
//   if (window.location.href.indexOf('news/') > -1) {
//     const like = sessionStorage.getItem('like');
//     if (!like) {
//       disLikeBtn.classList.add('hidden');
//     } else {
//       likeBtn.classList.add('hidden');
//     }
//   }

//   if (likeBtn || disLikeBtn) {
//     likeBtn.addEventListener('click', (event) => {
//       sessionStorage.setItem('like', 'false');
//     });

//     disLikeBtn.addEventListener('click', (event) => {
//       sessionStorage.removeItem('like');
//     });
//   }
// });

// if (likeBtn || disLikeBtn) {
//   const like = sessionStorage.getItem('like');

//   window.onload = function () {
//     if (!like) {
//       disLikeBtn.classList.add('hidden');
//     } else {
//       likeBtn.classList.add('hidden');
//     }
//   };

//   likeBtn.addEventListener('click', (event) => {
//     sessionStorage.setItem('like', 'false');
//   });

//   disLikeBtn.addEventListener('click', (event) => {
//     sessionStorage.removeItem('like');
//   });
// }

// remove flash message
$(document).ready(function () {
  setTimeout(function () {
    $('.alert').alert('close');
  }, 2000);
});
