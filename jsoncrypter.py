import sys, json, numpy as np, hashlib, time


class CypherResolver:
    def __init__(self, mappingsjson):
        self.mappings = json.load(open(mappingsjson,"r"))
        self.reverse = {}
        for k,v in self.mappings.items():
            for i in v:
                self.reverse[i] = k
    def encode(self, s):
        t = ""
        for i in s:
            if i.upper() in self.mappings:
                t += str(np.random.choice(self.mappings[i.upper()]))
                if i != s[-1]:
                    t += " "
        return t
    def decode(self, s):
        t = ""
        s = s.split(" ")
        g = []
        for i in s:
            if int(i) in self.reverse:
                t += self.reverse[int(i)]
        return t

def seed():
    return int(hashlib.sha256(str(time.time()).encode()).hexdigest(), 16) % 10**8
np.random.seed(seed())

def after_argv(ind):
    s = ""
    for i in range(ind,len(sys.argv)):
        s += sys.argv[i]
        if i < len(sys.argv)-1:
            s += " "
    return s

if __name__ == "__main__":
    c = CypherResolver(sys.argv[1])
    if sys.argv[2] == "encode":
        print(c.encode(after_argv(3)))
    elif sys.argv[2] == "decode":
        print(c.decode(after_argv(3)))