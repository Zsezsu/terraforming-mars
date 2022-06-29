main();

function main() {
    const expansionDiv = document.querySelector('#expansions');
    toggleExpansionDiv(expansionDiv);
    showExpansionsCorporations(expansionDiv);
    toggleSelectedCorporation();
    const showRoundFormButton = document.querySelector('.show-round-form-button');
    const closeRoundFormButton = document.querySelector('.close-round-form-button');
    [showRoundFormButton, closeRoundFormButton].forEach(
        button => button.addEventListener('click', toggleRoundForm)
    );
    const saveRoundButton = document.querySelector('button.save-round-form-button');

}

function toggleRoundForm() {
    const showRoundFormButton = document.querySelector('.show-round-form-button');
    const roundForm = document.querySelector('.round-form');
    roundForm.classList.toggle('hide-form-container');
    showRoundFormButton.disabled = !showRoundFormButton.disabled;
}


function toggleExpansionDiv(expansionDiv) {
    if (!hasExpansions(expansionDiv)) {
        expansionDiv.remove();
    }
}

function showExpansionsCorporations(expansionDiv) {
    if (!hasExpansions(expansionDiv)) {
        return;
    }
    const expansions = expansionDiv.querySelectorAll(".round-expansion");
    expansions.forEach(
        (input) => {
            input.addEventListener('change', toggleExpansionsCorporations);
        });
}

function toggleExpansionsCorporations() {
    const expansionId = this.value;
    const expansionsCorporations = document.querySelectorAll(`option[data-expansion-id="${expansionId}"]`);
    expansionsCorporations.forEach((corporation) => {
        corporation.hidden = !this.checked;
    });
    const corporations = document.querySelectorAll(`.corporations`);
    corporations.forEach(
        (corporation) => {
            const selectedOption = corporation.selectedOptions[0];
            const selectedOptionExpansionId = selectedOption.getAttribute("data-expansion-id");
            if (selectedOption.value !== "" && selectedOptionExpansionId === expansionId) {
                corporation.value = "";
            }
        }
    )
}

function toggleSelectedCorporation() {
    const corporations = document.querySelectorAll('.corporations');
    corporations.forEach(
        (corporation) => {
            corporation.addEventListener('change', toggleCorporationForOthers);
        });
}

function toggleCorporationForOthers() {
    const selectedCorporation = this.selectedOptions[0];
    const playerId = selectedCorporation.getAttribute('data-player-id');
    const previousSelectedCorporation = document.querySelector(`.corporation[data-selected="true"][data-player-id="${playerId}"]`);
    if (previousSelectedCorporation) {
        showPreviouslySelectedCorporation(playerId, previousSelectedCorporation);
    }
    hideSelectedCorporation(this.value);
    selectedCorporation.hidden = false;
    selectedCorporation.setAttribute("data-selected", "true");
}

function showPreviouslySelectedCorporation(playerId, previousSelectedCorporation) {
    const otherPlayerCorporations = document.querySelectorAll(`.corporations:not(#player${playerId})`);
    const previousSelectedCorporationId = previousSelectedCorporation.value;
    otherPlayerCorporations.forEach(
        (corporations) => {
            corporations.querySelector(`.corporation[value="${previousSelectedCorporationId}"]`).hidden = false;
            previousSelectedCorporation.removeAttribute("data-selected");
        });
}

function hideSelectedCorporation(selectedCorporationID) {
    const selectedCorporations = document.querySelectorAll(`option[value="${selectedCorporationID}"]`);
    selectedCorporations.forEach(
        (corporation) => {
            corporation.hidden = true;
        });
}

function hasExpansions(expansionDiv) {
    return expansionDiv.querySelector('input') != null;
}
