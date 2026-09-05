import json
import os
import datetime

def sum(a:int,b:int)->int:  #return funct
    return a+b

def main():  #void funct
    result = sum(25,10)
    print(result)

if __name__=="__main__":
    main()

print(datetime.datetime.now())