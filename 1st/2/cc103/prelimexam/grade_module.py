
def compute_average(grades):
    total = sum(grades)
    average = total / len(grades)
    return average


def determine_status(average):
    if average >= 90:
        return "Excellent"
    elif average >= 75:
        return "Passed"
    else:
        return "Failed"
