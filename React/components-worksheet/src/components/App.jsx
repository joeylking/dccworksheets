import React, { Component } from 'react';
import './App.css';
import DisplayName from './DisplayName/DisplayName';

class App extends Component {
  constructor(props) {
    super(props);
    this.books = [
      { title: 'Ready Player One', author: 'Ernest Cline' },
      { title: 'All the Light We Cannot See', author: 'Anthony Doerr' },
      { title: 'The First and Last Freedom', author: 'Jiddu Krishnamurit' },
    ];
    this.state = {
      firstName: 'Reggie',
      lastName: 'White',
    };
  }

  render() {
    return (
      <DisplayName
        firstName={this.state.firstName}
        lastName={this.state.lastName}
      />
    );
  }
}

export default App;
