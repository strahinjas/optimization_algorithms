import matplotlib.pyplot as plt


def plotFromFile(fileName, xLabel, yLabel, plotCount):
    file = open(fileName, 'r')

    x = []
    y = []

    for i in range(plotCount):
        y.append([])

    for line in file:
        s = line.split()

        if len(s) == plotCount + 1:
            x.append(float(s[0]))

            for i in range(1, plotCount + 1):
                y[i - 1].append(float(s[i]) / (1024 ** 2))

    file.close()

    plt.figure()

    for i in range(plotCount):
        plt.plot(x, y[i])
        plt.yscale('log')

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.show()


plotFromFile('C:\\Users\\User\\Desktop\\Strahinja\\OOA\\Domaći\\7\\cumulative_minimum.txt',
             'Iteration', 'Cumulative minimum of cost-function', 20)
plotFromFile('C:\\Users\\User\\Desktop\\Strahinja\\OOA\\Domaći\\7\\average_cumulative_minimum.txt',
             'Iteration', 'AVERAGE Cumulative minimum of cost-function', 1)
