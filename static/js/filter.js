const filter = {
    init(){
        this.filterByGameType()
    },

    filterByGameType(){
        const gameTypes = document.querySelector('#filter-game-type');
        gameTypes.addEventListener('change', this.filterEventListener.bind(this))
    },

    filterEventListener(event) {
        const value = event.currentTarget.value;
        let cards = document.querySelectorAll('.card.league');
        this.removeLeagueDivMessages();
        for (let card of cards) {
            if (value === 'all') {
                card.hidden = false;
            } else {
                card.hidden = (card.dataset.leagueType !== value);
            }
        }
        if (!this.hasLeague(cards)) {
            this.displayNoLeagueMessage(event.currentTarget);
        }
    },

    hasLeague(cards) {
        for (let card of cards) {
            if (card.getAttribute('hidden') == null) {
                return true;
            }
        }
        return false;
    },

    displayNoLeagueMessage(target) {
        const leagueContainer = document.querySelector('#league-card-container');
        let message = null;
        switch (target.value) {
            case 'all':
                message = "You don't have any league yet!";
                break;
            case '1':
                message = "You don't have any Terraforming Mars league yet!";
                break;
            case '2':
                message = "You don't have any Ares Expedition league yet!";
                break;
            default:
                message = "You don't have any league yet!"
        }
        leagueContainer.insertAdjacentHTML(
            'afterbegin',
            `<h2 class="text-light no-league">${message}</h2>`
        )
    },

    removeLeagueDivMessages() {
            document.querySelectorAll('.no-league').forEach((message) => {message.remove()});
    }
}

filter.init();