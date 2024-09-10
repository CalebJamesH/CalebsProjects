const http = require('http');
const fs = require('fs');

http.createServer((req, res) => {
  if (req.url === '/style.css') {
    // Send the CSS file
    fs.readFile('style.css', (err, data) => {
      res.writeHead(200, { 'Content-Type': 'text/css' });
      res.end(data);
    });
  } else {
    // Send the HTML file (browser will automatically ask for the CSS file after)
    fs.readFile('index.html', (err, data) => {
      res.writeHead(200, { 'Content-Type': 'text/html' });
      res.end(data);
    });
  }
}).listen(3000);
