# Image Steganography

On different occasions, people want to store data in some safe way or in a safe place where it is difficult for others to access. Many people save valuable data like **sensitive/important text**, **Passwords** or **Seed Phrase** of a wallet in an Excel file, txt File or even block notes, which is obviously insecure.

The purpose of this project is to create a way of saving valuable information in images by using the technique called [Steganography](https://searchsecurity.techtarget.com/definition/steganography) which basically is **hiding secret data within an ordinary, non-secret, file or message in order to avoid detection; the secret data is then extracted at its destination.** 

## General Idea
With this script you can hide *text files* and *images* within other images and later send them to someone as a typical image. They can only see the hidden content if they know the a key (*pattern*) of how you save the secret info within the image. 
<img src="https://github.com/CarlosCujcuj/Image-Steganography/blob/master/imgs/flow.jpg" height="400" />


## Brief Introduction How it Works:
Every image si made of pixels, and every pixel is made of 3 colors: **RED, GREEN, BLUE** *(RGB)*.
<p align="center">
<img src="https://github.com/CarlosCujcuj/Image-Steganography/blob/master/imgs/pixels.jpg" height="250" /> <img src="https://github.com/CarlosCujcuj/Image-Steganography/blob/master/imgs/pixels2.jpg" height="250" />
</p>

This means that every image is composed of 3 channels (red, green blue).
If you separate each channel you end up with a black and white image where you have parts of images which are more white than others for every channel. 
**This represents the the amount of that color in that channel**. As you can see in the image below, in the red channel the Scarlet Macaw has his feathers more white than in other channels

<p align="center">
<img src="https://github.com/CarlosCujcuj/Image-Steganography/blob/master/imgs/channels.png" height="250" />
</p>

So this tell us that every channel has a range of value that describes how much of a color has that image. This range of values goes from 0 to 255, which **0** represents total **Black** and **255** total **White**

<p align="center">
<img src="https://github.com/CarlosCujcuj/Image-Steganography/blob/master/imgs/values.gif" height="250" />
</p>

So all of this information help us to achieve our goal to hide info inside an image, because we can represent characters like letters or other alphanumeric with numbers. Every alphanumeric character is represented by a number in the ASCII table

<p align="center">
<img src="https://github.com/CarlosCujcuj/Image-Steganography/blob/master/imgs/ascii.png" height="450" />
</p>
So we can use these values to save every characters within our images. 

To save images within other images there's a step before this. First we need to encode to image to **Base64**, which is a group of binary-to-text encoding schemes that represent binary data in an ASCII string.
letters or other alphanumeric with numbers. Every alphanumeric character is represented by a number in the ASCII table. Like we see in the image below

<p align="center">
<img src="https://github.com/CarlosCujcuj/Image-Steganography/blob/master/imgs/Screen%20Shot%202019-12-04%20at%201.26.31%20PM.png" height="250" />
</p>
