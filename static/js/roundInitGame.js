main();

function main() {
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
