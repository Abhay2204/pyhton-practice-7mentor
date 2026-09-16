from database import db, find_user, add_new_user


class User:
    def __init__(self, username, password, full_name, role="student_admin", college="COEP Pune", email=""):
        self.username = username.strip()
        self.password = password
        self.full_name = full_name.strip()
        self.role = role
        self.college = college
        self.email = email

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "full_name": self.full_name,
            "role": self.role,
            "college": self.college,
            "email": self.email
        }


def check_password_strength(password):
    score = 0
    feedback = []

    if not password:
        return {
            "score": 0,
            "level": "Very Weak",
            "is_valid": False,
            "feedback": ["Password cannot be empty."]
        }

    if len(password) >= 8:
        score += 25
    else:
        feedback.append("Make it at least 8 characters long.")

    has_lower = any(c.islower() for c in password)
    if has_lower:
        score += 20
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    has_upper = any(c.isupper() for c in password)
    if has_upper:
        score += 20
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    has_digit = any(c.isdigit() for c in password)
    if has_digit:
        score += 20
    else:
        feedback.append("Add at least one number (0-9).")

    special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"
    has_special = any(c in special_chars for c in password)
    if has_special:
        score += 15
    else:
        feedback.append("Add at least one special symbol (!@#$%^&*...).")

    if score < 40:
        level = "Weak"
    elif score < 70:
        level = "Medium"
    elif score < 90:
        level = "Strong"
    else:
        level = "Very Strong"

    return {
        "score": score,
        "level": level,
        "is_valid": score >= 60,
        "feedback": feedback
    }


def login_user(username, password):
    if not username or not password:
        return {"success": False, "message": "Please provide both username and password."}

    user = find_user(username)
    if not user:
        return {"success": False, "message": f"User '{username}' does not exist. Please register first."}

    if user["password"] != password:
        return {"success": False, "message": "Incorrect password. Please try again."}

    user_info = {
        "username": user["username"],
        "full_name": user["full_name"],
        "role": user["role"],
        "college": user.get("college", "General"),
        "email": user.get("email", ""),
        "department": user.get("department", ""),
        "roll_no": user.get("roll_no", "")
    }
    return {
        "success": True,
        "message": f"Welcome back, {user['full_name']}!",
        "user": user_info
    }


def register_user(username, password, full_name, role="student_admin", college="COEP Pune", email="", extra_info=None):
    if not username or not password or not full_name:
        return {"success": False, "message": "Username, password, and full name are required."}

    if find_user(username):
        return {"success": False, "message": f"Username '{username}' is already taken. Please choose another."}

    strength = check_password_strength(password)
    if not strength["is_valid"]:
        tips = " ".join(strength["feedback"])
        return {
            "success": False,
            "message": f"Password is too weak ({strength['level']}). {tips}"
        }

    new_user = User(username, password, full_name, role, college, email)
    user_dict = new_user.to_dict()

    if extra_info and isinstance(extra_info, dict):
        user_dict.update(extra_info)

    add_new_user(user_dict)

    return {
        "success": True,
        "message": f"Account for '{full_name}' created successfully! You can now log in.",
        "username": username
    }
