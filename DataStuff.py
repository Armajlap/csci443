import matplotlib.pyplot as plt
import numpy as np

#Clicks
def clicks():
    labels = ['User 1', 'User 2', 'User 3', 'User 4', 'User 5']
    task1 = [5, 2, 2, 2, 7]
    task2 = [5, 3, 3, 3, 3]
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, task1, width, label='Task 1')
    rects2 = ax.bar(x + width/2, task2, width, label='Task 2')
    ax.set_ylabel('Clicks')
    ax.set_title('Clicks for each user and task')
    ax.set_xticks(x, labels)
    ax.legend()
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    fig.tight_layout()

    average1 = np.mean(task1)
    average2 = np.mean(task2)
    print("Average clicks for task 1: "+str(average1)+" for task 2: "+str(average2))
    std1 = np.std(task1)
    std2 = np.std(task2)
    print("Standard deviation for clicks for task 1: " + str(std1) + " for task 2: " + str(std2))

    plt.show()

def errors():
    labels = ['User 1', 'User 2', 'User 3', 'User 4', 'User 5']
    task1 = [1, 0, 0, 0, 3]
    task2 = [2, 0, 0, 0, 0]
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, task1, width, label='Task 1')
    rects2 = ax.bar(x + width / 2, task2, width, label='Task 2')
    ax.set_ylabel('Errors')
    ax.set_title('Errors for each user and task')
    ax.set_xticks(x, labels)
    ax.legend()
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    fig.tight_layout()

    average1 = np.mean(task1)
    average2 = np.mean(task2)
    print("Average errors for task 1: " + str(average1) + " for task 2: " + str(average2))
    std1 = np.std(task1)
    std2 = np.std(task2)
    print("Standard deviation for errors for task 1: " + str(std1) + " for task 2: " + str(std2))

    plt.show()

def times():
    labels = ['User 1', 'User 2', 'User 3', 'User 4', 'User 5']
    task1 = [20, 18, 5, 10, 69]
    task2 = [42, 16, 5, 10, 5]
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, task1, width, label='Task 1')
    rects2 = ax.bar(x + width / 2, task2, width, label='Task 2')
    ax.set_ylabel('Time (s)')
    ax.set_title('Time taken for each user and task')
    ax.set_xticks(x, labels)
    ax.legend()
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    fig.tight_layout()

    average1 = np.mean(task1)
    average2 = np.mean(task2)
    print("Average time for task 1: " + str(average1) + " for task 2: " + str(average2))
    std1 = np.std(task1)
    std2 = np.std(task2)
    print("Standard deviation of time for task 1: " + str(std1) + " for task 2: " + str(std2))

    plt.show()

def qual():
    labels = ['User 1', 'User 2', 'User 3', 'User 4', 'User 5']
    task1 = [4, 4, 5, 5, 5]
    task2 = [5, 4, 4, 4, 4]
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, task1, width, label='How easy is the app to use')
    rects2 = ax.bar(x + width / 2, task2, width, label='Overall satisfaction with the app')
    ax.set_ylabel('Rating (1-5)')
    ax.set_title('User ratings')
    ax.set_xticks(x, labels)
    ax.legend()
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    fig.tight_layout()

    average1 = np.mean(task1)
    average2 = np.mean(task2)
    print("Average score task 1: " + str(average1) + " for task 2: " + str(average2))
    std1 = np.std(task1)
    std2 = np.std(task2)
    print("Standard deviation of score for task 1: " + str(std1) + " for task 2: " + str(std2))

    plt.show()


clicks()
errors()
times()
qual()
