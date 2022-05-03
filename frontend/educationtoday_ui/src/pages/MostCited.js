import React, { useState } from "react";
import Form from 'react-bootstrap/Form';
import { Button } from "react-bootstrap";
import Card from 'react-bootstrap/Card';
import MostCitedResults from "../components/MostCitedResults";

export default function MostCited() {

	const [authorId, setAuthorId] = useState(0);
	const [topK, setTopK] = useState(1);
	const [toggleResults, setToggleResults] = useState(false);

	const onAuthorIdChange = ({ target: { value } }) => setAuthorId(value);
	const onTopKChange = ({ target: { value } }) => setTopK(value);
	const onFormSubmit = e => {
		setToggleResults(false);
		e.preventDefault()
		console.log(authorId, topK);
		setToggleResults(true);
	}

	return (
		<div>
			<Card bg="light" style={{ margin: 10 + 'px' }}>
				<Card.Header>
					Most Cited articles by Author
				</Card.Header>
				<Card.Body>
					<Form onSubmit={onFormSubmit}>
						<Form.Group className="mb-3" controlId="formAuthorID">
							<Form.Label>Author ID</Form.Label>
							<Form.Control type="number" onChange={onAuthorIdChange} placeholder="Enter Author ID" />
						</Form.Group>

						<Form.Group className="mb-3" controlId="formBasicPassword">
							<Form.Select onChange={onTopKChange} aria-label="Citation count">
								<option>Select the count of Citations</option>
								<option value="5">5</option>
								<option value="10">10</option>
								<option value="15">15</option>
							</Form.Select>
						</Form.Group>

						<Button variant="primary" type="submit">
							Submit
						</Button>
					</Form>
				</Card.Body>
			</Card>

			{toggleResults &&
				<Card bg="light" style={{ margin: 15 + 'px' }}>
					<MostCitedResults authorId={authorId} topK={topK} />
				</Card>}
		</div>
	);
}
