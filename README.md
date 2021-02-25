My Sudoku solver that uses human strategies

My goal was to make the strategies readable as well as what a human would be possible of doing.
I didn't want to do any brute force methods or guessing methods.

My strategies could be refactored and cleaned up for sure. 
They currently use a bunch of for loops because I was implementing what my brain does when solving these puzzles and of course my brain doesn't have the fancy iterables that python does. 

I didn't want to look at anyone else's solver or look at [sudoku strategy wikis](https://www.sudokuwiki.org/Naked_Candidates) until after I had implemented what I do to solve the puzzles.
I didn't implement the naked/hidden triples/quads though.

I did take the boards.txt file from
https://github.com/roukaour/sudoku
after I finished my implementation. 
It provided a bunch of puzzles to try to solve.

As of 24 Feb 2021, the following strategies were implemented

* naked singles
* hidden singles
* naked twins 
* hidden twins
* unit intersection

It solved 40432/49606 (81.5%) of the boards.txt and took 3.5 hrs (12543 s) to run on my system for an average runtime of 253 ms per puzzle.
I am pretty satisfied with its current state. I may come back again another time and add some more strategies or refactor the for loops using iterables