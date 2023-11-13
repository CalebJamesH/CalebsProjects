const prompt = require("prompt-sync")();

let wins = 0;
let losses = 0;
let draws = 0;

while (true) {
    const choice = prompt("Enter rock, paper or scissors: ");
    if (choice !== "rock" && 
    choice !== "paper" && 
    choice !== "scissors"
    ) {
    console.log("Do you not know how to spell? Enter a valid choice");
    continue;
    } 

    const choices = ["rock", "paper", "scissors"];
    const randomIndex = Math.round(Math.random() * 2 );
    const computerChoice = choices[randomIndex];


    console.log("The computer chose", computerChoice);

    if (computerChoice === choice) {
        console.log("Draw!");
        draws++;
    } else if (
        (choice === "paper" && computerChoice === "rock") ||
        (choice === "rock" && computerChoice === "scissors") ||
        (choice === "scissors" && computerChoice === "paper")
    ) {
        console.log("Won!");
        wins++;
    } else {
        console.log("You lost!")
        losses++;
}

console.log("Wins",wins + ", Losses", losses + ", Draws," + draws)
}
