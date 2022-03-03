const roundDetails = {
    init(){
        const id = this.getDataValue('id');
        const roundStatus = this.getDataValue('status');
        console.log(roundStatus)
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
             button.addEventListener('click', initButtonClick)
        } else if (roundStatus === 'started'){

        } else if (roundStatus === 'finished'){

        }

        function initButtonClick(event){
            containerDiv.insertAdjacentHTML(
                "beforeend",
                `<label for="table" class="text-light">Please select the table of this game</label>
                    <select>
                        <option></option>
                    </select>`)
        }
    },

    async fetchData(){
        let response = await fetch('/api/boards');
    },


    renderTable(){
        let containerDiv = document.querySelector('.container');
        console.log(containerDiv)
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
