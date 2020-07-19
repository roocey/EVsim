# simbox
super simple python project to mess with simulations

Simple example of how simbox works: imagine you have a bag with five balls, each with a different color. Let's say we want to every unique combination of two balls. A little bit of math here tells us there will be 25 combinations. Now, how many times will we have to pull two balls from the bag to find all 25 combinations, assuming we put all of the balls back in the bag each time? This, in essence, is the question simbox is designed to answer -- by simulating this hundreds, thousands, or even millions of times!

TODO:

1. Make it faster (set variables once, move away from lists and repetitive ifs)
2. Detach "colors" and make a simple UI to set combination parameters [detached colors]
3. Allow for different combination paramters other than (len * (len-1)) [mostly done]
4. Introduce meta level higher-order class to simulate simulations, test speed differences between different complexities, and so on.
