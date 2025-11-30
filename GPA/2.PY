# GPA / CGPA Calculator Program
# Student: Bhumi, Roll No. 14 (VIT)

file_name = "results.txt"

# grade to point table
grade_points = {
    "A+": 10,
    "A": 9,
    "B+": 8,
    "B": 7,
    "C": 6,
    "D": 5,
    "F": 0
}

# ------------------------------------

def read_previous_data():
    data = []
    try:
        with open(file_name, "r") as f:
            for line in f:
                s = line.strip().split(",")
                if len(s) == 3:
                    data.append((int(s[0]), float(s[1]), float(s[2])))
    except FileNotFoundError:
        pass
    return data


def save_sem_data(sem, gpa, credits):
    with open(file_name, "a") as f:
        f.write(f"{sem},{gpa:.2f},{credits}\n")

# ------------------------------------

def get_float(msg):
    while True:
        try:
            return float(input(msg))
        except:
            print("Enter a valid number.")


def get_grade_point(g):
    g = g.strip().upper()
    if g in grade_points:
        return grade_points[g]
    try:
        value = float(g)
        if 0 <= value <= 10:
            return value
    except:
        return None
    return None

# ------------------------------------

def calculate_gpa():
    print("\n--- GPA Calculation ---")
    sub = int(input("How many subjects? "))

    total_cr = 0
    total_pts = 0

    for i in range(1, sub + 1):
        print(f"\nSubject {i}")
        cr = get_float("Credits: ")
        while True:
            g = input("Grade (A+/A/B+/etc or 0-10): ")
            gp = get_grade_point(g)
            if gp is not None:
                break
            print("Invalid grade.")

        total_cr += cr
        total_pts += cr * gp

    if total_cr == 0:
        print("Credits cannot be zero.")
        return

    gpa = total_pts / total_cr
    print(f"\nYour Semester GPA = {gpa:.2f}")

    # save
    old = read_previous_data()
    next_sem = 1 if not old else max(s[0] for s in old) + 1
    save_sem_data(next_sem, gpa, total_cr)
    print(f"Saved as Semester {next_sem}")

# ------------------------------------

def calculate_cgpa():
    print("\n--- CGPA Calculation ---")

    data = read_previous_data()
    if not data:
        print("No saved semester data.")
        return

    total_cr = sum(d[2] for d in data)
    total_w = sum(d[1] * d[2] for d in data)

    if total_cr == 0:
        print("Credits missing.")
        return

    cgpa = total_w / total_cr
    print(f"CGPA from {len(data)} semesters = {cgpa:.2f}")

# ------------------------------------

def show_data():
    print("\n--- Saved Semesters ---")
    data = read_previous_data()
    if not data:
        print("No data available.")
        return

    print("Sem | GPA  | Credits")
    for s, g, c in data:
        print(f"{s}   | {g:.2f} | {c}")

# ------------------------------------

def main():
    while True:
        print("\n===== MENU =====")
        print("1. Calculate Semester GPA")
        print("2. Calculate CGPA")
        print("3. View Saved Data")
        print("4. Clear Data")
        print("5. Exit")

        ch = input("Choose: ")

        if ch == "1":
            calculate_gpa()
        elif ch == "2":
            calculate_cgpa()
        elif ch == "3":
            show_data()
        elif ch == "4":
            open(file_name, "w").close()
            print("Data cleared.")
        elif ch == "5":
            break
        else:
            print("Invalid option.")

main()