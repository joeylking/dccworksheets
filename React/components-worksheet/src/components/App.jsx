import React, { Component } from 'react';
import './App.css';
import SuperheroTable from './SuperheroTable/SuperheroTable';
import SuperheroCreateForm from './SuperheroCreateForm/SuperheroCreateForm';

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

  addHero = newHero => {
    newHero.superheroId = this.state.superheroes.length + 1;
    this.state.superheroes.push(newHero);
    console.log(this.state.superheroes);
  };

  render() {
    return (
      <>
        <SuperheroTable superheroes={this.state.superheroes} />
        <SuperheroCreateForm
          superheroes={this.state.superheroes}
          addHero={this.addHero}
        />
      </>
    );
  }
}

export default App;
