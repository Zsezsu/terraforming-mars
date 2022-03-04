import {dataHandler} from "./data/dataHandler.js";

const images = await dataHandler.getImages('league-cards');

export const leagueImages = {
    leagueImage: document.getElementById('slideshow-image'),
    imageIndex: images.length,
    maxImageIndex: images.length,
    currentImageIndex: 0
}


main();

async function main() {
    changeImage();
    const previousButton = document.getElementById('slideshow-previous');
    const nextButton = document.getElementById('slideshow-next');
    previousButton.addEventListener('click', previousImage);
    nextButton.addEventListener('click', nextImage);
}

export function changeImage() {
    leagueImages.leagueImage.src = `static/${images[leagueImages.currentImageIndex].image_source}`;
    leagueImages.leagueImage.setAttribute('data-image-id', images[leagueImages.currentImageIndex].id);
}

function nextImage() {
    leagueImages.currentImageIndex += 1;
    if (leagueImages.currentImageIndex >= leagueImages.maxImageIndex) {
        leagueImages.currentImageIndex = 0;
    }
    changeImage();
}

function previousImage() {
    leagueImages.currentImageIndex -= 1;
    if (leagueImages.currentImageIndex < 0) {
        leagueImages.currentImageIndex = leagueImages.maxImageIndex - 1;
    }
    changeImage();
}


