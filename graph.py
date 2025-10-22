import matplotlib.pyplot as plt
import numpy as np
import datetime
from utils.logs import logging


def hourlyData(last_four_weeks_data,today_data,type,filename,filepath):
# def hourlyData(today_data):

# Sample data (replace with your actual data)
    # last_four_weeks = [
    #     [42, 18, 10, 9, 11, 14, 65, 134, 129, 148, 139, 121, 93, 98, 88, 89, 68, 90, 62, 79, 78, 75, 71, 57],
    #     [44, 24, 9, 14, 8, 20, 69, 127, 126, 141, 139, 118, 89, 83, 103, 69, 75, 71, 91, 95, 72, 84, 69, 45],
    #     [63, 7, 8, 9, 10, 23, 54, 133, 135, 142, 123, 102, 96, 73, 91, 95, 66, 70, 73, 68, 93, 77, 61, 48],
    #     [50, 20, 9, 9, 13, 28, 75, 125, 133, 139, 132, 114, 86, 81, 78, 76, 96, 68, 74, 72, 95, 86, 85, 39]
    # ]

    # today_data = [19, 6, 3, 3, 4, 3, 13, 37, 27, 38, 30, 34, 41, 24, 19, 25, 20, 22, 15]

    # Calculate average order rate for each hour
    average_rates = np.mean(last_four_weeks_data, axis=0)
    Date = datetime.datetime.now().hour+1
    # Date = datetime.datetime.now().m

    # Date = 5
    # Create a graph
    this_hour = np.sum(today_data[:Date-1])
    print (this_hour)
    Average_hour = np.sum(average_rates[:Date-1])
    hours = list(range(1, 25))
    hourss = list(range(1, int(Date)+1))


    plt.figure(figsize=(12, 6))
    for hour, value in zip(hours, average_rates):
        plt.text(hour, value, f'{int(value)}', ha='center', va='bottom')

    for hour, value in zip(hourss, today_data[:Date]):
        plt.text(hour, value, f'{value}', ha='center', va='bottom')

    todayDate = datetime.datetime.now().strftime("%d-%m-%Y ")
    todayTIme = datetime.datetime.now().strftime(" %H:%M:%S ")
    if  type =="DPS last 4 days":
        plt.plot(hours, average_rates, label=f"Average (Last 4 days Average )")
    else:
        plt.plot(hours, average_rates, label=f"Average (Last 4 weeks )")
    plt.plot(hourss, today_data[:int(Date)], label='Today')

    # Customize the graph

    plt.xlabel('Hour')
    plt.ylabel('Order Rate')
    # plt.title(f"{type}({todayDate}) average till {Date}:00:00 BST  orders {this_hour}/{Average_hour}")
    plt.title(f"{type}({todayDate}) average till {Date}:00:00 BST  ")

    plt.xticks(hours)
    plt.legend()
    plt.grid(True)


    plt.savefig(f"{filepath}")
    logging.info(f"{filename } graph created")
