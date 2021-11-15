import React, { Component } from 'react';
import './App.css';
import NamesList from './NamesList/NamesList';
import AlertUser from './AlertUser/AlertUser';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      names: ['Mike', 'Nevin', 'Aaron', 'Tory', 'Kellie'],
    };
  }

  handleClick = () => {
    alert('devCodeCamp');
  };

  render() {
    return <AlertUser clickAlert={this.handleClick} />;
  }
}

export default App;
