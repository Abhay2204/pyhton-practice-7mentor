"""
login.py
Authentication, Registration & Password Strength Checker.
Contains simple logic for:
1. Password strength evaluation (weak/medium/strong)
2. New user registration with validation
3. Old user login verification
"""

import string
from database import find_user, add_new_user, load_data


def check_password_strength(password):
    """
    Evaluates password strength based on standard rules:
    - Minimum length 8 characters
    - Contains lowercase letters (a-z)
    - Contains uppercase letters (A-Z)
    - Contains numbers (0-9)
    - Contains special symbols (!@#$%^&*...)
    
    Returns:
        dict: {
            "score": int (0-100),
            "level": "Weak" | "Medium" | "Strong" | "Very Strong",
            "is_valid": bool (True if score >= 60),
            "feedback": list of improvement tips
        }
    """
    score = 0
    feedback = []

    if not password:
        return {
            "score": 0,
            "level": "Very Weak",
            "is_valid": False,
            "feedback": ["Password cannot be empty."]
        }

    # 1. Length check
    if len(password) >= 8:
        score += 25
    else:
        feedback.append("Make it at least 8 characters long.")

    # 2. Lowercase check
    has_lower = any(c.islower() for c in password)
    if has_lower:
        score += 20
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    # 3. Uppercase check
    has_upper = any(c.isupper() for c in password)
    if has_upper:
        score += 20
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    # 4. Digit check
    has_digit = any(c.isdigit() for c in password)
    if has_digit:
        score += 20
    else:
        feedback.append("Add at least one number (0-9).")

    # 5. Special character check
    special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"
    has_special = any(c in special_chars for c in password)
    if has_special:
        score += 15
    else:
        feedback.append("Add at least one special symbol (!@#$%^&*...).")

    # Determine level
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
    """
    Login logic for existing (old) users.
    Verifies if username exists and password matches.
    """
    if not username or not password:
        return {"success": False, "message": "Please provide both username and password."}

    user = find_user(username)
    if not user:
        return {"success": False, "message": f"User '{username}' does not exist. Please register first."}

    if user["password"] != password:
        return {"success": False, "message": "Incorrect password. Please try again."}

    # Successful login
    # Return user details without sensitive fields
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
    """
    Registration logic for new users.
    Checks password strength, checks username uniqueness, and saves the new user.
    """
    username = username.strip()
    full_name = full_name.strip()

    if not username or not password or not full_name:
        return {"success": False, "message": "Username, password, and full name are required."}

    # Check if username already exists
    if find_user(username):
        return {"success": False, "message": f"Username '{username}' is already taken. Please choose another."}

    # Password strength check
    strength = check_password_strength(password)
    if not strength["is_valid"]:
        tips = " ".join(strength["feedback"])
        return {
            "success": False,
            "message": f"Password is too weak ({strength['level']}). {tips}"
        }

    new_user = {
        "username": username,
        "password": password,
        "full_name": full_name,
        "role": role,
        "college": college,
        "email": email
    }

    if extra_info and isinstance(extra_info, dict):
        new_user.update(extra_info)

    # Save to database
    add_new_user(new_user)

    return {
        "success": True,
        "message": f"Account for '{full_name}' created successfully! You can now log in.",
        "username": username
    }
