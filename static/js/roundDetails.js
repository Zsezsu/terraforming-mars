import {dataHandler} from "./data/dataHandler.js";

const roundDetails = {
    init(){
        const id = this.getDataValue('id');
        const roundStatus = this.getDataValue('status');
        this.pageControl(roundStatus)
    },

    getDataValue(dataValue){
        const containerDiv = document.querySelector('.container');
        return containerDiv.getAttribute(`data-${dataValue}`);
    },

    pageControl(roundStatus){
        const containerDiv = document.querySelector('.container');
        if (roundStatus === 'init_round'){
             containerDiv.insertAdjacentHTML('afterbegin', `<button id="init">Init round</button>`);
             let button = document.querySelector('#init');
             button.addEventListener('click', this.initButtonClick.bind(this))
        } else if (roundStatus === 'started'){

        } else if (roundStatus === 'finished'){

        }

    },

    async initButtonClick(event){
        let button = event.currentTarget;
        button.hidden = 'True';
        const containerDiv = document.querySelector('.container');
        let boards =  await dataHandler.getBoards();
        let optionHTML = ''
        for (let board of boards){
            optionHTML += `<option id="${board['id']}">${board['board_name']}</option>`
        }
        containerDiv.insertAdjacentHTML(
            "beforeend",
            `<label for="table" class="text-light">Please select the table of this game</label>
                <select id="select-board">
                    ${optionHTML}
                </select>`);
        let select = document.querySelector('#select-board');
        select.addEventListener('select', this.selectEvent.bind(this))

    },


    selectEvent(event){
        let value = event.currentTarget.value;

    },

    renderTable(){
        let containerDiv = document.querySelector('.container');
        containerDiv.innerHTML = this.htmlFactory();
    },

    htmlFactory(){
        return `
        <table class="text-light">
            <thead>
            <tr>
                <th>Name</th>
                <th>Corporation</th>
                <th>TR number</th>
                <th>Milestone points</th>
                <th>Award points</th>
                <th>Own greeneries</th>
                <th>Cities</th>
                <th>Greeneries around cities</th>
                <th>Victory points on cards</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <td>0</td>
            </tr>
            </tbody>
        </table>
        `

    }
}

roundDetails.init();
