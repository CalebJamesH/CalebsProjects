const PromptSync = require("prompt-sync");

const prompt = require(PromptSync)

const answer = prompt("The princess has been captured and is locked in a castle. Are you willing to save her (y/n)? ")

if (answer.toLowerCase() === "y") {
    const answer1 = prompt("You're on your mission and you arrive to a cliff. You see an old bridge and a fallen tree. The old bridge seems as if it has weak ropes and is about to fall, and the fallen tree seems old and rotten. would you like to cross through the bridge or tree (bridge/tree) ")

        if (answer1.toLowerCase === "bridge") {
            console.log("Oh no!The ropes ripped and you fell down the cliff and died, game over!")
        } else {
            console.log("nice! the tree barely held you.")
            const answer2 = prompt("You have crossed the tree and start heading down the road. After some time you reach a dark forest and you have two choices, cross it or find another way. What will you choose (cross/another)? ")
        }

        if (answer2 === cross) {
            const answer3 = prompt("You're crossing the dark forest and all of a sudden a spider jumps out at you, what do you do?")
        } else {
            console.log("you're walking and a scorpion stung you. You lose!")
        }
        





} else {
    console.log("That sucks but I already knew you were weak")
}