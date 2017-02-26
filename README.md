# Stock Analysis

## Work in progress

Most of this comes from a [youtube tutorial series](https://youtu.be/URTZ2jKCgBc?list=PLQVvvaa0QuDd0flgGphKCej-9jp-QdzZ3). I'm aiming to modularize the completed tutorial and refactor the code for more reusability. After, I'll be adding my own usage to find new insights, and demonstrate understanding.

## Current usage

Python 3.4

Most of these functions rely on CSV files being in the `/data` folder, and then a master CSV that is aggregated in the root. Use the functions defined in the `/get_data` folder.

The primary value of this repo is the `/train` folder. This uses the "sp500_joined_closes.csv" to look at 7 day samples of the entire sp500 closing costs and see if the specified ticker goes up or down ~2%. Currently has ~38% accuracy. 
