import json
import os


class DatabaseManager:
    def __init__(self, filename="users_data.json"):
        self.filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
        self.data = self.load()

    def get_default_data(self):
        return {
            "users": [
                {
                    "username": "admin",
                    "password": "Admin@123",
                    "full_name": "Platform Super Admin",
                    "role": "platform_admin",
                    "college": "Global Platform",
                    "email": "admin@platform.com"
                },
                {
                    "username": "coep_admin",
                    "password": "College@123",
                    "full_name": "COEP College Dean",
                    "role": "college_admin",
                    "college": "COEP Pune",
                    "email": "dean@coep.ac.in"
                },
                {
                    "username": "teacher1",
                    "password": "Teacher@123",
                    "full_name": "Prof. Rajesh Sharma",
                    "role": "teacher_admin",
                    "college": "COEP Pune",
                    "department": "Computer Science",
                    "email": "sharma@coep.ac.in"
                },
                {
                    "username": "student1",
                    "password": "Student@123",
                    "full_name": "Rahul Verma",
                    "role": "student_admin",
                    "college": "COEP Pune",
                    "roll_no": "CS-101",
                    "branch": "Computer Science",
                    "email": "rahul@coep.ac.in"
                }
            ],
            "colleges": [
                {"name": "COEP Pune", "city": "Pune", "code": "COEP01"},
                {"name": "PICT Pune", "city": "Pune", "code": "PICT02"},
                {"name": "MIT Pune", "city": "Pune", "code": "MIT03"}
            ],
            "marks": [
                {"student_username": "student1", "subject": "Python Programming", "marks": 88, "max_marks": 100, "grade": "A"},
                {"student_username": "student1", "subject": "Data Structures", "marks": 92, "max_marks": 100, "grade": "A+"},
                {"student_username": "student1", "subject": "Database Systems", "marks": 81, "max_marks": 100, "grade": "A"}
            ],
            "attendance": [
                {"student_username": "student1", "subject": "Python Programming", "total_classes": 40, "attended_classes": 37},
                {"student_username": "student1", "subject": "Data Structures", "total_classes": 45, "attended_classes": 41},
                {"student_username": "student1", "subject": "Database Systems", "total_classes": 38, "attended_classes": 34}
            ]
        }

    def load(self):
        if not os.path.exists(self.filename):
            data = self.get_default_data()
            self.save(data)
            return data

        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            data = self.get_default_data()
            self.save(data)
            return data

    def save(self, data=None):
        if data is not None:
            self.data = data
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)

    def find_user(self, username):
        self.data = self.load()
        for user in self.data["users"]:
            if user["username"].lower() == username.lower().strip():
                return user
        return None

    def add_user(self, user_dict):
        self.data = self.load()
        self.data["users"].append(user_dict)
        self.save()
        return True

    def reset(self):
        self.data = self.get_default_data()
        self.save()
        return self.data


db = DatabaseManager()


def load_data():
    return db.load()


def save_data(data):
    db.save(data)


def find_user(username):
    return db.find_user(username)


def add_new_user(user_dict):
    return db.add_user(user_dict)


def get_all_users():
    return db.load().get("users", [])


def reset_database():
    return db.reset()
