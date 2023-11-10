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


const percent = Math.round((correctAnswers / totalQuestions) * 100);

const grade = ("you got " + percent + "%!")

console.log(grade);

if (percent >= 99) {
   console.log("Wow, you got 100%! That is incredible! You must be a great friend of my Master. I hope you know my Master is very happy with how much you know him and he really needs to start treating you better");
} else if (percent >= 87){
    console.log("You did a pretty good job. You must be a great friend of his!");
} else if (percent >= 75) {
    console.log("ok ok, not too bad. you could still get to know him bettter");
} else if (percent >= 50) {
    console.log("You need to start spending more time with my master.");
} else {
    console.log("Wow! You are a bad friend. Do you even know my master?")
}