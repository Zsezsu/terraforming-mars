export const dataHandler = {
    getPlayers: async function () {
        return await apiGet(`/api/players`);
    }
}

async function apiGet(url) {
    let response = await fetch(url, {method: 'GET'});
    if (response.ok) {
        return await response.json();
    }
}