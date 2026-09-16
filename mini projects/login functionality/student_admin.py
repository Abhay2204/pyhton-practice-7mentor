"""
student_admin.py
Functions and simple logs for Students.
- View personal profile
- View subject marks & calculate overall percentage
- View attendance records & check 75% minimum eligibility
"""

from database import load_data, find_user


def get_student_report_card(username):
    """
    Returns full academic marks card for the student.
    Calculates total marks, obtained marks, percentage, and passed/failed status.
    """
    user = find_user(username)
    if not user:
        return {"success": False, "message": "Student not found."}

    data = load_data()
    student_marks = [m for m in data.get("marks", []) if m["student_username"].lower() == username.lower()]

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


def get_student_attendance_summary(username):
    """
    Returns attendance records and calculates overall percentage.
    Checks if attendance satisfies the mandatory 75% criteria.
    """
    user = find_user(username)
    if not user:
        return {"success": False, "message": "Student not found."}

    data = load_data()
    student_att = [a for a in data.get("attendance", []) if a["student_username"].lower() == username.lower()]

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
