# Multi-Role College Management & Login System (Mini Project)

A simple, educational, and complete Python backend with an interactive modern HTML/CSS/JavaScript frontend.

---

## 📁 Project Structure (Matching Your Files)

```text
login_functionality/
│
├── app.py                # Main backend web server & API router (runs on http://localhost:5000)
├── login.py              # Login logic, password strength evaluator, and new user registration
├── database.py           # Simple data storage (users, colleges, marks, attendance) in JSON
├── platform_admin.py     # Platform Super Admin functions (view stats, manage users, add colleges)
├── college_adin.py       # College Admin alias (matching exact file name from screenshot)
├── college_admin.py      # College Admin functions (view faculty & students, add members)
├── teacher_admin.py      # Teacher portal functions (enter marks with auto-grades, attendance)
├── student_admin.py      # Student portal functions (view report card, attendance percentage)
│
└── static/               # Frontend (HTML, CSS, JavaScript)
    ├── index.html        # Clean tabbed interface for Login, Register, and Dashboards
    ├── style.css         # Modern dark glassmorphism styling and password strength bars
    └── script.js         # Interactive client logic, API calls, and real-time validation
```

---

## 🚀 How to Run the Project

1. Open your terminal or VS Code in this directory:
   ```bash
   cd "mini projects/login_functionality"
   ```
2. Start the backend application:
   ```bash
   python app.py
   ```
3. Open your browser and go to:
   **[http://localhost:5000](http://localhost:5000)**

---

## 🔑 Default Demo Accounts (Pre-configured)

You can also use the **⚡ Quick Fill** buttons on the login screen to sign in with one click:

| Role | Username | Password | Notes |
| :--- | :--- | :--- | :--- |
| **Platform Admin** | `admin` | `Admin@123` | System-wide statistics & user management |
| **College Admin** | `coep_admin` | `College@123` | Manage college faculty & student roster |
| **Teacher Admin** | `teacher1` | `Teacher@123` | Enter marks (auto-grading) & attendance |
| **Student Admin** | `student1` | `Student@123` | View academic report card & attendance |

---

## 🧠 Core Features & Simple Logic

### 1. Password Strength Checker (`login.py`)
- Evaluates password strength dynamically with a score (0 to 100):
  - **Length**: At least 8 characters (+25 points)
  - **Lowercase**: Contains `a-z` (+20 points)
  - **Uppercase**: Contains `A-Z` (+20 points)
  - **Number**: Contains `0-9` (+20 points)
  - **Special Character**: Contains symbols like `!@#$%` (+15 points)
- Visual color bar: **Weak** (Red) ➔ **Medium** (Amber) ➔ **Strong** (Green) ➔ **Very Strong** (Emerald).

### 2. Old Users Login
- Checks if username exists in the database.
- Matches password.
- Identifies user role and automatically opens their dedicated dashboard.

### 3. New Users Registration & Saves
- Validates password strength before saving.
- Checks that the username is not already taken.
- Saves the user immediately to `users_data.json` without requiring any external database configuration.

### 4. Role-Specific Dashboards
- **Platform Admin**: View platform-wide statistics, inspect registered users, and add new institutions.
- **College Admin**: View all faculty members and students belonging to their college.
- **Teacher**: Record marks (auto-calculates grades `A+`, `A`, `B`, `C`, `D`, `F`) and tracks class attendance.
- **Student**: View overall percentage, pass/fail status, and exam eligibility based on the 75% attendance rule.
