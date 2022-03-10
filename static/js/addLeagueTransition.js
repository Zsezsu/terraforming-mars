main();

function main() {
    const addNewLeagueButton = document.querySelector('#new-league');
    const closeNewLeagueButton = document.querySelector('#button-close');
    [addNewLeagueButton, closeNewLeagueButton].forEach(
        button => button.addEventListener('click', toggleAddNewLeague)
    );
}

export function toggleAddNewLeague() {
    const newLeagueButton = document.querySelector('#new-league');
    const newLeague = document.querySelector('.new-league');
    newLeague.classList.toggle('hide-form-container');
    newLeagueButton.disabled = !newLeagueButton.disabled;
}