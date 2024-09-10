const http = require('http');

// after every request it will run the callback function
const storedServer = http.createServer((req, res) => {
    console.log("request was made...")
});

// make sure the server is listening
storedServer.listen(3000, 'localhost', () => {
    console.log(`listening for host on localhost:3000`)
})


