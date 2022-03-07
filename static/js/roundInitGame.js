main();

function main() {
    const showRoundFormButton = document.querySelector('.show-round-form-button');
    const closeRoundFormButton = document.querySelector('.close-round-form-button');
    [showRoundFormButton, closeRoundFormButton].forEach(
        button => button.addEventListener('click', toggleRoundForm)
    );
}

function toggleRoundForm() {
    const showRoundFormButton = document.querySelector('.show-round-form-button');
    const roundForm = document.querySelector('.round-form');
    roundForm.classList.toggle('hide-round-form');
    showRoundFormButton.disabled = !showRoundFormButton.disabled;
}
