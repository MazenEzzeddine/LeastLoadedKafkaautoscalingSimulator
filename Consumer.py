from Partition import Partition


class  Consumer(object):
    def __init__(self, id = "", partitions=None, mu =0.0, lag=0.0):
        if partitions is None:
            partitions = []
        self.patitions = partitions
        self.mu = mu
        self.lag = lag
        self.id = id
    def __str__(self):
        str1 =   "consumer %s mu: %f  lag : %f"  % (self.id, self.mu, self.lag)
        str2 = ' '.join([' %s' % (self.patitions[n]) for n in range(len(self.patitions))])
        return str1 + " partitions " + str2

    def __eq__(self, other):
        return self.patitions == other.partitions and self.mu == other.mu

    def __lt__(self, other):
        return self.patitions < other.partitions

    def __gt__(self, other):
        return self.patitions > other.partitions

