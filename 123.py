#cau 1
def lapphuong(s):
    v = s**3
    return v
def hopchunhat(l,w,h):
    v= l*w*h
    return v
import math
def trutron(r,h):
    v= math.pi * r*r * h
    return v
def cau(r):
    v = 4/3 *math.pi*(r**3)
    return v
#hàm main
print(lapphuong(3))
print(hopchunhat(3,3,3))
print(trutron(3,3))
print(cau(3))
#cau 2
def classification_model (tp,fp,fn):
    if(not (isinstance(tp, int))): print(tp, " must be int")
    elif(not (isinstance(fp, int))): print(fp, " must be int")
    elif(not (isinstance(fn, int))): print(fn, " must be int")
    elif((tp<=0) or (fp<=0) or (fn<=0)): print ("tp and fp and fn must be greater than zero") 
    else:
        precision = tp/(tp+fp)
        print(precision)
        recall = tp/(tp+fn)
        print(recall)
        f1_score=2*(precision*recall)/(precision+recall)
        print(f1_score)
#hàm main
classification_model(2,3,3)
#cau 3
x= input()
activation_function=input()
def binary_step(x):
    if x<0: x=0
    else: x=1
    return x
def sigmoid(x):
    x= 1/(1+math.e**(-x))
    return x
def elu(x):
    if x<0: x=0.01*(e**x-1)
    return x
if(not x.isdigit()): print("x must be a number")
elif(activation_function == "binary"): print("binary: f(",x,")=",binary_step(float(x)))
elif(activation_function =="sigmoid"): print("sigmoid: f(",x,")=",sigmoid(float(x)))
elif(activation_function == "elu"): print("elu: f(",x,")=",elu(float(x)))
else: print("ten_function_user is not supported")
    
