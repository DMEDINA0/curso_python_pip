import matplotlib.pyplot as plt
import os

def generate_pie_chart():
    labels = ["A","B","C"]
    values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    plt.savefig("modelo.png")
    plt.close()

generate_pie_chart()    

print(os.getcwd())