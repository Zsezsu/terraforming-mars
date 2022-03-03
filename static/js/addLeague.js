import {dataHandler} from "./data/dataHandler.js";

const data = {
    players: await dataHandler.getPlayers(),
    leagueImages: await dataHandler.getLeagueImages(),
    loggedInUser: await dataHandler.getLoggedInUser()
}

function createNewLeague() {
    const addNewLeagueButton = document.querySelector('button#new-league');
    addNewLeagueButton.addEventListener('click', addPlayersToGame);

    const confirmButton = document.querySelector('button#button-confirm');
    confirmButton.addEventListener('click', confirmLeague.confirm)
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
        if (player.name.includes(input) || player.username.includes(input)) {
            if (!selectedPlayers(player.id)) {
                let playerCard = createPlayerCard(player);
                userContainer.insertAdjacentHTML('beforeend', playerCard);
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
    <div class="player-card" data-player-id="${player.id}">
        <p>${player.username}(${player.name})</p>
        <img alt="user-image" src="static/${player.image_source}">
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

const confirmLeague = {
    confirm: function () {
        const leagueName = document.querySelector('input[name="league-name"]').value;
        const leagueRounds = document.querySelector('input[name="league-rounds"]').value;
        const selectedPlayers = document.querySelector('div#selected-players').children;
        const minRounds = 1;
        const maxRounds = 10;
        const minPlayers = 1;
        const maxPlayers = 5;
        if (leagueName) {
            if (+leagueRounds >= minRounds && +leagueRounds <= maxRounds) {
                if (+selectedPlayers.length >= minPlayers && +selectedPlayers.length <= maxPlayers) {
                    const selectedPlayersDetails = getPlayersDetails(selectedPlayers)
                    const data = {
                        'leagueName': leagueName,
                        'leagueRounds': leagueRounds,
                        'userIds': selectedPlayersDetails
                    }
                    dataHandler.postNewLeague(data);
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
