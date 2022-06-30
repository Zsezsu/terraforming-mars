import {dataHandler} from "./data/dataHandler.js";

main();

const playerId = document.querySelector('#username').getAttribute('data-user-id');

function main() {
    const updateProfilePictureButton = document.querySelector('#update-profile-picture');
    const updatePasswordButton = document.querySelector('#update-password');
    updateProfilePictureButton.addEventListener('click', updateProfilePicture);
    updatePasswordButton.addEventListener('click', updatePassword);
}

async function updateProfilePicture() {
    const imageId = document.querySelector('#slideshow-profile').getAttribute('data-image-id');
    const response = await dataHandler.updateProfilePicture(playerId, imageId);
    if (response.status === 200) {
        alert('Successfully updated the profile picture!');
    }
}

async function updatePassword() {
    const oldPassword = document.querySelector('#old-password').value;
    const newPassword = document.querySelector('#new-password').value;
    const response = await dataHandler.updatePassword(playerId,
        {
            'oldPassword': oldPassword,
            'newPassword': newPassword
        });
    if (response.status === 401) {
        alert(await response.text());
    } else if (response.status === 200) {
        alert('Successfully updated the password!');
    }
}
