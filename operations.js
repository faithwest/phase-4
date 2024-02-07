function number(value) {
    return function(operation) {
        return operation ? operation(value) : value;
    };
}

function operation(func) {
    return func;
}

const zero = number(0);
const one = number(1);
const two = number(2);
const three = number(3);
const four = number(4);
const five = number(5);
const six = number(6);
const seven = number(7);
const eight = number(8);
const nine = number(9);

// Define operation instances
const plus = operation(x => y => x + y);
const minus = operation(x => y => x - y);
const times = operation(x => y => x * y);
const dividedBy = operation(x => y => Math.floor(x / y));

console.log(seven(times(five())));    // Output: 35
console.log(four(plus(nine())));      // Output: 13
console.log(eight(minus(three())));   // Output: 5
console.log(six(dividedBy(two())));   // Output: 3
