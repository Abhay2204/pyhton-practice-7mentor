"""
platform_admin.py
Functions and simple logs for the Platform Administrator (Super Admin).
- View platform overview & user counts
- List and add colleges
- Manage and view all registered users
"""

from database import load_data, save_data, find_user


def get_platform_stats():
    """Returns platform overview numbers and logs."""
    data = load_data()
    users = data.get("users", [])
    colleges = data.get("colleges", [])

    role_counts = {
        "platform_admin": 0,
        "college_admin": 0,
        "teacher_admin": 0,
        "student_admin": 0
    }

    for u in users:
        role = u.get("role", "student_admin")
        if role in role_counts:
            role_counts[role] += 1
        else:
            role_counts[role] = 1

    return {
        "total_users": len(users),
        "total_colleges": len(colleges),
        "role_counts": role_counts
    }


def get_all_users_list():
    """Returns formatted list of all users for display."""
    data = load_data()
    user_list = []
    for u in data.get("users", []):
        user_list.append({
            "username": u.get("username"),
            "full_name": u.get("full_name"),
            "role": u.get("role"),
            "college": u.get("college", "General"),
            "email": u.get("email", "")
        })
    return user_list


def add_college(name, city, code):
    """Add a new college to the system."""
    name = name.strip()
    city = city.strip()
    code = code.strip().upper()

    if not name or not city or not code:
        return {"success": False, "message": "College name, city, and code are required."}

    data = load_data()
    colleges = data.get("colleges", [])

    # Check for duplicate code
    for c in colleges:
        if c.get("code") == code:
            return {"success": False, "message": f"College with code {code} already exists."}

    colleges.append({"name": name, "city": city, "code": code})
    data["colleges"] = colleges
    save_data(data)

    return {"success": True, "message": f"College '{name}' ({code}) added successfully!"}


def get_colleges_list():
    """Return all colleges."""
    data = load_data()
    return data.get("colleges", [])


def remove_user(username):
    """Remove a user from system (cannot remove platform admin)."""
    if username == "admin":
        return {"success": False, "message": "Cannot delete default platform admin."}

    data = load_data()
    users = data.get("users", [])
    initial_len = len(users)

    users = [u for u in users if u["username"].lower() != username.lower()]

    if len(users) == initial_len:
        return {"success": False, "message": f"User '{username}' not found."}

    data["users"] = users
    save_data(data)
    return {"success": True, "message": f"User '{username}' removed successfully."}
