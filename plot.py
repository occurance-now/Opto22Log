import datetime
import regex as re
import matplotlib.pyplot as plt

'''Show Graph/Print Min/Max/Range'''
def get_graph_labels(ypoints):
    if re.findall(".*_TT_.*", ypoints):
        label = 'Temperature'
        unit = 'Deg C'
    elif re.findall(".*_PT_.*", ypoints):
        label = 'Pressure'
        unit = 'PSI'
    elif re.findall(".*_VB_.*", ypoints):
        label = 'Vibration'
        unit = 'IPS'
    elif re.findall(".*_LD_.*", ypoints):
        label = 'Load'
        unit = 'Amps'
    elif re.findall(".*_Confirm", ypoints):
        label = 'On/Off Status'
        unit = 'Boolean'
    else: 
        print("Tag no recognized")

    return label, unit

'''Graph data'''
def plot_data(label, unit, data, ypoints):
    fig, ax = plt.subplots(1, 1)
    plt.ylabel(unit)

    data.plot(x='Time', y=ypoints,  color = 'g', linestyle = 'solid', 
            label = label, figsize=(12,6), title=ypoints, ax=ax)

    y_data = data[ypoints]
    annot_max(data, y_data, ypoints)
    annot_min(data, y_data, ypoints)
    file_date = datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S')
    plt.savefig(f'./graph_archives/{file_date}{ypoints}.png')
    plt.show()

'''Time converter for graph label'''
def time_convert(time):
    xmax_time = datetime.datetime.strptime(time,'%H:%M').strftime('%I:%M %p')
    return xmax_time
'''Max/Min annotation functions'''
def annot_max(data, y_data, ypoints, ax=None):
    ymax = max(y_data)
    xmax = data.index[data[ypoints] == ymax].tolist()[0]
    xmax_str = data['Time'][xmax][0:5]
    xmax_time = time_convert(xmax_str)
    text= f"Max Value: x={xmax_time}, y={ymax:.3f}"

    if not ax:
        ax=plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.26)
    arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60")
    kwargs = dict(xycoords='data',textcoords="axes fraction", arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top", size = 8)
    ax.annotate(text, xy=(xmax, ymax), xytext=(.99, .9), **kwargs)

def annot_min(data, y_data, ypoints, ax=None):
    ymin = min(y_data)
    xmin = data.index[data[ypoints] == ymin].tolist()[0]
    xmin_str = data['Time'][xmin][0:5]
    xmin_time = time_convert(xmin_str)
    text= f"Min Value: x={xmin_time}, y={ymin:.3f}"

    if not ax:
        ax=plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.26)
    arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60")
    kwargs = dict(xycoords='data',textcoords="axes fraction", arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top", size = 8)
    ax.annotate(text, xy=(xmin, ymin), xytext=(.99, .85), **kwargs)

