# AI_Dino_Game
The objective of this repor is to create a bot that will game the chrome dino game at chrome://dino.

 The first technique that I tried is using by taking a screenshot of the screen at a very quick pase. Compare the ROI ( Region of Intrest ) of the screenshot to a set of examples of images where the dino should jump. The decision of whether the dino should jump or not is made by subtracting the pixel values of the ROI of the screenshot and all the examples. If it is below a certian threshold ( i.e the ROI resembles the example ) then the dino will jump. 

 As you can see this is not the best method to figure out if the dino should jump or not. We cannot possible conver all the possible instanecs where the dino should jump in the examples. Since we cannot be finding the differences of a lot of ROI and examples. Another reason is that finding abosulte differences between the pixels of the ROI and examples is not the most accurate way to tell if the images resmble each other or not. 

 But hey if you do wanna try it, check out Simple_Dino.  

**How to use Simple Dino**

1. Open the Chrome web browser
2. Start the `main.py` in Simple_Dino
3. Switch to the Chrome window
4. The script will start working after 5 seconds to give you enough time to get ready. 

## Chrome Dino game using Machine Learning 

Now we come to the real reason you are here. There are several 
ways of playing the game. First let's figure out what kind of 
ML algorithm are we gonna use. There is Supervised or Reinforced. 
I am going to use Reinforced here  as it is the one I am mostly intrested. 

First we need an important input form the game which is the speed at which the obstacles are moving. 
We find the speed at which they are moving by taking 4 frames and finding how much the pixels have moved.
