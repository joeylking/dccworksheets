import React, { Component } from 'react';
import './App.css';
import SuperheroTable from './SuperheroTable/SuperheroTable';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      superheroes: [
        {
          superheroId: 1,
          name: 'Batman',
          primaryAbility: 'Wealthy',
          secondaryAbility: 'Rich',
        },
        {
          superheroId: 2,
          name: 'Superman',
          primaryAbility: 'Super strength',
          secondaryAbility: 'Fly',
        },
        {
          superheroId: 3,
          name: 'Spiderman',
          primaryAbility: 'Spider senses',
          secondaryAbility: 'Shoots web',
        },
      ],
    };
  }

  handleClick = () => {
    alert('devCodeCamp');
  };

  render() {
    return <SuperheroTable superheroes={this.state.superheroes} />;
  }
}

export default App;
