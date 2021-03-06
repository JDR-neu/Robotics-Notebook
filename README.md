# Robotics-Notebook

- [Path Planning](#Path-Planning)
  - [Dijkstra](#Dijkstra)
  - [A*](#AStar)
  - [Potential Field](#Potential-Field)
  - [RRT](#RRT)
  - [RRT*](#RRTStar)
  - [RRT* Smart](#RRTStarSmart)
  - [Qlearning](#Qlearning)

## Path Planning

### Dijkstra

<img src="PathPlanning/Dijkstra/Dijkstra.png" width="450" height="350">

*Reference*:

[Dijkstra's algorithm - Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

### A* <a name="AStar"></a>

<img src="PathPlanning/AStar/AStar.png" width="450" height="350">

*Reference*:

[A* search algorithm - Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm)

### Potential Field

<img src="PathPlanning/PotentialField/PotentialField.png" width="450" height="350">

*Reference*:

[Robotic Motion Planning: Potential Functions](https://www.cs.cmu.edu/~motionplanning/lecture/Chap4-Potential-Field_howie.pdf)

### RRT
<img src="PathPlanning/RRT/RRT.png" width="450" height="350">

*Reference*:

[Rapidly-Exploring Random Trees: A New Tool for Path Planning](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.35.1853)

### RRT* <a name="RRTStar"></a>
<img src="PathPlanning/RRTStar/RRTStar.png" width="450" height="350">

*Reference*:

[Sampling-based algorithms for optimal motion planning](https://journals.sagepub.com/doi/abs/10.1177/0278364911406761)

### RRT* Smart <a name="RRTStarSmart"></a>

<img src="PathPlanning/RRTStarSmart/RRTStarSmart.png" width="450" height="350">

*Reference*:

[RRT*-SMART: A Rapid Convergence Implementation of RRT*](https://journals.sagepub.com/doi/pdf/10.5772/56718)

[A Comparison of RRT, RRT* and RRT*-Smart Path Planning Algorithms](http://paper.ijcsns.org/07_book/201610/20161004.pdf)

### Qlearning

<img src="PathPlanning/Qlearning/qlearning.gif" width="450" height="350">

*Reference*:

[**Path Planning with qlearning**](<https://github.com/0aqz0/path-planning-with-qlearning>)

## Getting Started

```bash
$ git clone git@github.com:0aqz0/Robotics-Notebook.git
$ cd Robotics-Notebook
$ virtualenv.exe venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
$ pip install -e .
$ python PathPlanning/AStar/run.py
```
