import { dataHandler } from "./data/dataHandler.js";

function initForm() {
  let nickname = document.querySelector('#username-input');
  let email1 = document.querySelector('#email-input');
  let email2 = document.querySelector('#email2-input');
  let password1 = document.querySelector('#password-input');
  let password2 = document.querySelector('#password2-input');
  [nickname, email1, email2, password1, password2].forEach((e) => {
    e.addEventListener('input', validataData);
  });
}

async function validataData(e) {
  const target = await e.currentTarget;
  console.log(`target: ${target.id} ${typeof target.id}`)
  let error = false;
  switch (target.id) {
    case "username-input":
      error = await usernameExist(target);
      break;
    case "email-input":
      error = await emailExist(target);
      error = emailRegex(target);
      break;
    case "email2-input":
      error = emailMatch(target);
      break;
    case "password-input":
      error = passwordRegex(target);
      break;
    case "password2-input":
      error = passwordMatch(target);
      break;
  }
  if (error) {
    // append error message here
    // error ==> error type (example: if email syntax wrong it returns 'email format is not correct')
    console.log(`------------------------------
                \nInput error type: ${error}
                \n------------------------------`);
  }
}

async function usernameExist(target) {
  if (await dataHandler.getIsTokenExist(target.value)) {
    return 'Username already exist.';
  }
}

function emailRegex(target) {
  const emailRegex = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$/
  if (!(emailRegex.test(target.value))) {
    return 'Email form is invalid.'
  }
}

async function emailExist(target) {
  if (await dataHandler.getIsTokenExist(target.value)) {
    return 'Email already exist.'
  }
}

function emailMatch(target) {
  const email1 = document.querySelector('#email-input').value;
  if (target.value !== email1) {
    return 'Emails are not matching.'
  }
}

function passwordRegex(target) {
  const pwdRegex = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,16}$/
  if (!(target.value.match(pwdRegex))) {
    return 'Password length between 6-16 and should contain:\n- one letter\n- one number\n one special character'
  }
}

function passwordMatch(target) {
  const pwd1 = document.querySelector('#password-input').value;
  if (target.value !== pwd1) {
    return 'Passwords are not matching.'
  }
}

initForm();
