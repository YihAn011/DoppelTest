import pickle


logbook_path = '/home/yihea/doppelTest/DoppelTest/data/log.bin'


with open(logbook_path, 'rb') as fp:
    logbook = pickle.load(fp)


print(logbook)