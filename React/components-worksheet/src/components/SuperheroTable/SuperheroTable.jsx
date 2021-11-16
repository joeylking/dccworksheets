import react from 'react';
import './SuperheroTable.css';

const SuperheroTable = props => {
  console.log(props.superheroes);
  return (
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Primary Ability</th>
          <th>Secondary Ability</th>
        </tr>
      </thead>
      <tbody>
        {props.superheroes.map(superhero => (
          <tr key={superhero.superheroId}>
            <td>{superhero.name}</td>
            <td>{superhero.primaryAbility}</td>
            <td>{superhero.secondaryAbility}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default SuperheroTable;
