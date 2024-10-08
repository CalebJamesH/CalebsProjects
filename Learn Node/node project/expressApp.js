const express = require('express')
const morgan = require('morgan')

// express app
const app = express();

app.set('view engine', 'ejs')

app.listen(3000);

// middleware & static files
app.use(express.static('public'));
app.use(morgan('dev'));

app.get('/', (req, res) => {
	const blogs = [
		{title: 'Yoshi finds eggs', snippet: 'Lorem ipsum dolor sit amet consectetur'},
		{title: 'Mario finds stars', snippet: 'Lorem ipsum dolor sit amet consectetur'},
		{title: 'How to defeat Bowser', snippet: 'Lorem ipsum dolor sit amet consectetur'}
	]
	res.render('index', { title: 'Home', blogs })
});

app.get('/about', (req, res) => {
	res.render('about', { title: 'About'})
});

app.get('/blogs/create', (req, res) => {
	res.render('create', { title: 'Create a new Blog'})
})

// 404 page
app.use((req, res) => {
	res.render('404', { title: '404'})
})