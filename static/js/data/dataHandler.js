export const dataHandler = {
    getPlayers: async function() {
        return await apiGet(`/api/players`);
    },
    getLeagueImages: async function() {
        return await apiGet(`/api/images/leagues`);
    },
    getLoggedInUser: async function() {
        return await apiGet(`/api/users/logged-in`);
    }
}

async function apiGet(url) {
    let response = await fetch(url, {method: 'GET'});
    if (response.ok) {
        return await response.json();
    }
}