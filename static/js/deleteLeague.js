import {dataHandler} from "./data/dataHandler.js";

const deleteLeague = {
    init() {
       this.clickOnDelete();
    },

    clickOnDelete() {
        const deleteButton = document.querySelector("#delete-button");
        if(deleteButton){
            deleteButton.addEventListener('click', this.deleteLeague);
        }
    },

    async deleteLeague(e) {
        if (window.confirm('Are you sure you want to delete this league?' +
                '\n Be careful this is irreversible!')){
            const leagueNumber = e.currentTarget.getAttribute('data-league-id');
            await dataHandler.deleteLeague(leagueNumber);
            window.location.replace("/my-leagues");
        }
    }
}

deleteLeague.init();