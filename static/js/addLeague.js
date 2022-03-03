import {dataHandler} from "./data/dataHandler.js";


function createNewLeague() {
    const addNewLeagueButton = document.querySelector('button#new-league');
    addNewLeagueButton.addEventListener('click', openNewLeagueDiv);
}

async function openNewLeagueDiv() {
    const players = await dataHandler.getPlayers();
    const leagueImages = await dataHandler.getLeagueImages();
}



function main() {
    createNewLeague();
}

main();
