def score_to_point(score):
    if score >= 80:
        return 5.0
    elif score >= 70:
        return 4.0
    elif score >= 60:
        return 3.0
    elif score >= 50:
        return 2.0
    else:
        return 0.0

courses = {
    "EIE 326": 3,
    "EIE 327": 3,
    "GEC 324": 2,
    "CIT 322": 0,
    "EIE 323": 3,
    "TMC 321": 1
}

total_points = 0
total_units = 0
report_lines = []

print("Enter your scores for the following courses:\n")

for course, units in courses.items():
    while True:
        try:
            score = float(input(f"{course} score: "))
            if 0 <= score <= 100:
                break
            else:
                print("Please enter a valid score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric score.")

    point = score_to_point(score)
    course_points = point * units
    total_points += course_points
    total_units += units

    line = f"{course}: Score = {score}, Grade Point = {point}, Units = {units}, Points = {course_points}"
    print(line)
    report_lines.append(line)

if total_units == 0:
    print("\nNo valid credit units found. Cannot compute GPA.")
else:
    gpa = total_points / total_units
    summary = f"\nTotal Grade Points: {total_points}\nTotal Credit Units: {total_units}\nCalculated GPA: {gpa:.2f}"
    print(summary)
    report_lines.append(summary)

    # Save to file
    with open("gpa_report.txt", "w") as f:
        f.write("GPA Calculation Report\n\n")
        for line in report_lines:
            f.write(line + "\n")

    print("\nReport saved to 'gpa_report.txt'.")
