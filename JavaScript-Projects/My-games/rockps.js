const PromptSync = require("prompt-sync");

const prompt = require("prompt-sync")();

let wins = 0;
let losses = 0;
let draws = 0;
let antiwins = 0;
let antilosses = 0;
let antidraws = 0;

while (true) {
    while (true) {
        const choice = prompt("Enter rock, paper or scissors: ");
        if (choice === "q") {
            break;
        }
        
        
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
            antidraws++;
        } else if (
            (choice === "paper" && computerChoice === "rock") ||
            (choice === "rock" && computerChoice === "scissors") ||
            (choice === "scissors" && computerChoice === "paper")
        ) {
            console.log("You won!");
            wins++;
            antiwins++;
        } else {
            console.log("You lost!");
            losses++;
            antilosses++;

        }

        console.log("Wins",wins + ", Losses", losses + ", Draws," + draws);
    
        if (
            (wins === 3) ||
            (losses === 3)
        ) {
            break;
        } else {
            continue;
        }
    }

    if (wins === 3) {
        console.log("Great job, you beat the computer!");
    } else {
        console.log("come on, how do you lose to a computer?");
    }

    const replay = prompt("Would you like to play again (y/n)? ")

    if (replay === "y") {
        wins = 0;
        losses = 0;
        draws = 0;
        continue;
    } else {;
        break;
    }
}