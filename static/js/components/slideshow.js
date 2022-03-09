import {dataHandler} from "../data/dataHandler.js";

let images;

export const imageTypes = {
    league: 'league-cards'
}

export const imageData = {
    imageElement: document.createElement('img'),
    maxIndex: 0,
    currentIndex: 0
}

export async function slideshow(imageType) {
    await initSlideshow(imageType);
    changeImage();
    const previousButton = document.querySelector('.slideshow-prev');
    const nextButton = document.querySelector('.slideshow-next');
    previousButton.addEventListener('click', previousImage);
    nextButton.addEventListener('click', nextImage);
}

async function initSlideshow(imageType) {
    images = await dataHandler.getImages(imageType);
    imageData.imageElement = document.querySelector('.slideshow img');
    imageData.maxIndex = images.length;
}

export function changeImage() {
    imageData.imageElement.src = `/static/${images[imageData.currentIndex]['image_source']}`;
    imageData.imageElement.setAttribute('data-image-id', images[imageData.currentIndex].id);
}

function nextImage() {
    imageData.currentIndex += 1;
    if (imageData.currentIndex >= imageData.maxIndex) {
        imageData.currentIndex = 0;
    }
    changeImage();
}

function previousImage() {
    imageData.currentIndex -= 1;
    if (imageData.currentIndex < 0) {
        imageData.currentIndex = imageData.maxIndex - 1;
    }
    changeImage();
}

