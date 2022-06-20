import {dataHandler} from "./data/dataHandler.js";

const deleteLeague = {
    init() {
       this.clickOnDelete();
    },

    clickOnDelete(){
        let deleteButton = document.querySelector("#delete-button");
        deleteButton.addEventListener('click', this.deleteLeague)
    },

    async deleteLeague(e){
        if (window.confirm('Are you sure you want to delete this league?' +
                '\n Be careful this is irreversible!')){
            let leagueNumber = e.currentTarget.getAttribute('data-league-id');
            console.log(leagueNumber);
            await dataHandler.deleteLeague(leagueNumber);
            // window.location.replace("/my-leagues");
        }
    }
}

deleteLeague.init();