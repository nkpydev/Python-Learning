import time


if __name__ == '__main__':

    print('Press any Key to start!\tPress any Key to stop!')

    while True:
        try:
            input()
            start_time = time.time()
            print('Started!!')
            while True:
                print('Elapsed Time:\t',round(time.time()-start_time,0),'secs',end='\r')
                time.sleep(1)
        except KeyboardInterrupt:
            print('\nStopped!!')
            end_time = time.time()
            print('Total Time Elapsed:\t',round(end_time-start_time,0),'secs')
            break