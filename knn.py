import csv
import random
with open(r"/Users/yuhangyang/Downloads/Prostate_Cancer.csv") as file:
        reader=csv.DictReader(file)
        datas=[row for row in reader]
random.shuffle(datas)

n=len(datas)//3
test_set=datas[0:n]
train_set=datas[n:]

def distance(d1,d2):
        res=0
        for key in ('radius','texture','perimeter','area','smoothness','compactness','symmetry','fractal_dimension'):
                res+=(float(d1[key])-float(d2[key]))**2
        return res**0.5

k=6

def knn(data):
        res=[{'result':train['diagnosis_result'],'distance':distance(data,train)} for train in train_set]
        sorted(res,key=lambda item:item['distance'])
        res2=res[0:k]
        result={'B':0,'M':0}

        sum_dist=0
        for r1 in res2:
                sum_dist+=r1['distance']

        for r2 in res2:
                result[r2['result']]+=1-r2['distance']/sum_dist
        print(result)

        if result['B']>result['M']:
                return'B'
        else:
                return'M'

correct=0
for test in test_set:
        result=test['diagnosis_result']
        result2=knn(test)

        if result == result2:
                correct = correct + 1;

print(str(correct/len(test_set)))


    
