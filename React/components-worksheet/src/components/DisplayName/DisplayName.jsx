import react from 'react';

const DisplayName = props => {
  return (
    <h1>
      {props.firstName} {props.lastName}
    </h1>
  );
};

export default DisplayName;
