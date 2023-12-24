import matplotlib.pyplot as plt

# Font sizes: https://stackoverflow.com/a/39566040/5940228

SMALL_SIZE = 10
MEDIUM_SIZE = 12
BIGGER_SIZE = 14


def load_iso_font():
    plt.rc('font', size=SMALL_SIZE)  # controls default text sizes
    plt.rc('axes', titlesize=BIGGER_SIZE)  # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
    plt.rc('font', **{'family': 'sans-serif', 'sans-serif': 'ISOCPEUR'})
