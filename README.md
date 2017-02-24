# Stock Analysis

## Work in progress

Most of this comes from a [youtube tutorial series](https://youtu.be/URTZ2jKCgBc?list=PLQVvvaa0QuDd0flgGphKCej-9jp-QdzZ3). I'm aiming to modularize the completed tutorial and refactor the code for more reusability. After, I'll be adding my own usage to find new insights, and demonstrate understanding.

## Current usage

Currently there is no use of "virtualenv". I think the main dependencies are pretty common, and compatible with a number of different versions. I'll be adding virtualenv in the future to manage this better. 

This repo is written python 2.7. I don't anticipate any issues moving to 3, but that isn't something I've move to yet. I'll be moving to python 3.6 soon.

Most of these functions rely on CSV files being in the `/data` folder, and then a master CSV that is aggregated in the root. Use the functions defined in the `/get_data` folder.
