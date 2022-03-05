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


function saveRound() {
    if (confirm('Can we start the game?') === true) {
        const players = document.querySelectorAll('tr[data-player-id]');
        let results = [];
        for (let player of players) {
            const total = player.querySelector('th.result').innerText;
            const playerId = player.getAttribute('data-player-id');
            let playerResult = {playerId: playerId, total: total}

            const points = player.querySelectorAll('td input');
            let resultPoints = [];
            for (let point of points) {
                resultPoints.push(point.value)
            }
            playerResult['points'] = resultPoints;
            results.push(playerResult)
        }
        console.log(results);
    }

}

main();