// Arrays 1

const idkArray = [1, 2, 3, 4, 5];

function arrLog(arr) {
  console.log(arr[0]);
  return arr[0];
}

arrLog(idkArray);

// Arrays 2

const colors = ['blue', 'red', 'white', 'green', 'yellow'];

function colorGuess(arr) {
  let userColor = prompt('Enter a color:');
  if (arr.includes(userColor)) {
    console.log('You found my color!');
  } else {
    console.log('Nope!');
  }
}

colorGuess(colors);

// Arrays 3

function sumEvenOdd(arr) {
  let sum = arr.reduce((a, b) => a + b);
  if (sum % 2 === 0) {
    return 'Even';
  } else {
    return 'Odd';
  }
}

console.log(sumEvenOdd(idkArray));

// Arrays 4

function greaterThan(arr, num) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > num) {
      console.log(arr[i]);
    }
  }
}

greaterThan(idkArray, 3);
