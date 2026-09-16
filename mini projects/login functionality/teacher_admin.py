"""
teacher_admin.py
Functions and simple logs for Teachers / Faculty.
- View college students
- Assign/update student marks with automatic letter grades
- Record/update student attendance
- View class academic reports
"""

from database import load_data, save_data, find_user


def calculate_grade(marks, max_marks=100):
    """Simple grade calculation function."""
    if max_marks <= 0:
        return "N/A"
    pct = (marks / max_marks) * 100
    if pct >= 90:
        return "A+"
    elif pct >= 80:
        return "A"
    elif pct >= 70:
        return "B"
    elif pct >= 60:
        return "C"
    elif pct >= 50:
        return "D"
    else:
        return "F"


def get_students_for_teacher(college_name):
    """Return all students belonging to the teacher's college."""
    data = load_data()
    students = []
    for u in data.get("users", []):
        if u.get("role") == "student_admin" and u.get("college", "").lower() == college_name.lower():
            students.append({
                "username": u.get("username"),
                "full_name": u.get("full_name"),
                "roll_no": u.get("roll_no", "N/A"),
                "branch": u.get("branch", "N/A")
            })
    return students


def add_student_mark(student_username, subject, marks, max_marks=100):
    """Add or update marks for a student."""
    user = find_user(student_username)
    if not user:
        return {"success": False, "message": f"Student '{student_username}' does not exist."}

    data = load_data()
    marks_list = data.get("marks", [])
    grade = calculate_grade(marks, max_marks)

    updated = False
    for m in marks_list:
        if m["student_username"].lower() == student_username.lower() and m["subject"].lower() == subject.lower():
            m["marks"] = marks
            m["max_marks"] = max_marks
            m["grade"] = grade
            updated = True
            break

    if not updated:
        marks_list.append({
            "student_username": student_username,
            "subject": subject,
            "marks": marks,
            "max_marks": max_marks,
            "grade": grade
        })

    data["marks"] = marks_list
    save_data(data)
    action = "updated" if updated else "saved"
    return {"success": True, "message": f"Marks {action} for {user['full_name']} in {subject} (Grade: {grade})", "grade": grade}


def add_student_attendance(student_username, subject, total_classes, attended_classes):
    """Add or update attendance for a student."""
    user = find_user(student_username)
    if not user:
        return {"success": False, "message": f"Student '{student_username}' does not exist."}

    if attended_classes > total_classes:
        return {"success": False, "message": "Attended classes cannot exceed total classes."}

    data = load_data()
    att_list = data.get("attendance", [])

    updated = False
    for a in att_list:
        if a["student_username"].lower() == student_username.lower() and a["subject"].lower() == subject.lower():
            a["total_classes"] = total_classes
            a["attended_classes"] = attended_classes
            updated = True
            break

    if not updated:
        att_list.append({
            "student_username": student_username,
            "subject": subject,
            "total_classes": total_classes,
            "attended_classes": attended_classes
        })

    data["attendance"] = att_list
    save_data(data)
    pct = (attended_classes / total_classes * 100) if total_classes > 0 else 0
    action = "updated" if updated else "saved"
    return {"success": True, "message": f"Attendance {action} for {user['full_name']}: {attended_classes}/{total_classes} ({pct:.1f}%)"}


def get_all_marks_and_attendance(college_name):
    """Get all marks and attendance for students in this college."""
    students = get_students_for_teacher(college_name)
    student_usernames = {s["username"].lower() for s in students}

    data = load_data()
    college_marks = [m for m in data.get("marks", []) if m["student_username"].lower() in student_usernames]
    college_att = [a for a in data.get("attendance", []) if a["student_username"].lower() in student_usernames]

    return {
        "marks": college_marks,
        "attendance": college_att
    }
