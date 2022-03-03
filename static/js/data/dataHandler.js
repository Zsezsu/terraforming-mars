export const dataHandler = {
    //GET
    getPlayers: async function () {
        return await apiGet(`/api/players`);
    },
    getLeagueImages: async function () {
        return await apiGet(`/api/images/leagues`);
    },
    getLoggedInUser: async function () {
        return await apiGet(`/api/users/logged-in`);
    },
    //POST
    postNewLeague: async function (data) {
        await apiPost(`/api/leagues`, data);
    }
}

async function apiGet(url) {
    let response = await fetch(url, {method: 'GET'});
    if (response.ok) {
        return await response.json();
    }
}

async function apiPost(url, payload) {
    const response = await fetch(
        url,
        {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(payload)
        }
    );
    if (response.ok) {
        return await response.json();
    }
}