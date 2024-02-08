// # Given an array of integers.

// # Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

// # If the input is an empty array or is null, return an empty array.

// # Example
// # For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

function countPositiveAndSumNegative(numbers) {
  let countPositive = 0; // Number of positive and negative numbers in the array
  let sumNegative = 0; // Number of negative numbers in the array

  for (let number of numbers) {
    if (number > 0) {
      countPositive++;
    } else if (number < 0) {//
      sumNegative += number;
    }
    // Ignore 0, as it is neither positive nor negative
  }

  return [countPositive, sumNegative];
}

// Example usage
let testData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15];
console.log(countPositiveAndSumNegative(testData));