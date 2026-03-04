import multiprocessing
def square(n):
    return n**2

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool : 
        out = pool.map(square , [1,2,3,4,5,6,7,8,9])
        print(out)





def producer(q) :
    for i in ["pagal","suru","moti","jugnu"]:
        q.put(i)
    
def consume(q) :
    while True : 
        item = q.get()
        if item is None :
            break
        print(item)

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    m1 = multiprocessing.Process(target=producer , args= (queue,))
    m2 = multiprocessing.Process(target=consume , args = (queue,))
    m1.start()
    m2.start()
    queue.put("suru")
    m1.join()
    m2.join()



