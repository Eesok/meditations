import React, { Component } from 'react';
import { Link, Redirect } from 'react-router-dom';
import { APIURL } from '../config.js';

class Meditation extends Component {
	constructor() {
		super();

		// initialize our state to make the constructor useFUL
		this.state = {
			meditation: null,
			deleted: false,
			error: false,
		};
	}

	componentDidMount() {
		const url = `${APIURL}/meditations/${this.props.match.params.id}`;
		fetch(url)
			.then((response) => response.json())
			.then((data) => {
				// Update state with successful meditation data
				this.setState({ meditation: data });
			})
			.catch(() => {
				// Update the state if there was an error
				// so we can give feedback to the user!
				this.setState({ error: true });
			});
	}

	onDeleteMeditation = (event) => {
		const url = `${APIURL}/meditations/${this.props.match.params.id}`;
		fetch(url, { method: 'DELETE' })
			.then((res) => {
				this.setState({ deleted: true });
			})
			.catch(console.error);
	};

	render() {
		// If we deleted the meditation, redirect back to the meditations list
		if (this.state.deleted) {
			return <Redirect to='/meditations' />;
		}

		// Check if there was an error
		// If there is give the user feedback!
		if (this.state.error) {
			return <div>Sorry, there was a problem getting the meditations</div>;
		}

		// Check if we have our meditations
		// Display "Loading..." if not
		if (!this.state.meditation) {
			return <div>Loading...</div>;
		}

		// If none of the if statements ran
		return (
			<div>
				<h3>Practice: {this.state.meditation.practice}</h3>
				<p>Origin: {this.state.meditation.origin}</p>
				<button onClick={this.onDeleteMeditation}>Delete Meditation</button>
				<Link to={`/meditations/${this.props.match.params.id}/edit`}>
					Update Meditation
				</Link>
			</div>
		);
	}
}

export default Meditation;
