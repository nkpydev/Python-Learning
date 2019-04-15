import time

def wait_for_10mins():
    start_time = time.time()
    print('\nStarted!')
    end_time = start_time + 600 # 600 secs = 10 mins
    current_time = time.time()
    while current_time < end_time:
        current_time = time.time()
        print('Time Elapsed since start:\t',round(current_time-start_time,0),'secs',end='\r')
    print('\nStopped!!',end='\t')
    return True

if __name__ == '__main__':
    print('\nStarting the counter to 10 mins now!!')
    if wait_for_10mins() == True:
        print('10 mins have elapsed!')