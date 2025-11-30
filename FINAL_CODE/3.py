# GPA & CGPA Calculator 
# Student: Bhumi, Roll No. 14, VIT

FILE_NAME = "results.txt"

# Grade conversion table
GRADE_POINTS = {
    "A+": 10,
    "A": 9,
    "B+": 8,
    "B": 7,
    "C": 6,
    "D": 5,
    "F": 0
}


# ---------------------- FILE HANDLING ----------------------

def load_previous_semesters():
    """Reads saved semester data from file"""
    data = []
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                sem, gpa, credits = line.strip().split(",")
                data.append((int(sem), float(gpa), float(credits)))
    except FileNotFoundError:
        pass
    return data


def append_semester_to_file(sem_no, gpa, credits):
    """Adds one semester entry to the file"""
    with open(FILE_NAME, "a") as f:
        f.write(f"{sem_no},{gpa:.3f},{credits}\n")


# ---------------------- INPUT UTILITIES ----------------------

def read_float(msg):
    """Safely read float input"""
    while True:
        try:
            return float(input(msg).strip())
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def convert_grade_to_points(grade):
    """Converts letter grade or numeric input to grade points"""
    grade = grade.strip().upper()

    if grade in GRADE_POINTS:
        return GRADE_POINTS[grade]

    try:
        val = float(grade)
        if 0 <= val <= 10:
            return val
    except:
        return None

    return None


# ---------------------- GPA CALCULATION ----------------------

def compute_semester_gpa():
    print("\n--- SEMESTER GPA CALCULATION ---")

    num_subjects = int(input("Enter total subjects: "))

    total_credits = 0
    total_weighted_points = 0

    for i in range(1, num_subjects + 1):
        print(f"\nSubject {i}")
        credit = read_float("  Credit hours: ")

        while True:
            grade_input = input("  Grade (A+/A/B+/etc OR 0-10): ")
            gp = convert_grade_to_points(grade_input)
            if gp is not None:
                break
            print("  Invalid grade. Please try again.")

        total_credits += credit
        total_weighted_points += credit * gp

    if total_credits == 0:
        print("No credits entered. GPA cannot be calculated.")
        return None, None

    gpa = total_weighted_points / total_credits
    print(f"\nSemester GPA = {gpa:.3f} | Total Credits = {total_credits}")

    previous = load_previous_semesters()
    next_sem_no = 1 if not previous else max(sem[0] for sem in previous) + 1

    append_semester_to_file(next_sem_no, gpa, total_credits)
    print(f"Semester {next_sem_no} saved successfully!\n")

    return gpa, total_credits


# ---------------------- CGPA CALCULATION ----------------------

def compute_cgpa():
    print("\n--- CGPA CALCULATION ---")

    semesters = load_previous_semesters()

    if not semesters:
        print("No saved semesters found.")
        manual = input("Do you want to enter previous semester details manually? (y/n): ").lower()
        if manual != 'y':
            return None

        count = int(input("How many semesters to enter? "))
        for i in range(count):
            g = read_float(f"GPA of semester {i+1}: ")
            c = read_float(f"Credits of semester {i+1}: ")
            semesters.append((i+1, g, c))

    total_credits = sum(item[2] for item in semesters)
    if total_credits == 0:
        print("Credits are zero. CGPA cannot be calculated.")
        return None

    weighted_sum = sum(item[1] * item[2] for item in semesters)
    cgpa = weighted_sum / total_credits

    print(f"\nCGPA based on {len(semesters)} semesters = {cgpa:.3f}")
    return cgpa


# ---------------------- VIEW SAVED DATA ----------------------

def display_saved_data():
    print("\n--- SAVED SEMESTER RECORDS ---")
    semesters = load_previous_semesters()

    if not semesters:
        print("No data available.")
        return

    print("Sem | GPA     | Credits")
    print("-------------------------")
    for sem, gpa, cr in semesters:
        print(f"{sem:3} | {gpa:7.3f} | {cr}")


# ---------------------- MAIN MENU ----------------------

def main_menu():
    while True:
        print("\n===== GPA / CGPA CALCULATOR =====")
        print("1. Calculate & Save Semester GPA")
        print("2. Calculate CGPA")
        print("3. View All Saved Semesters")
        print("4. Clear All Data")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            compute_semester_gpa()

        elif choice == "2":
            compute_cgpa()

        elif choice == "3":
            display_saved_data()

        elif choice == "4":
            confirm = input("Are you sure you want to delete all data? (y/n): ").lower()
            if confirm == "y":
                open(FILE_NAME, "w").close()
                print("All saved records cleared.")

        elif choice == "5":
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid option. Try again.")


main_menu()