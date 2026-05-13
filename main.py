from pyscript import display, document

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']


def plot_graph(data):
    plt.clf()
    plt.plot(days, data)
    plt.title("Weekly Attendance")
    plt.xlabel("Days")
    plt.ylabel("Absences")
    display(plt, target="output2")


def displaying_output(e):
    selected_day = document.getElementById("input1").value
    absence_value = document.getElementById("input2").value

    if absence_value.isdigit():
        absence_value = int(absence_value)
    else:
        absence_value = 0

    day_index_map = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4
    }

    values = [0, 0, 0, 0, 0]
    values[day_index_map.get(selected_day, 0)] = absence_value

    plot_graph(values)
