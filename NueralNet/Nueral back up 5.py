import numpy as np
from PIL import Image
import sys


#geting the image
img_data = Image.open('1.png')

CorrectChoice=2

img_arr = np.array(img_data)
np.set_printoptions(threshold=sys.maxsize)
#print(img_arr)


new_a = np.delete(img_arr, [2])

print()

TotalSnew_a=(new_a.size)

x=0

new_a_b_w=[]

while x != TotalSnew_a:
    val=new_a[x]
    new_a_b_w.append(val)
    x=x+1
#print(new_a_b_w)

TotalSnew_a_b_w=(len(new_a_b_w))
#print(TotalSnew_a_b_w)
x=0
new_TotalCV_arr=[]

w=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
b=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]



SumVal_arr=(sum(new_a_b_w))/TotalSnew_a_b_w
#CondenseVAl=SumVal_arr/TotalSnew_a_b_w
#print(SumVal_arr)
#print(CondenseVAl)


CalVAl_arr=[]

#print(TotalSnew_a_b_w)
while x != TotalSnew_a_b_w:
    print(x)
    CalVAl=(SumVal_arr*w[x])+b[x]
    #CondCalVAl=CalVAl/TotalSnew_a_b_w
    CalVAl_arr.append(CalVAl)
    #print(SumCalVAl)
    x=x+1


NumChoices=2
x=0
# 5 , 2
w2=[1, 3]
b2=[1, 3]
CalVAl_arr2=[]

SumCalVAl=(sum(CalVAl_arr))/TotalSnew_a_b_w
#print(SumCalVAl)

#print((SumCalVAl*w2[x])+b2[x])

CorrectFull=0

while CorrectFull != True:
    x=0
    CalVAl_arr2=[]
    #print(w2,b2)
    while x != NumChoices:
        CalVAl2=(SumCalVAl*w2[x])+b2[x]
        #print(CalVAl2)
        CondCalVAl2=CalVAl2/TotalSnew_a_b_w
        CalVAl_arr2.append(CondCalVAl2)
        #print(CondCalVAl2)
        x=x+1

    print(CalVAl_arr2)
    TotalVal2=CalVAl_arr2[0]+CalVAl_arr2[1]
    #print(TotalVal2)

    if CalVAl_arr2 [0] > CalVAl_arr2 [1]:
        #print("5")
        if CorrectChoice == 5:
            CorrectFull=True
            print("correct Its 5")
    
        else:
            Cost=(CalVAl_arr2[0]/TotalVal2)
            counterw=w2[0]
            w2[0]=counterw-Cost

            counterb=b2[0]
            b2[0]=counterb-Cost


            counterwadd=w2[0]
            w2[0]=counterwadd+Cost

            counterbadd=b2[0]
            b2[0]=counterbadd+Cost



            
            #print(Cost)
            #print(w2,b2)     


    elif CalVAl_arr2 [1] > CalVAl_arr2 [0]:
        #print("2")
        if CorrectChoice == 2:
            CorrectFull=True
            print("correct Its 2")

        else:
            Cost2=(CalVAl_arr2[1]/TotalVal2)
            #print(Cost2)
            counterw2=w2[1]
            w2[1]=counterw2-Cost2

            counterb2=b2[1]
            b2[1]=counterb2-Cost2



            counterw2add=w2[0]
            w2[0]=counterw2add+Cost2

            counterb2add=b2[0]
            b2[0]=counterb2add+Cost2



            #print(w2,b2)  
            #print(w2,b2)  

        





























