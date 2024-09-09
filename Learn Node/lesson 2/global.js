// Global objects

console.log(global)

const timeout = setTimeout(() => {
    console.log('hello');
    clearInterval(int)
}, 4000)

// clearTimeout(timeout); // cancels the timeout

number = 1;
const int = setInterval(() => {
    console.log(number);
    number += 1;
}, 1000)

console.log(__dirname);
console.log(__filename)