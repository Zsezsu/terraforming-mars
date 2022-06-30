import {dataHandler} from "./data/dataHandler.js";

main();

function main() {
    const updateProfilePictureButton = document.querySelector('#update-profile-picture');
    updateProfilePictureButton.addEventListener('click', updateProfilePicture);
}

async function updateProfilePicture() {
    const userId = document.querySelector('#username').getAttribute('data-user-id');
    const imageId = document.querySelector('#slideshow-profile').getAttribute('data-image-id');
    const status = await dataHandler.updateProfilePicture(userId, imageId);
    if (status === 200) {
        alert('Successfully updated the profile picture!')
    }
}