import time 

def timer_func():
    timer = int(input("Please set a timer"))
    while timer:
        print(timer)
        timer -= 1
        time.sleep(1)
    print("Your timer is up!")
    
timer_func()






