import time

total_len = 1000000

x = list(range(total_len))
idx_insert = int(total_len / 2)
val_insert = 1000
y = list(range(len(x) + 1))


start_time = time.time()
for itr in range(0, idx_insert):    
	y[itr] = x[itr]

y[idx_insert] = val_insert

for itr in range(idx_insert, len(x)):    
	y[itr+1] = x[itr]

x = y

print(time.time() - start_time)



x = list(range(total_len))
idx_insert = int(total_len / 2)
val_insert = 1000
y = list(range(len(x) + 1))

idx_insert = int(total_len / 3)
start_time = time.time()
for itr in range(0, idx_insert):    
	y[itr] = x[itr]

y[idx_insert] = val_insert

for itr in range(idx_insert, len(x)):    
	y[itr+1] = x[itr]

x = y

print(time.time() - start_time)


x = list(range(total_len))
idx_insert = int(total_len / 2)
val_insert = 1000
y = list(range(len(x) + 1))

idx_insert = int(total_len / 4)
start_time = time.time()
for itr in range(0, idx_insert):    
	y[itr] = x[itr]

y[idx_insert] = val_insert

for itr in range(idx_insert, len(x)):    
	y[itr+1] = x[itr]

x = y

print(time.time() - start_time)