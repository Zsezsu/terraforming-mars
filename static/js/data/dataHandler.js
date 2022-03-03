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
    getImages: async function() {
        return [
            '/static/img/mars-1.webp',
            '/static/img/mars-2.webp',
            '/static/img/mars-3.webp',
            '/static/img/mars-4.webp',
            '/static/img/mars-5.webp',
        ]
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