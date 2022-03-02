function createNewLeague() {
    const button = document.querySelector('button#new-league');
    button.addEventListener('click', openLeague)
}

function openLeague() {
    const div = document.querySelector('div[hidden]');
    div.hidden = false;
}

createNewLeague();