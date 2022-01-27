
import queue
pre_orders = []
last_order = None
cases = int(input())
available = queue.PriorityQueue(cases)
total_wait = 0

for _ in range(cases):
    pre_orders.append ([int(x) for x in input().split()])
    
pre_orders.sort(key=lambda x: x[0], reverse=True)

last_order = pre_orders.pop()
last_order.append(last_order[0] + last_order[1])
total_wait += last_order[2] - last_order[0]

time = last_order[2]
for _ in range(cases-1):
                        
    while(pre_orders and time >= pre_orders[-1][0]): 
        node = pre_orders.pop()
        available.put((node[1], node))
                        
    if available:
        deleted = available.get()[1]
        deleted.append(time + deleted[1])
        total_wait += deleted[2] - deleted[0]
        last_order = deleted
    else:
        temp = pre_orders.pop()
        temp.append(temp[0] + temp[1])
        total_wait += temp[2] - temp[0]
        last_order = temp

    time = last_order[2]

    
print(int(total_wait/cases))
