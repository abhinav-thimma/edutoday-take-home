import React, { useState } from "react";
import Table from 'react-bootstrap/Table';

class MostAffiliatedResults extends React.Component {
    constructor(props) {
        super(props);
        this.state = { response: [] };
    }

    componentDidMount() {
        fetch('http://127.0.0.1:5000/mostaffliated?affiliationId=' + this.props.affiliationId, {
            'method': 'get',
            'headers': { 'Access-Control-Allow-Origin': '*', 'Accept': 'application/json' }
        })
            .then(response => response.json())
            .then(data => this.setState({ response: data }));
    }

    render() {

        // iterating over response entries and creating table row components
        let entries = this.state.response.map((entry, i) => (
            <tr>
                <td>{entry['affiliationId']}</td>
                <td>{entry['count']}</td>
            </tr>
        ));

        return (
            <div>
                <Table striped bordered hover>
                    <thead>
                        <tr>
                            <td>Affiliation ID</td>
                            <td>Number of Affiliations</td>
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

export default MostAffiliatedResults;