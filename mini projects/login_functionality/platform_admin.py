from database import db
from login import User


class PlatformAdmin(User):
    def __init__(self, username="admin", password="", full_name="Platform Super Admin"):
        super().__init__(username, password, full_name, role="platform_admin", college="Global Platform", email="admin@platform.com")

    def get_stats(self):
        data = db.load()
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

    def get_all_users(self):
        data = db.load()
        users = []
        for u in data.get("users", []):
            users.append({
                "username": u.get("username"),
                "full_name": u.get("full_name"),
                "role": u.get("role"),
                "college": u.get("college", "General"),
                "email": u.get("email", "")
            })
        return users

    def add_college(self, name, city, code):
        name = name.strip()
        city = city.strip()
        code = code.strip().upper()

        if not name or not city or not code:
            return {"success": False, "message": "College name, city, and code are required."}

        data = db.load()
        colleges = data.get("colleges", [])

        for c in colleges:
            if c.get("code") == code:
                return {"success": False, "message": f"College with code {code} already exists."}

        colleges.append({"name": name, "city": city, "code": code})
        data["colleges"] = colleges
        db.save(data)

        return {"success": True, "message": f"College '{name}' ({code}) added successfully!"}

    def get_colleges(self):
        data = db.load()
        return data.get("colleges", [])

    def remove_user(self, username):
        if username.lower() == "admin":
            return {"success": False, "message": "Cannot delete default platform admin."}

        data = db.load()
        users = data.get("users", [])
        initial_len = len(users)

        users = [u for u in users if u["username"].lower() != username.lower()]

        if len(users) == initial_len:
            return {"success": False, "message": f"User '{username}' not found."}

        data["users"] = users
        db.save(data)
        return {"success": True, "message": f"User '{username}' removed successfully."}


admin_power = PlatformAdmin()


def get_platform_stats():
    return admin_power.get_stats()


def get_all_users_list():
    return admin_power.get_all_users()


def add_college(name, city, code):
    return admin_power.add_college(name, city, code)


def get_colleges_list():
    return admin_power.get_colleges()


def remove_user(username):
    return admin_power.remove_user(username)
