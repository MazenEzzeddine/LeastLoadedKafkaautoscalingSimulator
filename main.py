import math



import matplotlib.pyplot as plt

from Consumer import Consumer
from Partition import Partition

time = []
point = []
lamdasla = 85
replicas = []
replicasscaled = []

partitions = []
wrkld = []
replicasbin = []


# Press the green button in the gutter to run the script.
def readWorkload():
    with open('defaultArrivalRatesm.csv', 'r') as f:
        lines = f.readlines()

    for line in lines:
        sample = line.split(',')[1][0:-1]
        wrkld.append(math.ceil(float(sample)))

    return  wrkld


def plotWorkload():
    for i in range(len(wrkld)):
        time.append((i+1))
        point.append(wrkld[i])
    plt.plot(time, wrkld)
    plt.show()



def plotWorkloadWithReplicas():
    for r in range(len(replicas)):
        replicasscaled.append(replicas[r]*175)

    plt.plot(time, wrkld)
    plt.plot(time, replicasscaled)
    plt.show()



def plotWorkloadWithReplicasBinPack():
    replicasscaled = []
    for r in range(len(replicasbin)):
        replicasscaled.append(replicasbin[r]*175)

    plt.plot(time, wrkld)
    plt.plot(time, replicasscaled)
    plt.show()


def computeReplicasLinear():
    for t in range(600):
        replicas.append(math.ceil(point[t]/lamdasla))
    print(replicas)




def computeReplicasLinearBinPack():
    for t in range(600):
        part = point[t]/5.0
        items = []
        for i in  range(5):
            items.append(part)
        bins = LeastLoaded(items)

        replicasbin.append(bins)
    print(replicasbin)

def simulate():
    for p in range(5):
        par = Partition(str(p),0, 0)
        partitions.append(par)

    c = Consumer(0,partitions, 175,0)
    print(c.patitions[0])
    items= []

    for p in partitions:
        p.lamda= 150
        items.append(p.lamda)
    LeastLoaded(items)



##########################################################

def LeastLoaded(items):
     for i in range(len(items)):
         print(items[i])

     items.sort(reverse=True)
     bincount=1

     while True:
        bins = []
        for i in range(bincount):
            bin = 85
            bins.append(bin)

        for j in range(len(items)):
            bins.sort(reverse=True)
            for id in range(bincount):
                if items[j] < bins[id]:
                    bins[id] = bins[id]- items[j]
                    break
            else:
                bincount += 1
                break
        else:
            break
     print(bincount)
     return bincount











##############################################################


if __name__ == '__main__':
     wrkld = readWorkload()
     #print(wrkld)
     plotWorkload()
     computeReplicasLinear()
     plotWorkloadWithReplicas()
     computeReplicasLinearBinPack()
     plotWorkloadWithReplicasBinPack()

     #simulate()


     #LeastLoaded()

