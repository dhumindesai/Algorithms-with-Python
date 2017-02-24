from Queue import Queue

def hotPotatoSim(name_list, num):

    sim_q = Queue()

    for name in name_list:
        sim_q.enqueue(name)
    
    while sim_q.size() > 1:

        for i in range(num):
            sim_q.enqueue(sim_q.dequeue())

        sim_q.dequeue()
    
    return sim_q.dequeue()



print hotPotatoSim(["Bill", "David", "Susan", "Jane", "Kent","Brad"], 7)

