import sys, json, numpy as np, hashlib, time
def seed():
    return int(hashlib.sha256(str(time.time()).encode()).hexdigest(), 16) % 10**8
np.random.seed(seed())

to_encoding = json.load(open(sys.argv[1],"r"))
from_encoding = {}
for k,v in to_encoding.items():
    for i in v:
        from_encoding[i] = k

def encode(s):
    t = ""
    for i in s:
        if i.upper() in to_encoding:
            t += str(np.random.choice(to_encoding[i.upper()]))
            if i != s[-1]:
                t += " "
    return t

def decode(s):
    t = ""
    s = s.split(" ")
    g = []
    for i in s:
        if int(i) in from_encoding:
            t += from_encoding[int(i)]
    return t
    
def after_argv(ind):
    s = ""
    for i in range(ind,len(sys.argv)):
        s += sys.argv[i]
        if i < len(sys.argv)-1:
            s += " "
    return s

if __name__ == "__main__":
    if sys.argv[2] == "encode":
        print(encode(after_argv(3)))
    elif sys.argv[2] == "decode":
        print(decode(after_argv(3)))