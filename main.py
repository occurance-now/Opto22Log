import codecs
import argparse
import pandas as pd
from columns import print_columns
from plot import get_graph_labels, plot_data

"""ArgParse module for detecting command line filepath selection"""
def parse_cmd_args():
    parser = argparse.ArgumentParser()#Create the parser
    parser.add_argument('-path', type=str, required=True, help="Filepath to historical log to be plotted. All log files should be place in historical_log folder.\
                                                                \nExample path: ./historical_logs/KT35/RD220726.H00 ")
    args = parser.parse_args()#Parse the arguement 
    
    '''
    Get File
    '''
    #file_path = './historical_logs/KT35/RD220726.H00'
    file_path = args.path
    data = pd.read_csv(codecs.open(file_path, 'rU', 'utf-16'))
    return data

"""User Input module for selecting which tag to be graphed"""
def user_input(tag_list):
    tag_list_length = len(tag_list)
    while True:
        raw_input = input(f'Please enter an integer value from the list above in the range of 0 -> {tag_list_length}: ')
        try:
            user_input = int(raw_input)
            if 0 <= user_input <= tag_list_length:
                break 
            print(f'Valid range = 0 -> {tag_list_length}')
        except ValueError:
            print(f"Only integer values in the range of 0 -> {tag_list_length} are accepted!")

    ypoints = data.columns[user_input + 2]
    return ypoints

if __name__ == "__main__":
    data = parse_cmd_args()
    tag_list = print_columns(data)
    ypoints = user_input(tag_list)
    label, unit = get_graph_labels(ypoints)
    plot_data(label, unit, data, ypoints)

