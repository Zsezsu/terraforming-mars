import {dataHandler} from "./data/dataHandler.js";

function initForm() {
    const firstName = document.querySelector('#firstname-input');
    const lastName = document.querySelector('#lastname-input');
    const nickname = document.querySelector('#username-input');
    const email1 = document.querySelector('#email-input');
    const email2 = document.querySelector('#email2-input');
    const password1 = document.querySelector('#password-input');
    const password2 = document.querySelector('#password2-input');
    [nickname, email1, email2, password1, password2].forEach((e) => {
        e.addEventListener('input', validataData);
    });
    [firstName, lastName, nickname, email1, email2, password1, password2].forEach(e => {
        e.addEventListener('input', unlockButton);
    })
}

function unlockButton() {
    const inputs = document.querySelectorAll('.form input:not(#picture-input)');
    const errorMessages = document.querySelectorAll('.form small.reg-error');
    const button = document.querySelector('#submit-btn');
    console.log(inputs);
    console.log(errorMessages);

    for (let input of inputs) {
        if (!input.value) {
            button.disabled = true;
            return
        }
    }
    for (let message of errorMessages) {
        if (!message.hidden) {
            button.disabled = true;
            return
        }
    }
    button.disabled = false;
}

async function validataData(e) {
    const target = await e.currentTarget;
    switch (target.id) {
        case "username-input":
            await usernameExist(target);
            break;
        case "email-input":
            await emailRegex(target);
            emailMatch();
            break;
        case "email2-input":
            emailMatch();
            break;
        case "password-input":
            passwordRegex(target);
            passwordMatch();
            break;
        case "password2-input":
            passwordMatch();
            break;
    }
}

async function usernameExist(target) {
    await dataHandler.getIsTokenExist(target.value) ? showErrorMessage(target) : hideErrorMessage(target);
}

async function emailRegex(target) {
    const emailRegex = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$/;
    !(emailRegex.test(target.value)) || await dataHandler.getIsTokenExist(target.value) ?
        showErrorMessage(target) : hideErrorMessage(target);
}

function emailMatch() {
    const email1 = document.querySelector('#email-input');
    const email2 = document.querySelector('#email2-input');
    email1.value !== email2.value ? showErrorMessage(email2) : hideErrorMessage(email2);
}

function passwordRegex(target) {
    const pwdRegex = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{6,16}$/;
    !(target.value.match(pwdRegex)) ? showErrorMessage(target) : hideErrorMessage(target);
}

function passwordMatch() {
    const pwd1 = document.querySelector('#password-input');
    const pwd2 = document.querySelector('#password2-input');
    pwd1.value !== pwd2.value ? showErrorMessage(pwd2) : hideErrorMessage(pwd2);
}

function showErrorMessage(element) {
    const errorMsg = document.querySelector(`small[data-input-id="${element.id}"]`)
    errorMsg.hidden = false;
}

function hideErrorMessage(element) {
    const errorMsg = document.querySelector(`small[data-input-id="${element.id}"]`)
    errorMsg.hidden = true;
}

initForm();
