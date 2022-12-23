import cv2
import os
BasePath="dataset/"
CropPath="dataset_crop/"
a=os.listdir(BasePath)
for i in a:
    path=BasePath+i+"/"
    savePath=CropPath+i+"/"
    b=os.listdir(CropPath)
    if i not in b:
        os.mkdir(savePath)
    imgs=os.listdir(path)
    ctr=0
    for j in imgs:
        imgPath=path+j
        img=cv2.imread(imgPath)
        nw=0
        nh=0
        h,w=img.shape[:2]
        for nw in range(0,w,1920):
            for nh in range(0,h,1080):
                c=img[nh:nh+1080,nw:nw+1920]
                #cv2.imshow("j",c)
                #cv2.waitKey(0)
                name=savePath+str(ctr)+".jpg"
                ctr+=1
                #print(name)
                cv2.imwrite(name,c)
