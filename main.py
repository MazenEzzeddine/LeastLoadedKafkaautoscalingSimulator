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
latencies = []
currentBins = 1


# Press the green button in the gutter to run the script.
def readWorkload():
    with open('2h.csv', 'r') as f:
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
    for t in range(7207):
        replicas.append(math.ceil(point[t]/lamdasla))
    print(replicas)




def computeReplicasLinearBinPack():
    for t in range(7207):
        part = point[t]/5.0
        items = []
        for i in  range(5):
            items.append(part)
        bins = scaledLeastLoaded(items, 1)

        ###########################################


        replicasbin.append(bins)

        ##########################################
        #bins = scaledLeastLoaded(items, 1.0)
        #computeLatencies(point[t], bins)
        #replicasbin.append(bins)

    # print scaling actions:
    scalingActions = 0
    for t in range(7206):
        if replicasbin[t] != replicasbin[t+1]:
            scalingActions += 1
    print("Scaling Actions is: " + str(scalingActions))



def computeReplicasLinearBinPackFraction():
    #600
    currentBins = 1
    for t in range(7207):
        part = point[t]/5.0
        items = []
        for i in  range(5):
            items.append(part)
        #bins = LeastLoaded(items)

        ###########################################

        bins = scaledLeastLoaded(items, 1.0)
        if bins > currentBins:
            replicasbin.append(bins)
            currentBins = bins
        elif bins < currentBins:
            bins = scaledLeastLoaded(items, 0.7)
            if bins < currentBins:
              replicasbin.append(bins)
              currentBins = bins
            else:
                replicasbin.append(currentBins)
        else:
            replicasbin.append(currentBins)

        ##########################################
        #bins = scaledLeastLoaded(items, 1.0)
        #computeLatencies(point[t], bins)
        #replicasbin.append(bins)

    # print scaling actions:
    scalingActions = 0
    for t in range(7206):
        if replicasbin[t] != replicasbin[t+1]:
            scalingActions += 1
    print("Scaling Actions is: " + str(scalingActions))

    # print(replicasbin)
    # print(latencies)





##########################################################


def scaledLeastLoaded(items, f):
    for i in range(len(items)):
        print(items[i])

    items.sort(reverse=True)
    bincount = 1

    while True:
        bins = []
        for i in range(bincount):
            bin = 85*f
            bins.append(bin)

        for j in range(len(items)):
            bins.sort(reverse=True)
            for id in range(bincount):
                if items[j] < bins[id]:
                    bins[id] = bins[id] - items[j]
                    break
            else:
                bincount += 1
                break
        else:
            break
    print(bincount)
    return bincount



#########################################################





def computeLatencies(Events, bins):
    for e in range(Events):
        latencies.append(5*(e)/bins)


def computeReplicaMinutes():
    replicasecond = 0.0
    for r in range(len(replicasbin)):
         replicasecond += replicasbin[r]

    print(replicasecond)
    print(replicasecond/60.0)












##############################################################


if __name__ == '__main__':
     wrkld = readWorkload()
     plotWorkload()
     computeReplicasLinear()
     plotWorkloadWithReplicas()
     computeReplicasLinearBinPack()
     plotWorkloadWithReplicasBinPack()
     computeReplicaMinutes()


