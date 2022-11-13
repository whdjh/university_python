import time

a = Queue()
b = new_Queue()

start_time = time.time()
a.enqueue(10)
end_time = time.time()

start_time1 = time.time()
b.enqueue(10)
end_time1 = time.time()

start_time2 = time.time()
a.dequeue()
end_time2 = time.time()

start_time3 = time.time()
b.dequeue()
end_time3 = time.time()

print(f"기존큐의삽입시간: {end_time - start_time}")

print(f"새로만든큐의삽입시간: {end_time1 - start_time1}")

print(f"기존큐의삭제시간: {end_time2 - start_time2}")

print(f"새로만든큐의삭제시간: {end_time3 - start_time3}")