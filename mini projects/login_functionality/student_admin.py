from database import db, find_user
from login import User


class StudentAdmin(User):
    def __init__(self, username="student1", password="", full_name="Rahul Verma", college="COEP Pune", roll_no="CS-101", branch="Computer Science"):
        super().__init__(username, password, full_name, role="student_admin", college=college, email="rahul@coep.ac.in")
        self.roll_no = roll_no
        self.branch = branch

    def get_report_card(self, username=None):
        target_user = username if username else self.username
        user = find_user(target_user)
        if not user:
            return {"success": False, "message": "Student not found."}

        data = db.load()
        student_marks = [m for m in data.get("marks", []) if m["student_username"].lower() == target_user.lower()]

        total_obtained = sum(m.get("marks", 0) for m in student_marks)
        total_max = sum(m.get("max_marks", 100) for m in student_marks)
        percentage = (total_obtained / total_max * 100) if total_max > 0 else 0

        return {
            "success": True,
            "marks": student_marks,
            "total_obtained": total_obtained,
            "total_max": total_max,
            "percentage": round(percentage, 2),
            "status": "PASSED" if percentage >= 40 else "NEEDS IMPROVEMENT"
        }

    def get_attendance_summary(self, username=None):
        target_user = username if username else self.username
        user = find_user(target_user)
        if not user:
            return {"success": False, "message": "Student not found."}

        data = db.load()
        student_att = [a for a in data.get("attendance", []) if a["student_username"].lower() == target_user.lower()]

        total_conducted = sum(a.get("total_classes", 0) for a in student_att)
        total_attended = sum(a.get("attended_classes", 0) for a in student_att)
        overall_pct = (total_attended / total_conducted * 100) if total_conducted > 0 else 0

        return {
            "success": True,
            "attendance": student_att,
            "total_conducted": total_conducted,
            "total_attended": total_attended,
            "overall_percentage": round(overall_pct, 2),
            "is_eligible": overall_pct >= 75.0,
            "status": "Eligible for Exams (>= 75%)" if overall_pct >= 75.0 else "Low Attendance Warning (< 75%)"
        }


student_power = StudentAdmin()


def get_student_report_card(username):
    return student_power.get_report_card(username)


def get_student_attendance_summary(username):
    return student_power.get_attendance_summary(username)
