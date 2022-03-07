
function initClick() {
  let pictures = document.querySelectorAll('img.profile-picture');
  pictures.forEach(e => {
    e.addEventListener('click', getPictureId);
  })
}

function getPictureId(e) {
  const id = e.currentTarget.id;
  document.querySelector('#picture-input').value = id;
  document.querySelector('#hidden-button').removeAttribute('hidden');
  let allPicture = e.currentTarget.parentElement.children;
  for (let picture of allPicture) {
    picture.classList.remove('selected');
  }
  e.currentTarget.classList.add('selected');
}

initClick()
