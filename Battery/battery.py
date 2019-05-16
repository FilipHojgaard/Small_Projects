import psutil
import matplotlib.pyplot as plt
import threading
import time
import msvcrt
import sys
import numpy as np

ESCAPE_KEY = chr(27).encode()
SPACE_KEY = chr(32).encode()



def fetch_battery_stat():
    print("NEW BATTERY THREAD\n")
    while(1):
        battery_now = psutil.sensors_battery().percent
        print(battery_now)
        data_file = open("battery_data.txt", "a")
        data_file.write(str(battery_now))
        data_file.write("\n")
        data_file.close()
        time.sleep(10)
        

def graph_battery():
    data = []
    data_file = open("battery_data.txt", "r")
    for line in data_file:
        data.append(int(line))
    data_file.close()
    number = np.arange(len(data))
    plt.plot(number, data)
    plt.show()
    # Create Graph
    
    


def main():
    battery_thread = threading.Thread(target=fetch_battery_stat, args=())
    battery_thread.setDaemon(True)  # Make the thread terminatable.
    battery_thread.start()
    while(1):
        key_press = msvcrt.getch()
        if(key_press == SPACE_KEY):
            print("SHOWING DATA...")
            graph_battery()
        if (key_press == ESCAPE_KEY):
            print("EXITTING...")
            sys.exit() 


if __name__ == "__main__":
    main()

