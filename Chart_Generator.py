from SimpleGraphics import *

# CHART MENU #
print("Chart Creation Menu:")
print("1. Pie Chart")
print("2. Bar Chart")

# SELECTION #
selection = int(input("Select your chart type: "))

if selection == 1:
    # INPUTS #
    title = input("Enter the title of the chart: ")
    sectors = int(input("Enter the number of sectors (2 to 6): "))
    valueAll = int(input("Enter the total value of all sectors: "))

    # DRAWING SETUP #
    setFont("Times New Roman", 24)
    text(400, 50, title)
    diameter = 400
    pieX = 200
    pieY = 150
    currentAngle = 0

    # LABEL AND VALUE OF SECTORS #
    i = 1
    sumValues = 0

    while i < sectors:
        label = input("Label sector " + str(i) + ": ")
        value = int(input("Enter the value of the " + str(label) + " sector: "))

        # DRAW CHART #
        sweepAngle = (value / valueAll) * 360
        setFill((i * 50) % 255, (i * 100) % 255, (i * 150) % 255)
        pieSlice(pieX, pieY, diameter, diameter, currentAngle, sweepAngle)
        currentAngle = currentAngle + sweepAngle

        # COLORS AND LABELS #
        legendY = 100 + (i * 60)
        rect(670, legendY, 30, 30)
        text(685, legendY - 15, label)

        sumValues = sumValues + value
        i = i + 1

    # LAST LABEL AND VALUE #
    lastLabel = input("Label sector " + str(sectors) + ": ")
    lastValue = valueAll - sumValues

    #COLORS AND LABELS #
    setFill((sectors * 50) % 255, (sectors * 100) % 255, (sectors * 150) % 255)
    legendY = 100 + (sectors * 60)
    rect(670, legendY, 30, 30)
    text(685, legendY - 15, lastLabel)

    # 3. DRAW THE LAST CHART SLICE #
    lastSweepAngle = (lastValue / valueAll) * 360
    pieSlice(pieX, pieY, diameter, diameter, currentAngle, lastSweepAngle)

    print("Your chart is complete")

elif selection == 2:
    # INPUTS #
    title = input("Enter the title of the chart: ")
    bars = int(input("Enter the number of bars (2 to 6): "))
    interval = int(input("Enter the gridline interval (10 to 100): "))
    yAxis = input("Enter the label for the Y-Axis: ")

    # DRAWING SETUP #
    setFont("Times New Roman", 24)
    text(400, 50, title)

    # X AND Y AXIS #
    line(100, 100, 100, 500)  # Y AXIS
    line(100, 500, 700, 500)  # X AXIS

    # Y AXIS LABEL #
    setFont("Times New Roman", 16)
    text(50, 300, yAxis)

    # GRIDLINES #
    currentGrid = interval
    while currentGrid <= 400:
        gridY = 500 - currentGrid
        line(100, gridY, 700, gridY)
        text(720, gridY, str(currentGrid))
        currentGrid = currentGrid + interval

    text(720, 500, "0")

    i = 1
    while i <= bars:
        label = input("Label bar " + str(i) + ": ")
        value = int(input("Enter the value of bar " + str(label) + ": "))

        # BAR MATH #
        section = 600 / bars
        barWidth = section - 40
        barX = 100 + (i - 1) * section + 20
        barY = 500 - value

        # DRAW BAR #
        setFill((i * 50) % 255, (i * 100) % 255, (i * 150) % 255)
        rect(barX, barY, barWidth, value)

        # LABELS AND VALUES #
        setFill("black")
        text(barX + (barWidth / 2), 520, label)
        text(barX + (barWidth / 2), barY + 15, value)

        i = i + 1

    print("Your chart is completed.")