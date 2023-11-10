const prompt = require("prompt-sync")();

let playag = "YES"

while (playag = "YES") {

    const target = Math.round(Math.random() * 100);

    let guesses = 0;

    while (true) {
        guesses++;

        const guess = Number(prompt("Guess the number (0-100): "))
        if (guess > target) {
            console.log("Your guess is too high.");
        } else if (guess < target) {
            console.log("Your guess is too low.");
        } else {
            console.log("You got it you dingus!");
            break;
        } 
    }

    console.log("You guessed the answer in", guesses, "tries!");

    let replay = prompt("would you like to play again? (type yes/no) ") ;

    if (replay.toUpperCase() !== "YES") {
        break;
    }

}    


