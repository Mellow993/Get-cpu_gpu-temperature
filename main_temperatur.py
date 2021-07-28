import sys
import os

try:
    import numpy as np
    import matplotlib.pyplot as plt
except:
    print("Modules could not be found.", file=sys.stderr)
    sys.exit(1)

class Temperatur:
    def __init__(self,name,time,T):
        self.name = name
        self.time = time
        self.T = T

    def get_name(self):
        return self.name

    def get_T_min(self):
        return min(self.T)

    def get_T_max(self):
        return max(self.T)

    def get_time_at_max_Temp(self):
        return self.time[max(self.T)] # Indexing in Klassen???

    def get_entire_time(self):
        return len(self.time)

def main():
    if len(sys.argv) != 2:
        print("Plot title is missing")
        sys.exit(2)

    else:
        pass
    titel = sys.argv[1]
    print("Starting")

    # Get the Values from textfile
    val_gpu = np.loadtxt('val_gpu')
    Core1 = np.loadtxt('Core1')
    Core2 = np.loadtxt('Core2')
    Core3 = np.loadtxt('Core3')
    Core4 = np.loadtxt('Core4')

    if len(Core1) == len(Core2) == len(Core3) == len(Core4) == len(val_gpu):
        print("ALL ARRAYS HAVE THE SAME LENGTH")
        len_gpu=len(val_gpu)
        t = np.arange(0,len_gpu)
    else:
        print("NOTIFICATION: ARRAY LENGTH IS NOT IDENTICAL")
        sys.exit(2)

    plt.style.use('seaborn')
    fig, ax = plt.subplots(nrows=5,ncols=1, sharex=True, sharey=True)

    ax[0].plot(t, Core1, label='Core1')
    ax[1].plot(t, Core2, label='Core2')
    ax[2].plot(t, Core3, label='Core3')
    ax[3].plot(t, Core4, label='Core4')
    ax[4].plot(t, val_gpu, label='GPU')
    ax[4].set_xlabel('Seconds [s]')
    ax[0].set_ylabel('[°C]')
    ax[1].set_ylabel('[°C]')
    ax[2].set_ylabel('[°C]')
    ax[3].set_ylabel('[°C]')
    ax[4].set_ylabel('[°C]')
    ax[0].legend(loc='upper left')
    ax[1].legend(loc='upper left')
    ax[2].legend(loc='upper left')
    ax[3].legend(loc='upper left')
    ax[4].legend(loc='upper left')
    plt.tight_layout()
    fig.savefig("Plots/GPU_Temp_" + titel + ".pdf")
    fig.show()

    #max_temp(Core1,Core2,Core3,Core4,val_gpu)

    C1 = Temperatur("Kern1", t, Core1)
    C2 = Temperatur("Kern2", t, Core2)
    C3 = Temperatur("Kern3", t, Core3)
    C4 = Temperatur("Kern4", t, Core4)
    G = Temperatur("GPU", t, val_gpu)

    # Printing the results
    print("The temperatures have been recorded for {} seconds".format(C1.get_entire_time()))
    MAX_T(C1,C2,C3,C4,G)
    print(30*"-")
    MIN_T(C1,C2,C3,C4,G)
    #print(C1.get_time()) Zeit bei maximaler Temperatur siehe Literatur

def MAX_T(C1,C2,C3,C4,G):
    for objekt in [C1, C2, C3, C4, G]:
        print("{:6s} has a max T of: {}  °C".format(objekt.get_name(), objekt.get_T_max()))

def MIN_T(C1,C2,C3,C4,G):
    for objekt in [C1, C2, C3, C4, G]:
        print("{:6s} has a min T of: {}  °C".format(objekt.get_name(), objekt.get_T_min()))
# Will not be executed. It has been substituted by classes
def temp_check(x): # check every value and give me a special notification
    if x <= 80:
        print("Mittlere Temperatur: ", x, " Grad Celsius")
    else:
        print("Warnung Temperatur zu hoch: ", x, " Grad Celsius")
def max_temp(c1,c2,c3,c4,gpu):
    print("CPU1 max: ", max(c1))
    print("CPU2 max: ", max(c2))
    print("CPU3 max: ", max(c3))
    print("CPU4 max: ", max(c4))
    print("GPU max: ", max(gpu))

    if max(c1)>=84 or max(c2)>=84 or max(c3)>=84 or max(c4 )>=84 or max(gpu)>=84 :
        print("The temperature reached over 84 degree")
        

# Starting Main Programm
if __name__ == "__main__":
    main()
