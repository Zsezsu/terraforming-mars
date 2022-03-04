import {dataHandler} from "./data/dataHandler.js";
import {toggleAddNewLeague} from "./addLeagueTransition.js";
import {leagueImages, changeImage} from "./leagueSlideshow.js";

const data = {
    players: await dataHandler.getPlayers(),
    leagueImages: await dataHandler.getImages('league-cards'),
    loggedInUser: await dataHandler.getLoggedInUser()
}

function createNewLeague() {
    const addNewLeagueButton = document.querySelector('button#new-league');
    addNewLeagueButton.addEventListener('click', addPlayersToGame);

    const confirmButton = document.querySelector('button#button-confirm');
    confirmButton.addEventListener('click', confirm)
}

// --------------------------------Select Players------------------------------------------

function addPlayersToGame() {
    const usernameInput = document.querySelector('input[name="league-players"]');
    usernameInput.addEventListener('input', selectPlayersByInput);
}

function selectPlayersByInput(event) {
    const input = event.currentTarget.value;
    playerSelector(input)
}

function playerSelector(input) {
    let userContainer = document.querySelector('div#searched-players');
    clearHtml(userContainer);
    for (let player of data.players) {
        if (input !== '') {
            if (player.name.toLowerCase().includes(input.toLowerCase()) ||
                player.username.toLowerCase().includes(input.toLowerCase())) {
                if (!selectedPlayers(player.id)) {
                    let playerCard = createPlayerCard(player);
                    userContainer.insertAdjacentHTML('beforeend', playerCard);
                }
            }
        }
    }
    addCardEventListeners();
}

function selectedPlayers(playerId) {
    const selectedPlayers = document.querySelector('div#selected-players').children;
    for (let selectedPlayer of selectedPlayers) {
        if (+selectedPlayer.getAttribute('data-player-id') === playerId) {
            return true;
        }
    }
    return false;
}

function clearHtml(element) {
    element.innerHTML = ``;
}

function createPlayerCard(player) {
    return `
    <div class="player-card card bg-dark" data-player-id="${player.id}">
        <img alt="Profile picture of ${player.username}" src="static/${player.image_source}">
        <div class="player-card-description">
            <p>${player.name}</p>
            <small>${player.username}</small>
        </div>
    </div>`;
}

function addCardEventListeners() {
    let userContainer = document.querySelector('div#searched-players');
    for (let playerCard of userContainer.childNodes) {
        playerCard.addEventListener('click', movePlayerToGame);
    }
}

function movePlayerToGame(event) {
    const playerLimit = 5;
    const selectedPlayerContainer = document.querySelector('div#selected-players');
    const selectPlayerContainer = document.querySelector('div#searched-players');
    if (selectedPlayerContainer.children.length >= playerLimit) {
        alert('You have reached the player limit(5)');
    } else {
        selectPlayerContainer.removeChild(event.currentTarget);
        selectedPlayerContainer.appendChild(event.currentTarget);
        event.currentTarget.removeEventListener('click', movePlayerToGame);
        addRemoveButton(event.currentTarget);
        refreshPlayersNumber();
    }

}

function addRemoveButton(player) {
    const playerId = +player.getAttribute('data-player-id');
    player.insertAdjacentHTML('beforeend',
        `<i data-remove-id="${playerId}" class="fa-solid fa-circle-xmark text-danger"></i>`
    );
    const removeButton = player.querySelector('i');
    removeButton.addEventListener('click', removePlayer);
}

function removePlayer(event) {
    const playerId = event.target.getAttribute('data-remove-id');
    const selectedPlayerContainer = document.querySelector('div#selected-players');
    const currentPlayer = selectedPlayerContainer.querySelector(`div[data-player-id="${playerId}"]`)
    selectedPlayerContainer.removeChild(currentPlayer);
    refreshPlayersNumber();
    refreshPlayerSelector();
}

function refreshPlayerSelector() {
    const userInput = document.querySelector('input[name="league-players"]').value;
    playerSelector(userInput);
}

function refreshPlayersNumber() {
    const selectedPlayerContainer = document.querySelector('div#selected-players');
    const selectedPlayersLabel = document.querySelector('label#label-league-players');
    selectedPlayersLabel.innerText = `League Players ${selectedPlayerContainer.children.length}/5`;
}

// --------------------------------Confirm league------------------------------------------


const confirm = async function () {
    const leagueName = document.querySelector('input[name="league-name"]').value;
    const leagueRounds = document.querySelector('input[name="league-rounds"]').value;
    const selectedPlayers = document.querySelector('div#selected-players').children;
    const leagueAdminId = data.loggedInUser.id;
    const selectedLeagueImage = document.querySelector('img[data-image-id]');
    const selectedLeagueImageSource = selectedLeagueImage.getAttribute('src');
    const minRounds = 1;
    const maxRounds = 10;
    const minPlayers = 1;
    const maxPlayers = 5;
    const divTransition = 1000;
    if (leagueName) {
        if (+leagueRounds >= minRounds && +leagueRounds <= maxRounds) {
            if (+selectedPlayers.length >= minPlayers && +selectedPlayers.length <= maxPlayers) {
                const selectedPlayersDetails = getPlayersDetails(selectedPlayers)
                const data = {
                    'leagueName': leagueName,
                    'leagueRounds': leagueRounds,
                    'userIds': selectedPlayersDetails,
                    'leagueAdminId': leagueAdminId,
                    'leagueImageId': selectedLeagueImage.getAttribute('data-image-id'),
                    'selectedLeagueImageSource': selectedLeagueImageSource
                }
                toggleAddNewLeague();
                setTimeout(clearLeagueDiv, divTransition);
                const newLeagueId = await dataHandler.postNewLeague(data);
                addNewLeagueCard(data, newLeagueId);
            } else {
                alert(`players Number(${selectedPlayers.length}) has to be between ${minPlayers}-${maxPlayers}`);
            }
        } else {
            alert(`League round(${leagueRounds}) has to be between ${minRounds}-${maxRounds}`);
        }
    } else {
        alert('League name required');
    }
}


function addNewLeagueCard(data, newLeagueId) {
    const leagueDiv = document.querySelector('div#league-card-container');
    const newLeagueDiv = `<div class="card league bg-dark" data-league-id="${newLeagueId}" data-league-admin-id="${data.leagueAdminId}">
                <img alt="mars" src="${data.selectedLeagueImageSource}">
                <h3 class="text-light">${data.leagueName}</h3>
                <div class="card-details">
                    <small class="text-light">${data.userIds.length}</small>
                    <i class="fa-solid fa-user-astronaut text-light"></i>
                    <small class="text-light">0 / ${data.leagueRounds}</small>
                    <i class="fa-solid fa-circle-check text-light"></i>
                </div>`
    leagueDiv.insertAdjacentHTML('afterbegin', newLeagueDiv);
}

function clearLeagueDiv() {
    document.querySelector('input[name="league-name"]').value = "";
    document.querySelector('input[name="league-rounds"]').value = "";
    document.querySelector('input[name="league-players"]').value = "";
    document.querySelector('label#label-league-players').innerText = "League Players 1/5";
    document.querySelector('div#selected-players').innerHTML = createPlayerCard(data.loggedInUser);
    document.querySelector('div#searched-players').innerHTML = "";
    leagueImages.currentImageIndex = 0;
    changeImage();
}

function getPlayersDetails(players) {
    let playersDetails = [];
    for (let player of players) {
        let id = player.getAttribute('data-player-id');
        playersDetails.push({'id': id});
    }
    return playersDetails;
}

function main() {
    createNewLeague();
}

main();