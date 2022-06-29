const filter = {
    init(){
        this.filterByGameType()
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
    }
}

filter.init();