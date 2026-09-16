"""
college_admin.py
Functions and logs for College Administrators.
- View college teachers and students
- Add new teacher to the college
- Add new student to the college
- View college summary stats
"""

from database import load_data
from login import register_user


def get_college_members(college_name):
    """Return all teachers and students belonging to a college."""
    data = load_data()
    teachers = []
    students = []

    for u in data.get("users", []):
        # Match college (case-insensitive)
        if u.get("college", "").strip().lower() == college_name.strip().lower():
            if u.get("role") == "teacher_admin":
                teachers.append(u)
            elif u.get("role") == "student_admin":
                students.append(u)

    return {
        "college": college_name,
        "teachers": teachers,
        "students": students,
        "total_teachers": len(teachers),
        "total_students": len(students)
    }


def add_teacher_for_college(college_name, username, password, full_name, department, email=""):
    """Register a new teacher under this college."""
    extra = {"department": department}
    return register_user(
        username=username,
        password=password,
        full_name=full_name,
        role="teacher_admin",
        college=college_name,
        email=email,
        extra_info=extra
    )


def add_student_for_college(college_name, username, password, full_name, roll_no, branch, email=""):
    """Register a new student under this college."""
    extra = {"roll_no": roll_no, "branch": branch}
    return register_user(
        username=username,
        password=password,
        full_name=full_name,
        role="student_admin",
        college=college_name,
        email=email,
        extra_info=extra
    )
