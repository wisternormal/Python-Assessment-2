import random
import matplotlib.pyplot as plt
import csv
import agent

# get the environment from flie
f = open('in.txt', newline='') 
environment = []
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:				# A list of rows
    rowlist = []
    for value in row:				# A list of value
    	rowlist.append(int(value))
    environment.append(rowlist)
f.close()

# Draws the density of drunks passing through each point on a map
trace = environment

plt.xlim(0, 300)
plt.ylim(0, 300)
# # cmap: clour map
plt.figure("Planing for Drunks")
plt.subplot(1,2,1)
plt.title('the trace of drunks')
plt.imshow(environment, cmap = plt.cm.hot, vmin = 0.5 , vmax = 1.5)

for num in range(1,26):
	step_num = 100
	num_iter = 0
	while 1:
		i = 1
		flag = 0
		agents = []
		trace_x = []
		trace_y = []
		agents.append(agent.Agent())
		trace_x.append(agents[0].x)
		trace_y.append(agents[0].y)
		# plt.scatter(agents[0].x,agents[0].y)
		while i < (step_num + num_iter/100):
			agents.append(agent.Agent())
			agents[i-1].move()
			agents[i].x = agents[i-1].x
			agents[i].y = agents[i-1].y
			trace_x.append(agents[i].x)
			trace_y.append(agents[i].y)
			if environment[agents[i].y][agents[i].x] == (num*10):
				flag = 1
				break
			i = i +1
		if flag == 1:
			print("drunk ",num,"Sucess","num_iter:",num_iter,"step number:",i)
			plt.plot(trace_x,trace_y)
			for j in range(len(trace_x)):
				trace[trace_y[j]][trace_x[j]] = trace[trace_y[j]][trace_x[j]] + 1
			break
		num_iter = num_iter + 1

import csv
with open('out.txt', 'w') as f:	
    writer = csv.writer(f)
    writer.writerow(trace)
f.close()

# cmap: clour map
plt.subplot(1,2,2)
plt.title('the density of trace')
plt.imshow(trace,cmap = plt.cm.hot, vmin = 0.5 , vmax = 1.5)
plt.show()

