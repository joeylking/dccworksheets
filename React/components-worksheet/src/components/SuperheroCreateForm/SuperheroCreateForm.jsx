import React, { Component } from 'react';

class SuperheroCreateForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      name: '',
      primaryAbility: '',
      secondaryAbility: '',
    };
  }

  handleChange = event => {
    this.setState({
      [event.target.name]: event.target.value,
    });
  };

  handleSubmit = event => {
    event.preventDefault();
    this.props.addHero(this.state);
  };

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label htmlFor=''>Superhero Name</label>
        <input
          name='name'
          onChange={this.handleChange}
          type='text'
          value={this.state.name}
        />
        <label htmlFor=''>Primary Ability</label>
        <input
          name='primaryAbility'
          onChange={this.handleChange}
          type='text'
          value={this.state.primaryAbility}
        />
        <label htmlFor=''>Secondary Ability</label>
        <input
          name='secondaryAbility'
          onChange={this.handleChange}
          type='text'
          value={this.state.secondaryAbility}
        />
        <button type='submit'>Create Superhero</button>
      </form>
    );
  }
}

export default SuperheroCreateForm;
