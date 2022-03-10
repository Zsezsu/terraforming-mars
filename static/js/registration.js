function initClick() {
    const submitButton = document.querySelector('#submit-btn');
    submitButton.addEventListener('click', getPictureId);
}

function getPictureId() {
    const picture = document.querySelector('#slideshow-profile');
    const pictureId = picture.getAttribute('data-image-id');
    const pictureInput = document.querySelector('#picture-input');
    pictureInput.value = pictureId;
}

initClick();
