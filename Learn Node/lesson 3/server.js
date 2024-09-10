const http = require('http');
const fs = require('fs');
const path = require('path');


// after every request it will run the callback function
const storedServer = http.createServer((req, res) => {
    console.log(req.url, req.method);
    
    res.setHeader('Content-Type', 'text/html');

    let path = './'
    switch(req.url) {
        case '/':
            path += 'index.html';
            break;
        case '/about':
            path += 'about.html';
            break;
        default:
            path += '404.html';
            break;
    }

    fs.readFile(path, (err, data) => {
        if (err) {
            console.log(err);
            res.end()
        } else {
            res.end(data)
    }
    })
});

// make sure the server is listening
storedServer.listen(3000, 'localhost', () => {
    console.log(`listening for host on localhost:3000`)
})


