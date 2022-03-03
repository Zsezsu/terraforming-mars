import {dataHandler} from "./data/dataHandler.js";


const data = {
    players: await dataHandler.getPlayers(),
    leagueImages: await dataHandler.getLeagueImages(),
    loggedInUser: await dataHandler.getLoggedInUser()
}

function createNewLeague() {
    const addNewLeagueButton = document.querySelector('button#new-league');
    addNewLeagueButton.addEventListener('click', addPlayersToGame);
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
        if (player.name.includes(input) || player.username.includes(input)) {
            if (!selectedPlayers(player.id)) {
                let playerCard = createPlayerCard(player);
                userContainer.insertAdjacentHTML('beforeend', playerCard);
            }
        }
    }
    addCardEventListeners()
}

function selectedPlayers(playerId) {
    const selectedPlayers = document.querySelector('div#selected-players').children;
    for (let selectedPlayer of selectedPlayers) {
        if (+selectedPlayer.getAttribute('player-id') === playerId) {
            return true
        }
    }
    return false

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
    selectPlayerContainer.removeChild(event.currentTarget);

    const selectedPlayerContainer = document.querySelector('div#selected-players');
    selectedPlayerContainer.appendChild(event.currentTarget);
    event.currentTarget.removeEventListener('click', movePlayerToGame)
}

function main() {
    createNewLeague();
}

main();
