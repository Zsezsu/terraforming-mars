const filter = {
    init(){
        this.filterByGameType();
        this.selectFilterByStatuses();
    },

    filterByGameType(){
        const gameTypes = document.querySelector('#filter-game-type');
        gameTypes.addEventListener('change', this.filterEventListener)

    },

    filterEventListener(){
        let cards = document.querySelectorAll('.card.league');
        for (let card of cards){
            if (this.value === 'all'){
                card.hidden = false;
            } else {
                card.hidden = (card.dataset.leagueType !== this.value);
            }
        }
    },

    selectFilterByStatuses(){
        const statuses = document.querySelector('#filter-statuses');
        statuses.addEventListener('change', this.filterByStatuses)
    },

    filterByStatuses(){
        let cards = document.querySelectorAll('.card.league');
        for (let card of cards){
            if (this.value === 'all'){
                card.hidden = false;
            } else {
                card.hidden = (card.dataset.finishedLeague !== this.value);
                }
        }
    }

}

filter.init();