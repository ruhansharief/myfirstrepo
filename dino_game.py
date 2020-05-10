#packages needs to be installed - PIL, numpy, pyautogui
#The below code works only in MacOs and Windows OS


from PIL import ImageGrab, ImageOps 
import pyautogui 
import time 
import numpy as np 
	
class AutomatedDino(): 

    def __init__(self):
        self.replay_button = (360, 214)
        self.dino = (149, 239 )
	
    def restartGame(self): 
        """
        Method to click on replay button
        """
        pyautogui.click(self.replay_button) 

        #Dino should always be down to avoid hitting by bird 
        pyautogui.keyDown('down') 

    def press_space(self): 

        #Releasing the down key 
        pyautogui.keyUp('down') 

        # pressing Space to overcome Bush 
        pyautogui.keyDown('space') 

        #Time gap 
        time.sleep(0.05) 

        #Time gap for the bush to be passed
        time.sleep(0.10) 

        #Releasing the Space Key 
        pyautogui.keyUp('space') 

        #Again pressing the Down Key to keep the dino always down 
        pyautogui.keyDown('down') 

    def imageGrab(self): 
        #coordinates of box in front of dinosaur 
        box = (self.dino[0]+30, self.dino[1], 
            self.dino[0]+120, self.dino[1]+2) 

        # grabbing all the pixels values in form of RGB tupples 
        image = ImageGrab.grab(box) 

        # converting RGB to Grayscale to 
        # make processing easy and result faster 
        grayImage = ImageOps.grayscale(image) 

        # using numpy to get sum of all grayscale pixels 
        a = np.array(grayImage.getcolors()) 

        # returning the sum 
         
        return a.sum() 
        
        
obj = AutomatedDino()
obj.restartGame()
while True: 
    # 435 is the sum of white pixels values of box. 
    # You may get different value is you are taking bigger 
    # or smaller box than the box taken in this article. 
    # if value returned by "imageGrab" function is not equal to 435, 
    # it means either bird or bush is coming towards dinosaur 
    if(obj.imageGrab()!= 435): 
        obj.press_space() 
        # time to recognize the operation performed by above function 
        time.sleep(0.1) 
