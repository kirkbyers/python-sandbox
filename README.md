# Python Projects

## Work in progress

This is just a collection of python projects. They are mostly Jupyter notebooks

Projects that do more than satisfy my curriosity will be moved to standalone repos.

## Current usage

Python 3.4

Projects reference data in the `/data` folder, or then a CSV that is aggregated in the root if file size is reasonable.

## Projects

### Stocks

 Most of this comes from a [youtube tutorial series](https://youtu.be/URTZ2jKCgBc?list=PLQVvvaa0QuDd0flgGphKCej-9jp-QdzZ3). I'm aiming to modularize the completed tutorial and refactor the code for more reusability. After, I'll be adding my own usage to find new insights, and demonstrate understanding.

 The bulk of this project is currently scattered throughout the root.

 This uses the "sp500_joined_closes.csv" to look at 7 day samples of the entire sp500 closing costs and see if the specified ticker goes up or down ~2%. Currently has ~38% accuracy which is slightly better than randomly guessing to buy, sell, or wait on a given comapny.

 ### Fast.ai

 Based off of week 6 of the fast.ai course. 
 
 Uses TensorFlow building up Long Short Term Memory Layers to create a neural net to create a text generator based of the H. P. Lovecraft story "The Call of Cthulu".
