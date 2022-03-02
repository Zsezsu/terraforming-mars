import {dataHandler} from "./data/dataHandler.js";
import {htmlFactory} from "./view/htmlFactory.js";
import {htmlTemplates} from "./view/htmlFactory.js";

function createNewLeague() {
    const button = document.querySelector('button#new-league');
    button.addEventListener('click', openLeague)
}

async function openLeague() {
    const div = document.querySelector('div#add-league');
    const users = await dataHandler.getPlayers();
    let userSelects = createUserSelect(users);
    let formBuilder = htmlFactory(htmlTemplates.form);
    const form = formBuilder(userSelects)
    div.innerHTML = form;
    div.hidden = false;
}

function createUserSelect(users) {
    let userOptions = ``;
    for (let user of users) {
        let optionBuilder = htmlFactory(htmlTemplates.option);
        userOptions += optionBuilder(user);
    }
    return userOptions;
}



createNewLeague();