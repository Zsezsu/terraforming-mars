const editableCells = document.querySelectorAll('td.editable');
editableCells.forEach(cell => cell.addEventListener('input', calculateResults));

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