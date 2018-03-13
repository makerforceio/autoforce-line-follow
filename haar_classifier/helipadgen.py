from PIL import Image, ImageDraw
import random
import cv2
import numpy as np
thickvary=10
sizevary=50
xmax=1024
ymax=1024
blackvary=0.20
for i in range(10):
    im=Image.new('RGB',(xmax,ymax),(255,255,255))
    d=ImageDraw.Draw(im)
    cw=25+(1 if random.randint(0,1) else -1)*random.randint(0,thickvary)
    hHeight=300+(1 if random.randint(0,1)%2 else -1)*random.randint(0,sizevary)
    hWidth=300+(1 if random.randint(0,1)%2 else -1)*random.randint(0,sizevary)
    vert1width=25+(1 if random.randint(0,1)%2 else -1)*random.randint(0,thickvary)
    vert2width=25+(1 if random.randint(0,1)%2 else -1)*random.randint(0,thickvary)
    horzwidth=25+(1 if random.randint(0,1)%2 else -1)*random.randint(0,thickvary)
    rgb=(int(255*random.uniform(0,blackvary)),int(255*random.uniform(0,blackvary)),int(255*random.uniform(0,blackvary)))
    d.ellipse([0,0,xmax,ymax],rgb,None)
    d.ellipse([cw,cw,xmax-cw,ymax-cw],(255,255,255),None);
    d.line([(xmax-hWidth)/2,ymax-(ymax-hHeight)/2,(xmax-hWidth)/2,(ymax-hHeight)/2],rgb,vert1width)
    d.line([xmax-(xmax-hWidth)/2,ymax-(ymax-hHeight)/2,xmax-(xmax-hWidth)/2,(ymax-hHeight)/2],rgb,vert2width)
    d.line([(xmax-hWidth)/2,ymax/2,xmax-(xmax-hWidth)/2,(ymax)/2],rgb,horzwidth)
    cvim=cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
    row,col,ch= cvim.shape
    mean = 0
    sigma = 20.0
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    
    noisy = cvim + gauss
    cv2.imwrite(str(i)+".png",noisy)
    #noisy = (noisy) * 255 / (np.amax(noisy) - np.amin(noisy))
    #noisy = np.clip(noisy + np.amin(noisy),0,255)
    
    #im.save(str(i)+".png")

