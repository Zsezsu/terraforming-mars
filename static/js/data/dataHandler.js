export const dataHandler = {
    //GET
    getPlayers: async function () {
        return await apiGet(`/api/players`);
    },
    getLoggedInUser: async function () {
        return await apiGet(`/api/users/logged-in`);
    },
    getImages: async function(imageType) {
        return await apiGet(`/api/images/${imageType}`);
    },
    getIsTokenExist: async function(token) {
        return await apiGet(`/api/user/name/${token}`);
    },

    //POST
    postNewLeague: async function (data) {
        return await apiPost(`/api/leagues`, data);
    },
    saveResults: async function (leagueId, roundId, data) {
        return await apiPost(`/api/leagues/${leagueId}/rounds/${roundId}`, data)
    },

    //PUT
    updateProfilePicture: async function(playerId, imageId) {
        return await apiPut(
            `/api/players/${playerId}`,
            {'imageId': imageId}
        );
    },

    //DELETE
    deleteLeague: async function (leagueId) {
        await apiDelete(`/api/leagues/${leagueId}`);
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

async function apiPut(url, payload) {
    const response = await fetch(url, {
        method: 'PUT',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(payload)
    });
    if (response.ok) {
        return response.status;
    }
}

async function apiDelete(url) {
    await fetch(url, {
        method: 'DELETE'
    });
}