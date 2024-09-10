// fs is file system
const fs = require('fs')

// // reading files
// fs.readFile('./test_folder/read.txt', (err, data) => { // asyncronous, takes time
//     if (err) {
//         console.log(err)
//     }
//     console.log(data.toString())
// })

// console.log('last line')

// // writing files
// fs.writeFile('./test_folder/read.txt1', 'hello ninja', () => {
//     console.log('file was written!')
// })

// // directories
// if (!fs.existsSync('./assets')) {
//     fs.mkdir('./assets', (err) => {
//         if (err) {
//             console.log(err);
//         }
//         console.log('folder created');
//     });
// } else {
//     fs.rmdir('./assets', (err) => {
//         if (err) {
//             console.log(err)
//         } 
//         console.log('folder deleted')
//     })
// }

// deleting files
if (fs.existsSync('./test_folder/read.txtw')) {
    fs.unlink('./test_folder/read.txt', (err) => {
        if (err) {
            console.log(err);
        }
        console.log('file deleted')
    })
}