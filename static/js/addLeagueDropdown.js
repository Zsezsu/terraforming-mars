const searchInput = document.querySelector('#league-players');
const searchedPlayers = document.querySelector('#searched-players');

document.addEventListener('click', closeDropdown);

function closeDropdown(clickEvent) {
    const clickedElement = clickEvent.target;
    if (clickedElement !== searchInput && clickedElement !== searchedPlayers) {
        searchedPlayers.classList.add('hidden');
    } else {
        searchedPlayers.classList.remove('hidden');
    }
}