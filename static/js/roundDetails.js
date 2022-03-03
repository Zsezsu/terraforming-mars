const roundDetails = {
    init(){
        const id = this.getDataValue('id');
        const roundStatus = this.getDataValue('status');
        console.log(roundStatus)
    },

    getDataValue(dataValue){
        const containerDiv = document.querySelector('.container');
        return containerDiv.getAttribute(`data-${dataValue}`);
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
