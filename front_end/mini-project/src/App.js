import React from 'react';
import { Link, Route, Switch } from 'react-router-dom';

import MeditationsList from './components/MeditationsList.js';
import Meditation from './components/Meditation.js';
import MeditationCreate from './components/MeditationCreate.js';
import MeditationEdit from './components/MeditationEdit.js';
import MeditationsHome from './components/MeditationsHome.js';

const App = () => (
	<>
		<header>
			<Link to='/'>Home</Link>
			<Link to='/meditations/create'>Create</Link>
			<Link to='/meditations'>All Meditations</Link>
		</header>
		<main>
			<Switch>
				<Route exact path='/' component={MeditationsHome} />
				<Route exact path='/meditations/create' component={MeditationCreate} />
				<Route exact path='/meditations' component={MeditationsList} />
				<Route exact path='/meditations/:id' component={Meditation} />
				<Route exact path='/meditations/:id/edit' component={MeditationEdit} />
			</Switch>
		</main>
	</>
);

export default App;
