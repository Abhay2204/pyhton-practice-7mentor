/**
 * EduPortal Frontend Logic
 * Connects HTML/CSS UI with Python Backend API endpoints.
 */

// Current Session State
let currentUser = null;

// ================= INITIALIZATION =================
document.addEventListener("DOMContentLoaded", () => {
    // Check if user was previously logged in
    const savedUser = localStorage.getItem("eduportal_user");
    if (savedUser) {
        try {
            currentUser = JSON.parse(savedUser);
            renderAuthenticatedState();
        } catch (e) {
            localStorage.removeItem("eduportal_user");
        }
    }

    // Bind demo accounts modal toggle
    document.getElementById("demoAccountsBtn").addEventListener("click", openDemoModal);
    document.getElementById("logoutBtn").addEventListener("click", handleLogout);
});

// ================= AUTH TABS & UTILITIES =================
function switchAuthTab(tab) {
    const loginTab = document.getElementById("tabLogin");
    const regTab = document.getElementById("tabRegister");
    const loginContainer = document.getElementById("loginFormContainer");
    const regContainer = document.getElementById("registerFormContainer");

    if (tab === "login") {
        loginTab.classList.add("active");
        regTab.classList.remove("active");
        loginContainer.classList.add("active");
        regContainer.classList.remove("active");
    } else {
        regTab.classList.add("active");
        loginTab.classList.remove("active");
        regContainer.classList.add("active");
        loginContainer.classList.remove("active");
    }
}

function togglePasswordVisibility(inputId, btn) {
    const input = document.getElementById(inputId);
    if (input.type === "password") {
        input.type = "text";
        btn.textContent = "🙈";
    } else {
        input.type = "password";
        btn.textContent = "👁️";
    }
}

function handleRoleChange() {
    const role = document.getElementById("regRole").value;
    const studentFields = document.getElementById("studentExtraFields");
    if (role === "student_admin") {
        studentFields.style.display = "grid";
    } else {
        studentFields.style.display = "none";
    }
}

// ================= QUICK FILL DEMO ACCOUNTS =================
const DEMO_PRESETS = {
    admin: { u: "admin", p: "Admin@123" },
    coep_admin: { u: "coep_admin", p: "College@123" },
    teacher1: { u: "teacher1", p: "Teacher@123" },
    student1: { u: "student1", p: "Student@123" }
};

function quickFill(presetKey) {
    const preset = DEMO_PRESETS[presetKey];
    if (!preset) return;
    document.getElementById("loginUsername").value = preset.u;
    document.getElementById("loginPassword").value = preset.p;
    showToast(`Loaded ${preset.u} credentials`, "info");
}

function quickFillAndClose(presetKey) {
    switchAuthTab("login");
    quickFill(presetKey);
    closeDemoModal();
}

function openDemoModal() {
    document.getElementById("demoModal").classList.remove("hidden");
}

function closeDemoModal() {
    document.getElementById("demoModal").classList.add("hidden");
}

// ================= LIVE PASSWORD STRENGTH EVALUATOR =================
function evaluatePasswordStrength(password) {
    const meterBar = document.getElementById("meterBar");
    const badge = document.getElementById("strengthBadge");

    const critLength = document.getElementById("critLength");
    const critLower = document.getElementById("critLower");
    const critUpper = document.getElementById("critUpper");
    const critNumber = document.getElementById("critNumber");
    const critSpecial = document.getElementById("critSpecial");

    if (!password) {
        meterBar.style.width = "0%";
        badge.textContent = "Enter Password";
        badge.className = "strength-badge weak";
        [critLength, critLower, critUpper, critNumber, critSpecial].forEach(el => el.classList.remove("valid"));
        return;
    }

    // Evaluate rules locally for instantaneous UI feedback
    const hasLength = password.length >= 8;
    const hasLower = /[a-z]/.test(password);
    const hasUpper = /[A-Z]/.test(password);
    const hasNumber = /[0-9]/.test(password);
    const hasSpecial = /[!@#$%^&*()_\-=\+\[\]{}|;:,.<>?/~`]/.test(password);

    critLength.classList.toggle("valid", hasLength);
    critLower.classList.toggle("valid", hasLower);
    critUpper.classList.toggle("valid", hasUpper);
    critNumber.classList.toggle("valid", hasNumber);
    critSpecial.classList.toggle("valid", hasSpecial);

    let score = 0;
    if (hasLength) score += 25;
    if (hasLower) score += 20;
    if (hasUpper) score += 20;
    if (hasNumber) score += 20;
    if (hasSpecial) score += 15;

    meterBar.style.width = `${score}%`;

    if (score < 40) {
        badge.textContent = "Weak";
        badge.className = "strength-badge weak";
        meterBar.style.backgroundColor = "var(--danger)";
    } else if (score < 70) {
        badge.textContent = "Medium";
        badge.className = "strength-badge medium";
        meterBar.style.backgroundColor = "var(--warning)";
    } else {
        badge.textContent = score >= 90 ? "Very Strong" : "Strong";
        badge.className = "strength-badge strong";
        meterBar.style.backgroundColor = "var(--success)";
    }
}

// ================= AUTH API CALLS =================
async function handleLogin(e) {
    e.preventDefault();
    const submitBtn = document.getElementById("loginSubmitBtn");
    submitBtn.disabled = true;
    submitBtn.textContent = "Signing in...";

    const username = document.getElementById("loginUsername").value.trim();
    const password = document.getElementById("loginPassword").value;

    try {
        const res = await fetch("/api/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password })
        });
        const data = await res.json();

        if (data.success) {
            currentUser = data.user;
            localStorage.setItem("eduportal_user", JSON.stringify(currentUser));
            showToast(data.message, "success");
            renderAuthenticatedState();
        } else {
            showToast(data.message, "error");
        }
    } catch (err) {
        showToast("Server connection error: " + err.message, "error");
    } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = "Sign In to Portal";
    }
}

async function handleRegister(e) {
    e.preventDefault();
    const submitBtn = document.getElementById("registerSubmitBtn");
    submitBtn.disabled = true;
    submitBtn.textContent = "Registering & Saving...";

    const fullName = document.getElementById("regFullName").value.trim();
    const username = document.getElementById("regUsername").value.trim();
    const role = document.getElementById("regRole").value;
    const college = document.getElementById("regCollege").value;
    const email = document.getElementById("regEmail").value.trim();
    const password = document.getElementById("regPassword").value;

    const extra = {};
    if (role === "student_admin") {
        extra.roll_no = document.getElementById("regRollNo").value.trim() || "CS-NEW";
        extra.branch = document.getElementById("regBranch").value.trim() || "Computer Science";
    }

    try {
        const res = await fetch("/api/register", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                username,
                password,
                full_name: fullName,
                role,
                college,
                email,
                extra
            })
        });
        const data = await res.json();

        if (data.success) {
            showToast(data.message, "success");
            // Switch to login tab and pre-fill username
            switchAuthTab("login");
            document.getElementById("loginUsername").value = username;
            document.getElementById("loginPassword").value = "";
            document.getElementById("registerForm").reset();
            evaluatePasswordStrength("");
        } else {
            showToast(data.message, "error");
        }
    } catch (err) {
        showToast("Error: " + err.message, "error");
    } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = "Register & Save User";
    }
}

function handleLogout() {
    currentUser = null;
    localStorage.removeItem("eduportal_user");
    showToast("Logged out successfully", "info");

    document.getElementById("authSection").classList.remove("hidden");
    document.getElementById("dashboardSection").classList.add("hidden");
    document.getElementById("userHeaderBadge").classList.add("hidden");

    // Hide all role dashboards
    document.querySelectorAll(".role-dashboard").forEach(el => el.classList.add("hidden"));
}

// ================= RENDER LOGGED IN STATE =================
function renderAuthenticatedState() {
    if (!currentUser) return;

    // Switch view from Auth form to Dashboard
    document.getElementById("authSection").classList.add("hidden");
    document.getElementById("dashboardSection").classList.remove("hidden");

    // Header info
    const badge = document.getElementById("headerRoleBadge");
    const nameSpan = document.getElementById("headerUserName");
    document.getElementById("userHeaderBadge").classList.remove("hidden");

    nameSpan.textContent = currentUser.full_name;

    const roleMap = {
        platform_admin: { text: "Platform Admin", cls: "badge-platform" },
        college_admin: { text: "College Admin", cls: "badge-college" },
        teacher_admin: { text: "Faculty", cls: "badge-teacher" },
        student_admin: { text: "Student", cls: "badge-student" }
    };

    const roleInfo = roleMap[currentUser.role] || { text: currentUser.role, cls: "badge-student" };
    badge.textContent = roleInfo.text;
    badge.className = `badge ${roleInfo.cls}`;

    // Hide all dashboards first
    document.querySelectorAll(".role-dashboard").forEach(el => el.classList.add("hidden"));

    // Activate specific dashboard
    if (currentUser.role === "platform_admin") {
        document.getElementById("platformAdminDashboard").classList.remove("hidden");
        fetchPlatformStats();
        fetchPlatformUsers();
    } else if (currentUser.role === "college_admin") {
        document.getElementById("collegeAdminDashboard").classList.remove("hidden");
        document.getElementById("collegeAdminSubtitle").textContent = `Managing ${currentUser.college}`;
        fetchCollegeMembers();
    } else if (currentUser.role === "teacher_admin") {
        document.getElementById("teacherDashboard").classList.remove("hidden");
        document.getElementById("teacherSubtitle").textContent = `Faculty: ${currentUser.full_name} | ${currentUser.college}`;
        fetchTeacherData();
    } else if (currentUser.role === "student_admin") {
        document.getElementById("studentDashboard").classList.remove("hidden");
        document.getElementById("studentSubtitle").textContent = `Student: ${currentUser.full_name} | Roll: ${currentUser.roll_no || 'N/A'} | ${currentUser.college}`;
        fetchStudentData();
    }
}

// ================= PLATFORM ADMIN ACTIONS =================
async function fetchPlatformStats() {
    try {
        const res = await fetch("/api/platform-stats");
        const data = await res.json();
        document.getElementById("statTotalUsers").textContent = data.total_users;
        document.getElementById("statTotalColleges").textContent = data.total_colleges;
        document.getElementById("statTotalTeachers").textContent = data.role_counts.teacher_admin || 0;
        document.getElementById("statTotalStudents").textContent = data.role_counts.student_admin || 0;
    } catch (e) {
        console.error(e);
    }
}

async function fetchPlatformUsers() {
    const tbody = document.getElementById("platformUsersTableBody");
    try {
        const res = await fetch("/api/all-users");
        const data = await res.json();
        const users = data.users || [];

        if (users.length === 0) {
            tbody.innerHTML = `<tr><td colspan="5" style="text-align:center;">No users registered yet.</td></tr>`;
            return;
        }

        const roleBadges = {
            platform_admin: `<span class="badge badge-platform">Platform Admin</span>`,
            college_admin: `<span class="badge badge-college">College Admin</span>`,
            teacher_admin: `<span class="badge badge-teacher">Faculty</span>`,
            student_admin: `<span class="badge badge-student">Student</span>`
        };

        tbody.innerHTML = users.map(u => `
            <tr>
                <td><strong>${escapeHtml(u.username)}</strong></td>
                <td>${escapeHtml(u.full_name)}</td>
                <td>${roleBadges[u.role] || u.role}</td>
                <td>${escapeHtml(u.college || 'N/A')}</td>
                <td>
                    ${u.username !== 'admin' ? `
                        <button class="btn btn-danger btn-sm" onclick="handleRemoveUser('${u.username}')">Delete</button>
                    ` : `<span style="color:var(--text-muted);font-size:0.8rem;">Super Admin</span>`}
                </td>
            </tr>
        `).join("");
    } catch (e) {
        tbody.innerHTML = `<tr><td colspan="5" style="color:var(--danger);text-align:center;">Failed to load users.</td></tr>`;
    }
}

async function handleAddCollege(e) {
    e.preventDefault();
    const name = document.getElementById("newColName").value;
    const code = document.getElementById("newColCode").value;
    const city = document.getElementById("newColCity").value;

    try {
        const res = await fetch("/api/add-college", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name, code, city })
        });
        const data = await res.json();
        if (data.success) {
            showToast(data.message, "success");
            document.getElementById("addCollegeForm").reset();
            fetchPlatformStats();
        } else {
            showToast(data.message, "error");
        }
    } catch (e) {
        showToast("Error adding college: " + e.message, "error");
    }
}

async function handleRemoveUser(username) {
    if (!confirm(`Are you sure you want to remove user '${username}'?`)) return;

    try {
        const res = await fetch("/api/remove-user", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username })
        });
        const data = await res.json();
        if (data.success) {
            showToast(data.message, "success");
            fetchPlatformStats();
            fetchPlatformUsers();
        } else {
            showToast(data.message, "error");
        }
    } catch (e) {
        showToast("Error deleting user: " + e.message, "error");
    }
}

// ================= COLLEGE ADMIN ACTIONS =================
async function fetchCollegeMembers() {
    const college = currentUser.college;
    try {
        const res = await fetch(`/api/college-members?college=${encodeURIComponent(college)}`);
        const data = await res.json();

        document.getElementById("collegeTeacherCount").textContent = data.total_teachers;
        document.getElementById("collegeStudentCount").textContent = data.total_students;

        // Teachers Table
        const tBody = document.getElementById("collegeTeachersTableBody");
        if (data.teachers.length === 0) {
            tBody.innerHTML = `<tr><td colspan="3" style="text-align:center;">No teachers registered yet.</td></tr>`;
        } else {
            tBody.innerHTML = data.teachers.map(t => `
                <tr>
                    <td><strong>${escapeHtml(t.full_name)}</strong></td>
                    <td><code>${escapeHtml(t.username)}</code></td>
                    <td>${escapeHtml(t.department || 'General')}</td>
                </tr>
            `).join("");
        }

        // Students Table
        const sBody = document.getElementById("collegeStudentsTableBody");
        if (data.students.length === 0) {
            sBody.innerHTML = `<tr><td colspan="3" style="text-align:center;">No students enrolled yet.</td></tr>`;
        } else {
            sBody.innerHTML = data.students.map(s => `
                <tr>
                    <td><code>${escapeHtml(s.roll_no || 'N/A')}</code></td>
                    <td><strong>${escapeHtml(s.full_name)}</strong></td>
                    <td>${escapeHtml(s.branch || 'Engineering')}</td>
                </tr>
            `).join("");
        }
    } catch (e) {
        console.error(e);
    }
}

// ================= TEACHER ACTIONS =================
async function fetchTeacherData() {
    const college = currentUser.college;
    try {
        // 1. Fetch Students to populate dropdowns
        const sRes = await fetch(`/api/teacher-students?college=${encodeURIComponent(college)}`);
        const sData = await sRes.json();
        const students = sData.students || [];

        const marksSelect = document.getElementById("marksStudentSelect");
        const attSelect = document.getElementById("attStudentSelect");

        if (students.length === 0) {
            marksSelect.innerHTML = `<option value="">No students enrolled in college</option>`;
            attSelect.innerHTML = `<option value="">No students enrolled in college</option>`;
        } else {
            const options = students.map(s => `
                <option value="${s.username}">${escapeHtml(s.full_name)} (${s.roll_no})</option>
            `).join("");
            marksSelect.innerHTML = options;
            attSelect.innerHTML = options;
        }

        // 2. Fetch Records Table
        const rRes = await fetch(`/api/teacher-records?college=${encodeURIComponent(college)}`);
        const rData = await rRes.json();
        const marks = rData.marks || [];
        const att = rData.attendance || [];

        const tbody = document.getElementById("teacherRecordsTableBody");
        if (marks.length === 0) {
            tbody.innerHTML = `<tr><td colspan="6" style="text-align:center;">No records entered yet.</td></tr>`;
            return;
        }

        tbody.innerHTML = marks.map(m => {
            // Find corresponding attendance if available
            const matchAtt = att.find(a => a.student_username === m.student_username && a.subject.toLowerCase() === m.subject.toLowerCase());
            const attDisplay = matchAtt ? `${matchAtt.attended_classes}/${matchAtt.total_classes}` : "-";
            const attPct = matchAtt ? ((matchAtt.attended_classes / matchAtt.total_classes) * 100).toFixed(1) + "%" : "-";

            let gradeClass = "grade-a";
            if (m.grade.startsWith("B")) gradeClass = "grade-b";
            else if (m.grade.startsWith("C") || m.grade.startsWith("D")) gradeClass = "grade-c";
            else if (m.grade === "F") gradeClass = "grade-f";

            return `
                <tr>
                    <td><strong>${escapeHtml(m.student_username)}</strong></td>
                    <td>${escapeHtml(m.subject)}</td>
                    <td>${m.marks} / ${m.max_marks}</td>
                    <td><span class="grade-pill ${gradeClass}">${m.grade}</span></td>
                    <td>${attDisplay}</td>
                    <td>${attPct}</td>
                </tr>
            `;
        }).join("");

    } catch (e) {
        console.error(e);
    }
}

async function handleEnterMarks(e) {
    e.preventDefault();
    const student_username = document.getElementById("marksStudentSelect").value;
    const subject = document.getElementById("marksSubject").value.trim();
    const marks = document.getElementById("marksObtained").value;
    const max_marks = document.getElementById("marksMax").value;

    if (!student_username) {
        showToast("Please select a student first", "warning");
        return;
    }

    try {
        const res = await fetch("/api/add-mark", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ student_username, subject, marks, max_marks })
        });
        const data = await res.json();
        if (data.success) {
            showToast(data.message, "success");
            fetchTeacherData();
        } else {
            showToast(data.message, "error");
        }
    } catch (e) {
        showToast("Error saving marks: " + e.message, "error");
    }
}

async function handleEnterAttendance(e) {
    e.preventDefault();
    const student_username = document.getElementById("attStudentSelect").value;
    const subject = document.getElementById("attSubject").value.trim();
    const total_classes = document.getElementById("attTotal").value;
    const attended_classes = document.getElementById("attAttended").value;

    if (!student_username) {
        showToast("Please select a student first", "warning");
        return;
    }

    try {
        const res = await fetch("/api/add-attendance", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ student_username, subject, total_classes, attended_classes })
        });
        const data = await res.json();
        if (data.success) {
            showToast(data.message, "success");
            fetchTeacherData();
        } else {
            showToast(data.message, "error");
        }
    } catch (e) {
        showToast("Error saving attendance: " + e.message, "error");
    }
}

// ================= STUDENT ACTIONS =================
async function fetchStudentData() {
    const username = currentUser.username;
    try {
        // 1. Report Card
        const mRes = await fetch(`/api/student-report?username=${encodeURIComponent(username)}`);
        const mData = await mRes.json();

        const reportTbody = document.getElementById("studentReportTableBody");
        if (mData.marks && mData.marks.length > 0) {
            reportTbody.innerHTML = mData.marks.map(m => {
                let gradeClass = "grade-a";
                if (m.grade.startsWith("B")) gradeClass = "grade-b";
                else if (m.grade.startsWith("C") || m.grade.startsWith("D")) gradeClass = "grade-c";
                else if (m.grade === "F") gradeClass = "grade-f";

                return `
                    <tr>
                        <td><strong>${escapeHtml(m.subject)}</strong></td>
                        <td>${m.marks}</td>
                        <td>${m.max_marks}</td>
                        <td><span class="grade-pill ${gradeClass}">${m.grade}</span></td>
                    </tr>
                `;
            }).join("");

            document.getElementById("studentOverallPercentage").textContent = `${mData.percentage}%`;
            document.getElementById("studentExamStatus").textContent = mData.status;
            document.getElementById("studentExamStatus").style.color = mData.percentage >= 40 ? "var(--success)" : "var(--danger)";
        } else {
            reportTbody.innerHTML = `<tr><td colspan="4" style="text-align:center;">No marks published yet.</td></tr>`;
            document.getElementById("studentOverallPercentage").textContent = "N/A";
            document.getElementById("studentExamStatus").textContent = "Pending";
        }

        // 2. Attendance Summary
        const aRes = await fetch(`/api/student-attendance?username=${encodeURIComponent(username)}`);
        const aData = await aRes.json();

        const attTbody = document.getElementById("studentAttendanceTableBody");
        if (aData.attendance && aData.attendance.length > 0) {
            attTbody.innerHTML = aData.attendance.map(a => {
                const pct = ((a.attended_classes / a.total_classes) * 100).toFixed(1);
                const isEligible = pct >= 75;
                return `
                    <tr>
                        <td><strong>${escapeHtml(a.subject)}</strong></td>
                        <td>${a.attended_classes}</td>
                        <td>${a.total_classes}</td>
                        <td style="color:${isEligible ? 'var(--success)' : 'var(--danger)'};font-weight:700;">
                            ${pct}% ${isEligible ? '✓' : '⚠️'}
                        </td>
                    </tr>
                `;
            }).join("");

            document.getElementById("studentAttendancePercentage").textContent = `${aData.overall_percentage}%`;
            document.getElementById("studentEligibilityStatus").textContent = aData.is_eligible ? "Eligible (≥ 75%)" : "At Risk (< 75%)";
            document.getElementById("studentEligibilityStatus").style.color = aData.is_eligible ? "var(--success)" : "var(--danger)";
        } else {
            attTbody.innerHTML = `<tr><td colspan="4" style="text-align:center;">No attendance records found.</td></tr>`;
            document.getElementById("studentAttendancePercentage").textContent = "N/A";
            document.getElementById("studentEligibilityStatus").textContent = "Pending";
        }

    } catch (e) {
        console.error(e);
    }
}

// ================= TOAST NOTIFICATION UTILITY =================
function showToast(message, type = "info") {
    const container = document.getElementById("toastContainer");
    const toast = document.createElement("div");
    toast.className = `toast ${type}`;
    toast.textContent = message;

    container.appendChild(toast);
    setTimeout(() => {
        toast.style.opacity = "0";
        setTimeout(() => toast.remove(), 300);
    }, 3500);
}

function escapeHtml(text) {
    if (!text) return "";
    return text.toString()
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}
