# Testing the NEAT Algorithm with Chrome's Dinosaur Game
This project was a simple attempt at experimenting with the NEAT (Neuro-Evolution of Augmenting Topologies) Algorithm in Python through the Dinosaur Chrome Game.

**Disclaimer: Most of the code within this repository is adapted from the following tutorial: https://www.youtube.com/watch?v=CKFCIzPSBjE&ab_channel=CodeBucket**
**The code in this repository makes notable changes to some areas, including the extended functionality of exporting the best genome as well as the crouching function of the Dinosaur**

The NEAT algorithm can be defined as an algorithm that continuously generates neural networks of succeeding generations. 
It's a very popular choice when trying to develop an AI to perform simple tasks through multiple trial and errors of the task.

The GIF below displays how a neural network with two hidden layers functions.

![A short gif on how a neural network works](./Images/neural_net.gif)

## The Game

The game is fairly simple and I'm fairly certain that any individual who has lost wifi connection on Chrome has probably played this game. But in case you HAVEN'T, then here's a short description.

![Short Photo of Algorithm in Action in Game](./show_game.png)

The game involves you, yes you, being a dinosaur running down a track. On the track there will be obstacles such as cacti and birds, that the dinosaur will need to dodge to stay alive. In this implementation of the game, we use **SPACEBAR** to dodge and **L-CTRL** to crouch. And that's basically it. In order to play this game manually, open the **main.py** python file and edit the machine_play variable.

```python
machine_play = False # Set to True instead if you want to visualise the NEAT Algorithm in action!
```

## The Algorithm (In Short)

![Short Photo of Algorithm in Action in Game](./show_algorithm_game.png)



## Results
