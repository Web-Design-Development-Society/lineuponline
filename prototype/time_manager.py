import csv
import os

CLASS_CODE_INDEX = 0
DIFF_LEVEL_INDEX = 1
CREDITS_INDEX = 2
HR_IN_CLASS_INDEX = 3


def main():
    try:
        # Create a loop that asks the user for class input that
        # loops through asking for each class and info
        # until user has given all their classes

        # Ask for the student's name
        student_name = input("Please insert the student's name: ").strip()

        # Create empty list
        classes = []
        # Create if statement so the user can input the name of their precreated csv file.

        have_classes_csv = input("Do you already have a csv file from this program? (yes or no): ").lower()
        if have_classes_csv != "y" and have_classes_csv != 'yes':
            while True:
                try:
                    # Gather class details
                    class_code = input("Please type in the class code: ").strip()
                    diff_level = int(input("Please type in the difficulty level of this class (1-3) 3 being hardest and 1 being lowest: "))
                    credits = int(input("Please enter how many credits this class is: "))
                    hr_in_class = int(input("Please enter in the number of hours you are in this class a week: "))

                    # Add class information as a dictionary
                    classes.append({
                        "class_code": class_code,
                        "class_difficulty": diff_level,
                        "credits": credits,
                        "hours_in_class": hr_in_class
                    })

                    # Ask if the user wants to add another class
                    add_class = input("Do you want to add another class? (yes/no): ").strip().lower()
                    if add_class != "yes" and add_class != "y":
                        break
                except ValueError as e:
                    print(f"Invalid input: {e}. \n Please enter valid numbers for difficulty, credits, and hours")
            filename = write_file(student_name, classes)
        else: 
            while True:
                filename = input("Please enter your file name: ").strip()
                if filename and filename.endswith(".csv"):
                    try:
                        with open(filename, "rt") as file:
                            break  # File exists, break out of the loop
                    except FileNotFoundError:
                        print("ERROR: File not found, please enter a valid file name.")
                else:
                    print("Invalid input. Please enter a valid CSV file name.")
                    # break

        # append the list as an array inside of classes[]
        # make the for loop go until the user is done.
        have_weekly_csv = input("Do you already have a weekly.csv file from this program? (yes or no): ").lower()
        if have_weekly_csv != "y" and have_weekly_csv != 'yes':
            weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
            weekly_time = []
            total_available_hrs = 0
            print("Let's walk you through organizing your schedule. Please answer the following questions about each week day")
            for date in weekdays:
                try:

                    print(date)
                    class_per_day = float(input(f"How many hours are you in class on {date}? "))
                    lunch = float(input(f"How long do you take for lunch? "))
                    available_hrs = 9 - (class_per_day + lunch)
                    print()
                    print(f"{available_hrs} hours available.")
                    print()
                    weekly_time.append({
                        "day": date,
                        "classes_per_day": class_per_day,
                        "lunch": lunch,
                        "available_hrs": available_hrs
                    })
                    total_available_hrs += available_hrs
                    
                except ValueError as e:
                    print(f"Invalid input: {e}. \n Please enter valid numbers for difficulty, credits, and hours")
            write_weekfile(student_name, weekly_time)
            
        else:
            total_available_hrs = 0

            while True:
                weekly_filename = input("Please enter your file name (include .csv): ").strip()
            
                # Automatically add .csv if missing
                if not weekly_filename.endswith(".csv"):
                    weekly_filename += ".csv"
            
                try:
                    with open(weekly_filename, "rt") as file:
                        reader = csv.DictReader(file)
                        for row in reader:
                            try:
                                available_hrs = float(row["available_hrs"])
                                total_available_hrs += available_hrs
                            except (KeyError, ValueError):
                                print(f"Invalid data in row: {row}")
                    print(f"\nFile '{weekly_filename}' loaded successfully.")
                    break  # Exit the loop if the file is read successfully

                except FileNotFoundError:
                    print("ERROR: File not found, please check the file name and try again.")

            # except Exception as e:
            #     print(f"ERROR: An unexpected error occured {e}")

            print(f"\nTotal available hours for the week: {total_available_hrs:.2f}")
        print()
        # average_study_time = read_file(filename)
        # print(average_study_time)

        read_file(filename, total_available_hrs)
        # print(classes)

    except Exception as e:
        print(f"ERROR: An error occurred: {e}")

def write_file(student_name, classes):
    try:
        # Write into the file named the student's name their classes and class info.
        filename = f"{student_name.replace(' ','_')}_classes.csv"

        with open(filename, mode="w", newline="") as student_schedule:
            # DictWriter is a class in python used for csv modules. It allows the data to be represented as a dictionary.

            # Create a DictWriter with fieldnames matching class dictionaries
            fieldnames = ["class_code", "class_difficulty", "credits", "hours_in_class"]
            writer = csv.DictWriter(student_schedule, fieldnames=fieldnames)

            # writer.writerow(student_name)

            # Write the header and rows
            writer.writeheader()
            writer.writerows(classes)
            
        print(f"CSV file '{filename}' successfully created.")
        return filename
    except IOError as e:
        print(f"An error occured writing the Dictionary: {e}")

# Read the csv file to access the info
def read_file(filename, total_available_hrs):

    with open(filename, "rt") as student_schedule:
        reader = csv.DictReader(student_schedule)
        # next(reader)
    
        print("\nStudy Time needed for Each Class: ")
        total_study_time = 0
        for row in reader:
            study_time = study_time_calculator(
                int(row["class_difficulty"]),
                int(row["credits"]),
                int(row["hours_in_class"])
            )
            print(f"Class {row['class_code']} requires {study_time} hours of study time each week")
            total_study_time += study_time
        if int(row['hours_in_class']) != 0:
            min_for_A = total_study_time / int(row['hours_in_class'])
        else:
            min_for_A = 0
        A_plus = total_study_time
        C = total_study_time / 3
        B = (total_study_time + C) / 2

        mid_for_A = (A_plus + B) / 2

        print(total_study_time)
        print(f"You need to study \n {A_plus} hours weekly to get a A+ \n {B:.1f} hours weekly to get a B \n {C:.1f} hours weekly to get a C")
        print()
        print(f"If your want to pass you need to study a range of: \n {min_for_A:.1f} - {A_plus:.1f} hrs/wk \n or an average of {mid_for_A:.1f} hours each week")
        print()
        print(f"A+ = {A_plus:.1f} hours/wk")
        print(f"A = {mid_for_A:.1f} hours/wk")
        print(f"B = {B:.1f} hours/wk")
        print(f"C = {C:.1f} hours/wk")
        total_time = total_available_hrs - mid_for_A
        print(f"You have {total_time} hours left over after studying from 8am-5pm")     



def study_time_calculator(diff_level, credits, hrs_in_class):
    # """Calculate the study time needed to get A's in each class"""

    cal = ((credits + 1) * diff_level) - hrs_in_class
    if cal < 1:
        cal = 1
    return cal

def write_weekfile(student_name, weekly_time):
    # Write into the file named the student's name their classes and class info.
    week_filename = f"{student_name.replace(' ','_')}_weekly.csv"

    with open(week_filename, mode="w", newline="") as student_schedule:
        # DictWriter is a class in python used for csv modules. It allows the data to be represented as a dictionary.

        # Create a DictWriter with fieldnames matching class dictionaries
        fieldnames = ["day", "classes_per_day", "lunch", "available_hrs"]

        writer = csv.DictWriter(student_schedule, fieldnames=fieldnames)

        # writer.writerow(student_name)

        # Write the header and rows
        writer.writeheader()
        for day_info in weekly_time:
                    # Ensure you're appending a dictionary, not just the available hours
                    writer.writerow(day_info)
                
    print(f"CSV file '{week_filename}' successfully created.")
    return week_filename




if __name__ == "__main__":
    main()