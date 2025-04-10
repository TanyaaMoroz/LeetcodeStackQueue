from collections import defaultdict, deque

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)   
        self.group = defaultdict(deque)   
        self.maxfreq = 0                  

    def push(self, val):
        self.freq[val] += 1
        f = self.freq[val]
        self.group[f].append(val) 
        if f > self.maxfreq:
            self.maxfreq = f

    def pop(self):
        val = self.group[self.maxfreq].pop()
        self.freq[val] -= 1

        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return val