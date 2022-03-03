import {dataHandler} from "./data/dataHandler.js";


function createNewLeague() {
    const addNewLeagueButton = document.querySelector('button#new-league');
    addNewLeagueButton.addEventListener('click', openNewLeagueDiv);
}

async function openNewLeagueDiv() {
    const players = await dataHandler.getPlayers();
    const leagueImages = await dataHandler.getLeagueImages();
    const loggedInUser = await dataHandler.getLoggedInUser();
    const playerContainer = document.querySelector('div#selected-players');

}



function main() {
    createNewLeague();
}

main();
