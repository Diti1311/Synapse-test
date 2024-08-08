customers = [[5,2], [5,4], [10,3], [20,1]]
finishing_time = 0
total_wait_time = 0

for arrival_time, required_time in customers:
    if finishing_time == 0:
        finishing_time = arrival_time + required_time
        waiting_time = finishing_time - arrival_time
        total_wait_time += waiting_time
        print(waiting_time)
    else:
        if arrival_time > finishing_time:
            finishing_time = arrival_time
        finishing_time = finishing_time + required_time
        waiting_time = finishing_time - arrival_time
        total_wait_time += waiting_time
        print(waiting_time)

average_time = total_wait_time / len(customers)
print("Average waiting time is:",average_time)