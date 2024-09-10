const fs = require('fs')

const readStream = fs.createReadStream('./test_folder/blog.txt', { encoding: 'utf8' })
const writeStream = fs.createWriteStream('./test_folder/blog.txt2')

// manually piping
readStream.on('data', (chunk) => { // the .on will listen to data events on the readStream
    console.log("------- NEW CHUNK -------")
    console.log(chunk)
    writeStream.write('\nNEW CHUNK\n')
    writeStream.write(chunk)
})

// piping
readStream.pipe(writeStream);