# maxoverhang

##Directions on How to Use:
In order to use the max overhang simulator, you must press ‘A’ to generate as many blocks as you want and then click and drag individual blocks such that they are stacked upon each other in order to attempt achieving the maximum overhang.
* Press ‘C’ to display the center of mass of each block and the entire stack, as well as messages showing the instability of the stack,
* Press ‘D’ to turn them off,
* Press ‘A’ to add a block,
* Press ‘S’ to remove one,
* Press ‘G’ to show forces of gravity,
* Press ‘H’ to turn them off,
* Press ‘N’ to show normal forces,
* Press ‘M’ to turn them off,
* and press L to check if you win, requiring center of masses to not be displayed,
(you win if the stack is balanced and your overhang is >=95% of the max overhang)
Note: if you adjust the blocks and then add or remove a block, it will reset the entire configuration of blocks to a vertical stack.

##Explanation of the Program:
	When “total com fail” appears on the right side of the screen, this indicates that the x-coordinate of the center of mass of the entire stack is over the edge of the table, which would result in the entire stack of blocks toppling over in real life. When “substack com fail” appears, this shows that individual blocks are not supported adequately by the stack.
	In addition, the line that appears on the screen when blocks are generated illustrates the maximum overhang given a number of blocks. The fraction in the bottom right shows how close the user is (in pixels) to achieving this maximum overhang.

##Mathematical/Physical Basis for the Overhang Problem:
	If a stack of “n-1” blocks are perfectly balanced with the maximum overhang possible, then the center of mass of the entire stack will be directly above the table edge. If you add the “nth” block to the bottom, then the entire center of mass has to be shifted towards the left a distance of 1/2n in order to achieve the maximum overhang for the new stack. Lastly, the maximum overhang for a stack of a single block is 1/2 because its individual com would be above the table. Thus, the maximum overhang is calculated as Overhang = ![equation](https://latex.codecogs.com/gif.latex?%5Csum_%7Bn%3D1%7D%5En%20%5Cfrac%7B1%7D%7B2i%7D%28%5Ctext%7Blength%20of%20blocks%7D%29)
