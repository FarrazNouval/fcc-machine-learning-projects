# Rock Paper Scissors

This project is the first project in the freecodecamp machine learning course. This project is entitled Rock Paper Scissor. The goal is to win a game of rock paper scissor against 4 bots with a win percentage of at least 60%.<br><br>
The interesting thing about this project is that we are asked to beat 4 bots in the game, and each bot has a different behavior.<br><br>
1. The first bot uses the index pattern, with the index being the remainder of the quotient of the number of previous rounds with the length of the list of options. The options are [R, R, P, P, S]. So as long as it hasn't reached round 6, he will still choose the 'R' rock. After that, it will be determined based on the index. This bot can be said to be easy to guess its pattern. <br><br>
2. The second bot uses the strategy of reading our playing history in the last 10 rounds; if the game has not reached 10 rounds then it will choose 'S' scissors. If the game has reached 10 rounds, this bot will read our history of playing for the last 10 rounds and then guess the next choice we will make, by taking the most choices we chose in the last 10 rounds, if in the last 10 rounds we often choose rock then it will chose the paper, because he guessed that we would pick the stone again.<br><br>
3. The third bot uses the strategy of reading our game history in the previous 1 round.<br><br>
4. The last bot uses the strategy of reading our game history in the previous 2 rounds.<br><br>

guess what strategy I used to beat them all hehehe.<br>
