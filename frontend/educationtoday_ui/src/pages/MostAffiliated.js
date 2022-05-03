import React, { useState } from "react";
import Form from 'react-bootstrap/Form';
import { Button } from "react-bootstrap";
import Card from 'react-bootstrap/Card';
import MostAffiliatedResults from "../components/MostAffiliatedResult";

export default function MostAffiliated() {

	const [affiliationId, setAffiliationId] = useState(0);
	const [toggleResults, setToggleResults] = useState(false);

	const onAffiliationIdChange = ({ target: { value } }) => setAffiliationId(value);
	const onFormSubmit = e => {
		e.preventDefault()
		console.log(affiliationId);
		setToggleResults(true);
	}

	return (
		<div>
			<Card bg="light" style={{ margin: 10 + 'px' }}>
				<Card.Header>
					Most frequent affiliation among all of the co-authors of these authors belonging to an institution.
				</Card.Header>
				<Card.Body>
					<Form onSubmit={onFormSubmit}>
						<Form.Group className="mb-3" controlId="formAffiliationID">
							<Form.Label>Affiliation ID</Form.Label>
							<Form.Control type="number" onChange={onAffiliationIdChange} placeholder="Enter Affiliation ID" />
						</Form.Group>

						<Button variant="primary" type="submit">
							Submit
						</Button>
					</Form>
				</Card.Body>
			</Card>
			{toggleResults &&
				<Card bg="light" style={{ margin: 15 + 'px' }}>
					<MostAffiliatedResults affiliationId={affiliationId} />
				</Card>}
		</div>
	);
}
