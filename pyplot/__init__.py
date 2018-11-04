import numpy as np
import matplotlib.pyplot as plt

def function_xdata(plot, xdata, function):
    plot.plot(xdata, function(xdata))

def function(plot, function, end, start=0, step=0.1):
    array = np.arange(start, end, step)
    function_xdata(plot, array, function)

def dataset(labels, dataset, category):
    cat = np.full(len(labels), None)
    for data in dataset:
        catid = category(data)
        if cat[catid] == None:
            cat[catid] = []
        
        cat[catid].append(data)
    return cat

def plot_ds(plot, sorted_ds, display, labels=None, colors=None):
    lines = np.full(len(sorted_ds), None)
    for i in range(len(sorted_ds)):
        points = sorted_ds[i]

        if points != None:
            for j in range(len(points)):
                x, y = points[j]
                if lines[i] == None:
                    lines[i] = plot.plot(x, y, display, color=colors[i])
                else:
                    line2d = lines[i][0]
                    xdata, ydata = line2d.get_data()
                    line2d.set_data(np.append(xdata, [x]), np.append(ydata, [y]))