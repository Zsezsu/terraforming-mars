import {dataHandler} from "./data/dataHandler.js";

const pointsTypes = [
    'tr_number',
    'milestones_points',
    'award_points',
    'number_of_own_greeneries',
    'number_of_cities',
    'greeneries_around_cities',
    'vp_on_cards',
];

function main() {
    const editableCells = document.querySelectorAll('td.editable');
    editableCells.forEach(cell => cell.addEventListener('input', calculateResults));

    const saveButton = document.querySelector('button#save-round');
    saveButton.addEventListener('click', saveRound)
}

function calculateResults(inputEvent) {
    const inputCell = inputEvent.target;
    const playerId = inputCell.getAttribute('data-player-id');
    const resultCell = document.querySelector(`th.result[data-player-id="${playerId}"]`);
    const playerCells = document.querySelectorAll(`td.editable input[data-player-id="${playerId}"]`);
    let resultSum = 0;
    playerCells.forEach(cell => {
        const cellValue = parseInt(cell.value);
        cellValue ? resultSum += parseInt(cell.value) : 0;
    });
    resultCell.textContent = resultSum;
}


async function saveRound() {
    if (confirm('Can we start the game?') === true) {
        const players = document.querySelectorAll('tr[data-player-id]');
        const table = document.querySelector("table#point-table");
        const leagueId = table.getAttribute('data-league-id');
        const roundId = table.getAttribute('data-round-id');
        let results = [];

        for (let player of players) {
            const total = player.querySelector('th.result').innerText;
            const playerId = player.getAttribute('data-player-id');
            let playerResult = {playerId: playerId, total: total};

            const points = player.querySelectorAll('td input');
            let resultPoints = {};
            for (let index = 0; index < points.length; index++) {
                let pointType = pointsTypes[index];
                resultPoints[pointType] = points[index].value;
            }
            playerResult['points'] = resultPoints;
            results.push(playerResult);
        }
        await dataHandler.saveResults(leagueId, roundId, results);
    }

}

main();