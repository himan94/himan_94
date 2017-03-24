class marriage:

    def __init__(self):
        self.marr = {}  #men and their choice
        self.marr1 = {} #women and their choice

    def add_poss(self,name,pref):
        self.marr[name] = pref

    def add_poss1(self,name1,pref1):
        self.marr1[name1] = pref1

    def dis(self):
        return self.marr

    def dis1(self):
        return self.marr1

    def match(self):
        men = {}
        women = {}
        pr = {}
        selected = {}
        loop = 1
        while loop <= len(self.marr):
            # 1st for loop takes men's choices
            for i in self.marr.keys():
                for j,k in self.marr[i].items():
                    if j == loop and i not in selected.values():
                        women.setdefault(k, [])
                        women[k].append(i)
            # 2nd loop considers 1 woman chosen by 2 men
            for i1 in women.keys():
                for j1,k1 in self.marr1[i1].items():
                    if k1 in women[i1]:
                        pr.setdefault(i1,[])
                        pr[i1].append(j1)
            # 3rd loop solves the 2nd loop and at end the woman chooses 1 man
            for i2 in pr:
                a = min(pr[i2])
                selected[i2] = self.marr1[i2][a]
          
            loop = loop+1
        return selected
                    
m = marriage()
m.add_poss('ad',{1:'al',4:'b',3:'c',2:'d'})
m.add_poss('bo',{2:'al',3:'b',1:'c',4:'d'})
m.add_poss('ca',{1:'al',4:'b',3:'c',2:'d'})
m.add_poss('da',{3:'al',4:'b',1:'c',2:'d'})
m.add_poss1('al',{4:'ad',3:'bo',2:'ca',1:'da'})
m.add_poss1('b',{4:'ad',2:'bo',3:'ca',1:'da'})
m.add_poss1('c',{2:'ad',1:'bo',4:'ca',3:'da'})
m.add_poss1('d',{2:'ad',1:'bo',4:'ca',3:'da'})
print m.match()
