import {dataHandler} from "./data/dataHandler.js";


const data = {
    players: await dataHandler.getPlayers(),
    leagueImages: await dataHandler.getLeagueImages(),
    loggedInUser: await dataHandler.getLoggedInUser()
}

function createNewLeague() {
    const addNewLeagueButton = document.querySelector('button#new-league');
    addNewLeagueButton.addEventListener('click', openNewLeagueDiv);
}

function openNewLeagueDiv() {
    const playerContainer = document.querySelector('div#selected-players');
    addPlayersToGame();

}

function addPlayersToGame() {
    const usernameInput = document.querySelector('input[name="league-players"]');
    usernameInput.addEventListener('input', selectPlayersByInput);
}

function selectPlayersByInput(event) {
    const input = event.currentTarget.value;
    let userContainer = document.querySelector('div#searched-players');
    clearHtml(userContainer);
    for (let player of data.players) {
        if (player.name.includes(input) || player.username.includes(input) && player.id !== data.loggedInUser.id) {
            let playerCard = createPlayerCard(player);
            userContainer.insertAdjacentHTML('beforeend', playerCard);
        }
    }
    addCardEventListeners()
}

function clearHtml(element) {
    element.innerHTML = ``;
}

function createPlayerCard(player) {
    return `
    <div class="player-card" player-id="${player.id}">
        <p>${player.username}(${player.name})</p>
        <img alt="user-image" src="static/${player.image_source}">
    </div>`
}

function addCardEventListeners() {
    let userContainer = document.querySelector('div#searched-players');
    for (let playerCard of userContainer.childNodes) {
        playerCard.addEventListener('click', movePlayerToGame);
    }
}

function movePlayerToGame(event) {
    const selectPlayerContainer = document.querySelector('div#searched-players');
    const selectedPlayerContainer = document.querySelector('div#selected-players');
    removeElement(selectPlayerContainer, event.currentTarget);
    selectedPlayerContainer.appendChild(event.currentTarget);
}

function removeElement(container, element) {
    container.removeChild(element);
}

function main() {
    createNewLeague();
}

main();
