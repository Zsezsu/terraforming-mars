const roundDetails = {
    init(){
        const id = this.getRoundId();
        this.renderTable();
    },

    getRoundId(){
        const containerDiv = document.querySelector('.container');
        return containerDiv.getAttribute('id');
    },

    renderTable(){
        let containerDiv = document.querySelector('.container');
        console.log(containerDiv)
        let table = this.htmlFactory();
        containerDiv.innerHTML = table;
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
