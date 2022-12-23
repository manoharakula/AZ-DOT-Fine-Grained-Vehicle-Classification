import os
import random
import shutil

trainPath="dataset/train/"
valPath="dataset/val/"

tDir=os.listdir(trainPath)
for i in tDir:
    vDir=os.listdir(valPath)
    imgPath=trainPath+i+"/"
    savePath=valPath+i+"/"
    if i not in vDir:
        os.makedirs(savePath)    
    tImgs=os.listdir(imgPath)
    n=int(len(tImgs)*0.1)
    vImgs=random.sample(tImgs,n)
    for j in vImgs:
        shutil.move(imgPath+j,savePath+j)

