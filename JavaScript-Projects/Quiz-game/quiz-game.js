const prompt = require("prompt-sync")();

console.log("Welcome to this awesome quiz created by Caleb. How well do you know him?");

let correctAnswers = 0;
const totalQuestions = 8;

// Question 1
const answer1 = prompt("What is my Master's favorite color? ");
const correct_answer1 = "GREEN";

if (answer1.toUpperCase() === correct_answer1) {
    console.log("You got it right!");
    correctAnswers++;
} else {
    console.log("you got it wrong! Do you actually know my Master?");
}

// Question 2
const answer2 = prompt("What is my Master's favorite sport? ");
const correct_answer2 = "SOCCER";

if (answer2.toUpperCase() === correct_answer2) {
    console.log("good job! you got the easy one right.");
    correctAnswers++;
} else {
    console.log("You got it wrong! Like... come on! how could you get that wrong?");
}


// Question 3
const answer3 = prompt("What is my Master's favorite food? ");
const correct_answer3 = "CHURASCO";

if (answer3.toUpperCase() === correct_answer3) {
    console.log("good job! You might actually get a good score.");
    correctAnswers++;
} else {
    console.log("you got it wrong! yeah, that one's a little harder.");
}


// Question 4
const answer4 = prompt("What is my Master's favorite animal? ");
const correct_answer4 = "CHAMELEON";

if (answer4.toUpperCase() === correct_answer4) {
    console.log("good job! Dang... that one was really hard, you're a pretty good friend of my Master.");
    correctAnswers++;
} else {
    console.log("you got it wrong! yeah... I didn't think you'd get that one.");
}


// Question 5
const answer5 = prompt("Where does my Master Want to live when he grows up? A: Virginia  B: Recife  C:  Texas  D: He doesn't know yet (Answer by letter) ");
const correct_answer5 = "D";

if (answer5.toUpperCase() === correct_answer5) {
    console.log("You got it right! It's probably cause of you that my Master is unsure of where he'll live.");
    correctAnswers++;
} else {
    console.log("you got it wrong! You should re-check how much you my Master");
}


// Question 6
const answer6 = prompt("When is my Master's birthday? (using numbers i.e 23/11/2023) ");
const correct_answer6 = "02/09/2005";

if (answer6.toUpperCase() === correct_answer6) {
    console.log("DANG bro! Great Job, you've just made my master very happy.");
    correctAnswers++;
} else {
    console.log("You got it wrong! Like... come on! how could you get that wrong?");
}


// Question 7
const answer7 = prompt("What color belt is my Master in jiu-jitsu? A: White  B: Orange  C:  Green  D: Blue (Answer by letter) ");
const correct_answer7 = "A";

if (answer7.toUpperCase() === correct_answer7) {
    console.log("You got it!");
    correctAnswers++;
} else {
    console.log("Nope! :(");
}


// Question 8
const answer8 = prompt("Who is my Master's best friend? ");
const correct_answer8 = "SOLLIE";

if (answer8.toUpperCase() === correct_answer8) {
    console.log("Good job!");
    correctAnswers++;
} else {
    console.log("Nope!");
}


console.log("you got", correctAnswers, "out of", totalQuestions, "which is", correctAnswers / totalQuestions * 100, "percent")


// answer time 


