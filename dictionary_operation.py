student = {
    "name": "Alice Wong",
    "student_id": "ST1024",
    "age": 21,
    "program": "Software Engineering",
    "city": "Nanjing",
    "gpa": 3.6
}


# First, display the complete record using for loop, printing and some string formatting only
print("Current student record:")
for key, value in student.items():
    print(f"{key.replace('_', ' ').title()}: {value}")


# Check if there's a key called 'email'. If not, ask the user to enter an email
if "email" not in student:
    email = input("Enter the student's email: ").strip()
    while email == "":
        print("Email cannot be empty.")
        email = input("Enter the student's email: ").strip()
    student["email"] = email


# Ask the user to enter a new city, and update the existing city with this new one
# Make sure the new city is not an empty string
new_city = input("Enter a new city: ").strip()
while new_city == "":
    print("City cannot be empty.")
    new_city = input("Enter a new city: ").strip()
student["city"] = new_city


# Check if there's 'phone' key in the dictionary. If not, print a message saying "Phone number not found."
# Use the get() method
phone = student.get("phone")
if phone is None:
    print("Phone number not found.")


# Add a new key called 'contact' to the dictionary, which is itself a dictionary containing two keys: 'phone' and 'email'.
if phone is None:
    phone = input("Enter the student's phone number: ").strip()
    while phone == "":
        print("Phone number cannot be empty.")
        phone = input("Enter the student's phone number: ").strip()

student["contact"] = {
    "phone": phone,
    "email": student["email"]
}



# Add another key called 'courses' to the dictionary, which is itself a dictionary containing three keys: 'Python', 'Databases', and 'Software Engineering', with 88, 91, and 84 as their corresponding scores
student["courses"] = {
    "Python": 88,
    "Databases": 91,
    "Software Engineering": 84
}


# Calculate the average score for the student without built-in functions like sum(). Use a for loop instead. 
total_score = 0
course_count = 0
for score in student["courses"].values():
    total_score += score
    course_count += 1

average_score = total_score / course_count
student["average_score"] = average_score


# Add a new key called 'academic_status' to the dictionary
# It should be a string that indicates the student's academic status based on the average score. 
# If the score is >= 90, the status should be "Excellent".
# If the score is >= 75, the status should be "Good".
# If the score is >= 60, the status should be "Pass".
# If the score is < 60, the status should be "At Risk".
if average_score >= 90:
    student["academic_status"] = "Excellent"
elif average_score >= 75:
    student["academic_status"] = "Good"
elif average_score >= 60:
    student["academic_status"] = "Pass"
else:
    student["academic_status"] = "At Risk"

# Add the logic to search for a course. 
# If the course is found, print the course name and score. If not, print "Course not found".
course_to_search = input("Enter a course to search for: ").strip()
found_course = None
for course_name in student["courses"]:
    if course_name.lower() == course_to_search.lower():
        found_course = course_name
        break

if found_course is not None:
    print(f"{found_course}: {student['courses'][found_course]}")
else:
    print("Course not found")



# Add the logic to update a course score. 
# Ask the user to enter the course name and the new score. 
# If the course is found, then update the score and print a message indicating the change.
# While adding the new course, make sure the new score is a number between 0 and 100
course_to_update = input("Enter a course to update: ").strip()
update_course = None
for course_name in student["courses"]:
    if course_name.lower() == course_to_update.lower():
        update_course = course_name
        break

if update_course is None:
    print("Course not found")
else:
    while True:
        new_score_text = input("Enter the new score (0-100): ").strip()
        try:
            new_score = float(new_score_text)
            if 0 <= new_score <= 100:
                break
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Score must be a number.")

    old_score = student["courses"][update_course]
    student["courses"][update_course] = new_score
    print(f"{update_course} score updated from {old_score:g} to {new_score:g}.")



# Recaclculate the average score and update the academic status after the course score has been updated.
total_score = 0
course_count = 0
for score in student["courses"].values():
    total_score += score
    course_count += 1

average_score = total_score / course_count
student["average_score"] = average_score

if average_score >= 90:
    student["academic_status"] = "Excellent"
elif average_score >= 75:
    student["academic_status"] = "Good"
elif average_score >= 60:
    student["academic_status"] = "Pass"
else:
    student["academic_status"] = "At Risk"



# Display the final formatted student record with all the updated information, including the average score and academic status.
# It should look like the following: 
""" 
=====================================
        STUDENT RECORD
=====================================

Name: Alice Wong
Student ID: ST1024
Age: 21
Program: Software Engineering
City: Shanghai
GPA: 3.6

CONTACT
Phone: 13800001111
Email: alice.wong@university.edu

COURSE RESULTS
Python: 88
Databases: 91
Software Engineering: 84

Average Score: 87.7
Academic Status: Good

===================================== """
print("\n=====================================")
print("        STUDENT RECORD")
print("=====================================\n")
print(f"Name: {student['name']}")
print(f"Student ID: {student['student_id']}")
print(f"Age: {student['age']}")
print(f"Program: {student['program']}")
print(f"City: {student['city']}")
print(f"GPA: {student['gpa']}\n")

print("CONTACT")
print(f"Phone: {student['contact']['phone']}")
print(f"Email: {student['contact']['email']}\n")

print("COURSE RESULTS")
for course_name, score in student["courses"].items():
    print(f"{course_name}: {score:g}")

print(f"\nAverage Score: {student['average_score']:.1f}")
print(f"Academic Status: {student['academic_status']}\n")
print("=====================================")
