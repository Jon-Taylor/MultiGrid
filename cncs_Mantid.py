import numpy as np

def histEventList(evlist):
    bins = np.histogram(evlist[:, 1]*0.0625, 500)
    binnedData=np.zeros([500,8*16*48])
    for i in range(8*16*48):
        ind = evlist[:, 0] == i
        tmp=evlist[ind,1]
        print('Number of counts in channel ' ,i,' ', len(tmp))
        binnedEvents = np.histogram(tmp, bins[1])
        binnedData[:,i]=binnedEvents[0]

    return bins, binnedData

evlst=np.load('/Users/jonathantaylor/PycharmProjects/untitled4/Eventlist.dat.npy')

bins,binneddata=histEventList(evlst)

test=CreateWorkspace(bins[1],binneddata,NSpec=8*16*48)
