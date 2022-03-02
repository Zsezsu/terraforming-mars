export const htmlTemplates = {
    form: 1,
    option: 2,
}

export function htmlFactory(template) {
    switch (template) {
        case htmlTemplates.form: {
            return formBuilder;
        }
        case htmlTemplates.option: {
            return optionBuilder;
        }
    }
}

function formBuilder(options) {
    return`
    <form>
        <label for="league-name">League Name</label>
        <input name="league-name" type="text" placeholder="League Name" required>
        
        <label for="league-name">Players</label>
        ${options}
    </form>
`
}

function optionBuilder(user) {
    return`
    <option user-id="${user['id']}">${user['name']}</option>
`
}

