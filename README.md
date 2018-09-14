# Maze + big maze

A purple dot is at the position shown in the figure below. Every second it will move at random along one of its adjacent "roads" (the edges of the graph). Once it has reached either a green or a red square it stops. As we can see, at every incidence point it has 3 options. What is the probability that it will eventually end in one of the green squares?

![small_hex_ant.png](small_hex_ant.png)

## Run

* Create a virtual environment `virtualenv env` and activate `source env/bin/activate`.
* Install dependencies `pip3 install -r requirements.txt`
* Run code for 10 million iterations `python3 ./random-walk-graph.py`

## Solution

This assumes a random choice is being made at every intersection. Probability of reaching green is 0.1109578
