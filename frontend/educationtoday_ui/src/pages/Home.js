import React from "react";
import { Link } from "react-router-dom";
import Card from 'react-bootstrap/Card';

export default function Home() {

    return (
        <div>
            <Card bg="light" style={{margin:10 +'px'}}>
                <Card.Header>
                    Welcome to Education Today
                </Card.Header>
                <Card.Body>
                    <Link to='/mostcited'>Find the papers most cited by an Author.</Link><br /><br/>
                    <Link to='/mostaffiliated'>Find the Institutions whose Affiliated authors collaborated the most.</Link>
                </Card.Body>
            </Card>
        </div>
    );
}
