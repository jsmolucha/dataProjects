from subprocess import _ENV
import requests
import json
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import time

response = requests.get(_ENV.API_STRING)
res_data = response.json()

totalgross = []
dayonlot = []
year = []


def printSum(obj):
    start = time.time()
    raw_data = obj.json()
    #filter out the NULL fields in the data
    #fucking data isnt filtered and its a shitshow with broken references 
    #goddamnit
    sum = 0
    for i in range(len(raw_data['data'])):
        #Ok actually skipping all deals that have NULL
        #fucking up my dataset
        val = raw_data['data'][i]['TOTALGROSS']

        #iF it actually returns a goddamn value 
        if val != None:
            flo_val = float(val)
            sum += flo_val
            totalgross.append(val)

        else:
            totalgross.append(0)
            continue

    end = time.time()
    print("TOTAL GROSS SUM: ")
    print('%.2f' % sum)
    print("exec time: ", '%.2f' % float(end-start))

def getYear(obj):
    raw_data = obj.json()

    for i in range(len(raw_data['data'])):
        val = raw_data['data'][i]['YR']

        if val != None:
            flo_val = float(val)
            year.append(val)
        else:
            dayonlot.append(0)
            continue

def dayAvg(obj):
    start = time.time()
    raw_data = obj.json()
    total = 0
    mDays = 0

    for i in range(len(raw_data['data'])):
        val = raw_data['data'][i]['DAYS']

        if val > mDays:
            mDays = val

        if val != None:
            flo_val = float(val)
            total += flo_val
            dayonlot.append(val)
        else:
            dayonlot.append(0)
            continue
    
    print("average days on lot: ", '%.2f' % float(total / len(raw_data['data'])), "days")
    end = time.time()
    print("exec time: ", '%.2f' % float(end-start))
    print("longest time on lot: ", mDays)

printSum(response)
dayAvg(response)

x = np.array(totalgross)
y = np.array(dayonlot)

plt.plot(x, y)
plt.show()

