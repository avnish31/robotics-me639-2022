import numpy as np
import cv2_tools as cv2
import matplotlib.pyplot as plt
import os
def scaleAndshow (im, name + 'window' , height = None  , waitkey =1):
    def callback (event,x,y,flags , param):
        if event== cv2.EVENT_LBUTTONDOWN:
            print (x.y. im[y,x])

    cv2.namewindow(name)
    cv2.serMouseCallback(name,callback)
    if height is not None:
        width = int(im.shape[1]*height/im.shape[]0)
        im=cv2.resize(im,(width,height),interplatin=cv2.INTER_NEAREST)
    cv2.imshow(name,im)
    if cv2.waitkey(waitkey) == ord('q'):
        exit()

class Renderer()

def __init__(self,height = 600 , width = 600 , recordLocation =None):
    shape=(height,width,3)
    self.height = height
    self.width = width
    self.writer = None
    if recordlocaion is not None:
        self.writer= cv2.VideoWriter(recordLocation, cv2VideoWriter_fourcc(&'XVID'),25,(width,height))

        self.origImage= np.ones(shape,dype=np.uint8)*255

    def putText(self, image, info = {}):
        for i, (k, v) in enumerate(info.items()):
            cv2.putText(image, k + ' : ' + str(v), (10, 20 + i*20), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)
        return image
    
    def draw(self, image):
        raise NotImplementedError

    def getInfo(self):
        raise NotImplementedError

    def render(self, height = 600, pause = 10):
        image = self.origImage.copy()
        image = self.draw(image)

        image = self.putText(image, self.getInfo())

        if self.writer is not None:
            self.writer.write(image)
        scaleAndShow(image, height= height, waitKey = pause)
        return image

if __name__ == "__main__":

    
    def render(image):
        cv2.line(image, (0, 0), (100, 100), (0, 128, 0), 1)
        return image

    r = Renderer(600, 600, render)    

    for i in range(100):
        r.render(info = {'hello' : '00'})