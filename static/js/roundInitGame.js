main();

function main() {
    const expansionDiv = document.querySelector('#expansions');
    toggleExpansionDiv(expansionDiv);
    showExpansionsCorporations(expansionDiv);
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
    if (!hasExpansions(expansionDiv)) {expansionDiv.remove();}
}

function showExpansionsCorporations(expansionDiv) {
    if (!hasExpansions(expansionDiv)) {return;}
    const expansions = expansionDiv.querySelectorAll(".round-expansion");
    expansions.forEach(
        (input) => {
            input.addEventListener('change', toggleExpansionsCorporations);
        });
}

function toggleExpansionsCorporations() {
    const expansionId = this.value;
    const expansionsCorporations = document.querySelectorAll(`option[data-expansion-id="${expansionId}"]`);
    expansionsCorporations.forEach((corporation)=> {
        corporation.hidden = !this.checked;
    });
}

function hasExpansions(expansionDiv) {
    return expansionDiv.querySelector('input') != null;
}
