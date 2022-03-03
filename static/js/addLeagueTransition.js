main();

function main() {
    const addNewLeagueButton = document.querySelector('#new-league');
    const confirmNewLeagueButton = document.querySelector('#button-confirm');
    const closeNewLeagueButton = document.querySelector('#button-close');
    [addNewLeagueButton, confirmNewLeagueButton, closeNewLeagueButton].forEach(
        button => button.addEventListener('click', toggleAddNewLeague)
    );
}

function toggleAddNewLeague() {
    const newLeagueButton = document.querySelector('#new-league');
    const newLeague = document.querySelector('.new-league');
    newLeague.classList.toggle('hide-new-league');
    newLeagueButton.classList.toggle('hide-new-league-button');
    newLeagueButton.disabled = !newLeagueButton.disabled;
}