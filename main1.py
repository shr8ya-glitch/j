import random
import time

def get(s,e):
    print("random date:")
    r=random.random()
    df='%m/%d/%y'
    st=time.mktime(time.strptime(s,df))
    et=time.mktime(time.strptime(e,df))
    print(r)
    print("random date=", (get("1/12016","2/2/2025")))