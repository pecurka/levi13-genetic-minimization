# Implementation of a Minimization Genetic Algorithm #

## Algorithm Description

The algorithm uses the following:

1. A continuous genetic algorithm
2. BLX-alpha crossover
3. Uniform mutation that uses a random value from the scope
4. The fitness function is the function we are minimizing, in this case the Levi number 13 function:

```
f(x, y) = sin^23πx + (x - 1)^2(1 + sin^23πy) + (y - 1)^2(1 + sin^22πy)
```

## Set Up ##

To set the project up you need to have Python 3 installed on your system. To run it use the command:

```
python main.py
```

## Configuration Parameters ##

All configuration parameters are in the file `config.py`. You can change them to change the way the algoritm functions.

Explanation of the parameters:

```
max_iter = ( int ) - Maximum number of generations
mut_rate = ( float < 1 ) - Rate of mutations
repetitions = ( int ) - Number of experiment repetitions
alpha = ( float < 1 ) - Alpha value for the BLX-a crossover
pop_size = ( int ) - Population size
scope = [ float, float ] - Scope of possible chromosome values
selection_size = ( int ) - Number of individuals we will compare in the selection
fitness_function = func() - The fitness function and the function we are trying to minimize
```

## Results Graph ##

For the following config paramaters:

```
repetitions = 5
max_iter = 500
mut_rate = 0.2
alpha = 0.7
pop_size = 150
scope = [-10, 10]
round_value = 10
```

We get the following graph as a result:

![Result Graph](https://raw.githubusercontent.com/pecurka/levi13-genetic-minimization/master/graph_screenshot.JPG)

As we can see each generation quickly starts convergating towards 0, usually finishing in about 25 generations on average reaching the global minimum of `f(x) = 0` for `x = [1.0, 1.0]`.


## Live Demo with Graphs ##

https://colab.research.google.com/drive/1QYukW55F93UmyfCZO17vpSYpp46Tiqf5
