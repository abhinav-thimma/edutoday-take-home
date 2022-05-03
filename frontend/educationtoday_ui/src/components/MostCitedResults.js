import React, { useState } from "react";
import Table from 'react-bootstrap/Table';

class MostCitedResults extends React.Component {
    constructor(props) {
        super(props);
        this.state = { response: [] };
    }

    componentDidMount() {
        const authorId = this.props.authorId;
        const topK = this.props.topK? this.props.topK: 10;

        fetch('http://127.0.0.1:5000/mostcited?authorId='+authorId+'&topK='+topK, {
            'method': 'get',
            'headers': { 'Access-Control-Allow-Origin': '*', 'Accept':'application/json' }
        })
            .then(response => response.json())
            .then(data => this.setState({ response: data }));
    }

    render() {
        
        // iterating over response entries and creating table row components
        let entries = this.state.response.map((entry, i) => (
            <tr>
                <td>{entry}</td>
            </tr>
        ));

        return (
            <div>
                <Table striped bordered hover>
                    <thead>
                        <tr>
                            <td>Paper Title</td>
                        </tr>
                    </thead>
                    <tbody>
                        {entries}
                    </tbody>
                </Table>
            </div>
        );
    }
}

export default MostCitedResults;