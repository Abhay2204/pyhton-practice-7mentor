import http.server
import socketserver
import json
import os
import urllib.parse
import webbrowser

from database import load_data, reset_database
from login import login_user, register_user, check_password_strength
from platform_admin import get_platform_stats, get_all_users_list, add_college, remove_user, get_colleges_list
from college_admin import get_college_members, add_teacher_for_college, add_student_for_college
from teacher_admin import get_students_for_teacher, add_student_mark, add_student_attendance, get_all_marks_and_attendance
from student_admin import get_student_report_card, get_student_attendance_summary

PORT = 5000
STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")


class PortalRequestHandler(http.server.SimpleHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=STATIC_DIR, **kwargs)

    def _send_json(self, data, status_code=200):
        response_bytes = json.dumps(data).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response_bytes)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(response_bytes)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def _parse_body(self):
        content_len = int(self.headers.get("Content-Length", 0))
        if content_len == 0:
            return {}
        body_bytes = self.rfile.read(content_len)
        try:
            return json.loads(body_bytes.decode("utf-8"))
        except Exception:
            return {}

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        if path == "/api/platform-stats":
            self._send_json(get_platform_stats())
            return
        elif path == "/api/all-users":
            self._send_json({"users": get_all_users_list()})
            return
        elif path == "/api/colleges":
            self._send_json({"colleges": get_colleges_list()})
            return
        elif path == "/api/college-members":
            college = query.get("college", ["COEP Pune"])[0]
            self._send_json(get_college_members(college))
            return
        elif path == "/api/teacher-students":
            college = query.get("college", ["COEP Pune"])[0]
            self._send_json({"students": get_students_for_teacher(college)})
            return
        elif path == "/api/teacher-records":
            college = query.get("college", ["COEP Pune"])[0]
            self._send_json(get_all_marks_and_attendance(college))
            return
        elif path == "/api/student-report":
            username = query.get("username", [""])[0]
            self._send_json(get_student_report_card(username))
            return
        elif path == "/api/student-attendance":
            username = query.get("username", [""])[0]
            self._send_json(get_student_attendance_summary(username))
            return

        super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        body = self._parse_body()

        if path == "/api/check-password":
            password = body.get("password", "")
            result = check_password_strength(password)
            self._send_json(result)
            return
        elif path == "/api/login":
            username = body.get("username", "")
            password = body.get("password", "")
            result = login_user(username, password)
            self._send_json(result)
            return
        elif path == "/api/register":
            username = body.get("username", "")
            password = body.get("password", "")
            full_name = body.get("full_name", "")
            role = body.get("role", "student_admin")
            college = body.get("college", "COEP Pune")
            email = body.get("email", "")
            extra = body.get("extra", {})
            result = register_user(username, password, full_name, role, college, email, extra)
            self._send_json(result)
            return
        elif path == "/api/add-college":
            result = add_college(body.get("name", ""), body.get("city", ""), body.get("code", ""))
            self._send_json(result)
            return
        elif path == "/api/remove-user":
            result = remove_user(body.get("username", ""))
            self._send_json(result)
            return
        elif path == "/api/college-add-teacher":
            result = add_teacher_for_college(
                body.get("college", "COEP Pune"),
                body.get("username", ""),
                body.get("password", ""),
                body.get("full_name", ""),
                body.get("department", "Computer Science"),
                body.get("email", "")
            )
            self._send_json(result)
            return
        elif path == "/api/college-add-student":
            result = add_student_for_college(
                body.get("college", "COEP Pune"),
                body.get("username", ""),
                body.get("password", ""),
                body.get("full_name", ""),
                body.get("roll_no", "CS-000"),
                body.get("branch", "Computer Science"),
                body.get("email", "")
            )
            self._send_json(result)
            return
        elif path == "/api/add-mark":
            student_username = body.get("student_username", "")
            subject = body.get("subject", "")
            marks = float(body.get("marks", 0))
            max_marks = float(body.get("max_marks", 100))
            result = add_student_mark(student_username, subject, marks, max_marks)
            self._send_json(result)
            return
        elif path == "/api/add-attendance":
            student_username = body.get("student_username", "")
            subject = body.get("subject", "")
            total_classes = int(body.get("total_classes", 0))
            attended_classes = int(body.get("attended_classes", 0))
            result = add_student_attendance(student_username, subject, total_classes, attended_classes)
            self._send_json(result)
            return
        elif path == "/api/reset-db":
            reset_database()
            self._send_json({"success": True, "message": "Database successfully reset to default demo records!"})
            return

        self._send_json({"success": False, "message": "Endpoint not found"}, status_code=404)


def run_server():
    os.makedirs(STATIC_DIR, exist_ok=True)

    with socketserver.TCPServer(("", PORT), PortalRequestHandler) as httpd:
        url = f"http://localhost:{PORT}"
        print("=" * 60)
        print("   MULTI-ROLE LOGIN SYSTEM & BACKEND SERVER RUNNING")
        print("=" * 60)
        print(f" [+] Web App URL : {url}")
        print(f" [+] Static Files: {STATIC_DIR}")
        print(" [+] Press Ctrl+C in terminal to stop server.")
        print("=" * 60)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[-] Server stopped.")


if __name__ == "__main__":
    run_server()
