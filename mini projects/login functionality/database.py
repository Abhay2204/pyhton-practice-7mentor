"""
database.py
Simple database management for the login system.
Stores and manages users, colleges, marks, and attendance using a clean JSON database file.
Easy to understand, modify, and inspect!
"""

import json
import os

# File where all user data is saved
DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "users_data.json")


def get_default_data():
    """Returns initial pre-configured data with demo accounts for each role."""
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


def load_data():
    """Load data from JSON file. If file doesn't exist, create it with default data."""
    if not os.path.exists(DB_FILE):
        data = get_default_data()
        save_data(data)
        return data

    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        data = get_default_data()
        save_data(data)
        return data


def save_data(data):
    """Save the python dictionary into the JSON database file."""
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


# Simple Helper Functions
def find_user(username):
    """Find a user by username."""
    data = load_data()
    for user in data["users"]:
        if user["username"].lower() == username.lower().strip():
            return user
    return None


def add_new_user(user_dict):
    """Add a new user dictionary to the database."""
    data = load_data()
    data["users"].append(user_dict)
    save_data(data)
    return True


def get_all_users():
    """Return list of all users."""
    data = load_data()
    return data.get("users", [])


def reset_database():
    """Reset the database to initial default demo records."""
    data = get_default_data()
    save_data(data)
    return data


# Auto-initialize database on import
load_data()
