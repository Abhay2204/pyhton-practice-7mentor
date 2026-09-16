from database import db
from login import User, register_user


class CollegeAdmin(User):
    def __init__(self, username="coep_admin", password="", full_name="COEP College Dean", college="COEP Pune"):
        super().__init__(username, password, full_name, role="college_admin", college=college, email="dean@coep.ac.in")

    def get_members(self, college_name=None):
        target_college = college_name if college_name else self.college
        data = db.load()
        teachers = []
        students = []

        for u in data.get("users", []):
            if u.get("college", "").strip().lower() == target_college.strip().lower():
                if u.get("role") == "teacher_admin":
                    teachers.append(u)
                elif u.get("role") == "student_admin":
                    students.append(u)

        return {
            "college": target_college,
            "teachers": teachers,
            "students": students,
            "total_teachers": len(teachers),
            "total_students": len(students)
        }

    def add_teacher(self, username, password, full_name, department, email="", college_name=None):
        target_college = college_name if college_name else self.college
        extra = {"department": department}
        return register_user(
            username=username,
            password=password,
            full_name=full_name,
            role="teacher_admin",
            college=target_college,
            email=email,
            extra_info=extra
        )

    def add_student(self, username, password, full_name, roll_no, branch, email="", college_name=None):
        target_college = college_name if college_name else self.college
        extra = {"roll_no": roll_no, "branch": branch}
        return register_user(
            username=username,
            password=password,
            full_name=full_name,
            role="student_admin",
            college=target_college,
            email=email,
            extra_info=extra
        )


college_power = CollegeAdmin()


def get_college_members(college_name):
    return college_power.get_members(college_name)


def add_teacher_for_college(college_name, username, password, full_name, department, email=""):
    return college_power.add_teacher(username, password, full_name, department, email, college_name)


def add_student_for_college(college_name, username, password, full_name, roll_no, branch, email=""):
    return college_power.add_student(username, password, full_name, roll_no, branch, email, college_name)
