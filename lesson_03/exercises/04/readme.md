# Exercise 04

## Introduction

How to use volumes

### Description

Create a few Docker images that can transform an image from original image folder `images/original` and saves it in the folder `images/modified`

There must be Docker images that can do the following:
- rotate image by 90 degrees clockwise
- flip image horizontally

For image modification it is possible to use [ImageMagick CLI](https://imagemagick.org/script/command-line-processing.php)

### Requirements for Completion
- After running the Docker image for rotating images with `images` folder as Mounted folder, there should be a rotated image in the `images/modified` folder. 
- After running the Docker image for flipping images with `images` folder as Mounted folder, there should be a flipped image in the `images/modified` folder

### Bonus difficulty (optional)

Create a single image for both functions. Add the choice of transformation as an additional parameter
