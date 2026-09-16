/**
 * script.js — CampusOS Modern Multi-Role Portal
 * Connects the dynamic animated frontend to the Python backend APIs
 */

// ── Session state ─────────────────────────────────────────
let currentUser = null;

// ── Boot ──────────────────────────────────────────────────
document.addEventListener("DOMContentLoaded", () => {
    const saved = localStorage.getItem("campusos_user");
    if (saved) {
        try {
            currentUser = JSON.parse(saved);
            renderDashboard();
        } catch (_) {
            localStorage.removeItem("campusos_user");
        }
    }
});

// ──────────────────────────────────────────────────────────
// AUTH TABS
// ──────────────────────────────────────────────────────────
function switchTab(tab) {
    const toLogin = tab === "login";
    document.getElementById("tabLoginBtn").classList.toggle("active", toLogin);
    document.getElementById("tabRegisterBtn").classList.toggle("active", !toLogin);
    document.getElementById("loginForm").classList.toggle("hidden", !toLogin);
    document.getElementById("registerForm").classList.toggle("hidden", toLogin);
    document.getElementById("loginAlert").classList.add("hidden");
}

// ──────────────────────────────────────────────────────────
// QUICK FILL — demo credentials with animated feedback
// ──────────────────────────────────────────────────────────
function quickFill(username, password, role) {
    switchTab("login");
    const uInput = document.getElementById("loginUsername");
    const pInput = document.getElementById("loginPassword");
    const rInput = document.getElementById("loginRoleHint");

    uInput.value = username;
    pInput.value = password;
    rInput.value = role;

    // Subtle flash highlight
    [uInput, pInput, rInput].forEach(el => {
        el.parentElement.style.borderColor = "var(--primary-indigo)";
        setTimeout(() => {
            el.parentElement.style.borderColor = "";
        }, 600);
    });

    toast(`Autofilled credentials for: ${username}`, "ok");
}

// ──────────────────────────────────────────────────────────
// TOGGLE PASSWORD VISIBILITY
// ──────────────────────────────────────────────────────────
function togglePwd(id, btn) {
    const el = document.getElementById(id);
    const show = el.type === "password";
    el.type = show ? "text" : "password";
    btn.innerHTML = show
        ? `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17.94 17.94A10.07 10.07 0 0112 20c-7 0-11-8-11-8a18.45 18.45 0 015.06-5.94M9.9 4.24A9.12 9.12 0 0112 4c7 0 11 8 11 8a18.5 18.5 0 01-2.16 3.19m-6.72-1.07a3 3 0 11-4.24-4.24"/><line x1="1" y1="1" x2="23" y2="23"/></svg>`
        : `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>`;
}

// ──────────────────────────────────────────────────────────
// LIVE PASSWORD STRENGTH
// ──────────────────────────────────────────────────────────
function liveStrength(pw) {
    const checks = {
        len:    pw.length >= 8,
        low:    /[a-z]/.test(pw),
        up:     /[A-Z]/.test(pw),
        num:    /[0-9]/.test(pw),
        sym:    /[!@#$%^&*()\-_=+\[\]{}|;:,.<>?/~`]/.test(pw)
    };

    Object.keys(checks).forEach(key => {
        document.getElementById(`c-${key}`)?.classList.toggle("valid", checks[key]);
    });

    let score = Object.values(checks).filter(Boolean).length;
    const fill = document.getElementById("strengthBar");
    const label = document.getElementById("strengthLabel");

    const levels = ["Strength: —", "Strength: Very Weak", "Strength: Weak", "Strength: Moderate", "Strength: Strong", "Strength: Very Strong"];
    const colors = ["#e2e8f0", "#ef4444", "#f97316", "#f59e0b", "#10b981", "#059669"];
    const widths = ["0%", "20%", "40%", "60%", "80%", "100%"];

    fill.style.width = widths[score];
    fill.style.backgroundColor = colors[score];
    label.textContent = levels[score];
    label.style.color = score > 0 ? colors[score] : "var(--text-muted)";
}

// Role toggle for register form
function handleRoleToggle() {
    const role = document.getElementById("regRole").value;
    const sf   = document.getElementById("studentFields");
    sf.style.display = role === "student_admin" ? "grid" : "none";
}

// ──────────────────────────────────────────────────────────
// LOGIN
// ──────────────────────────────────────────────────────────
async function handleLogin(e) {
    e.preventDefault();
    const btn = document.getElementById("loginBtn");
    btn.disabled = true;
    btn.innerHTML = `<span>Authenticating…</span>`;

    const username  = document.getElementById("loginUsername").value.trim();
    const password  = document.getElementById("loginPassword").value;
    const roleHint  = document.getElementById("loginRoleHint").value;

    try {
        const res  = await fetch("/api/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password })
        });
        const data = await res.json();

        if (data.success) {
            // Validate role hint match if user explicitly picked one
            if (roleHint && roleHint !== data.user.role) {
                setLoginAlert("The name, password, or dashboard role does not match our records.");
                btn.disabled = false;
                btn.innerHTML = `<span>Enter Workspace</span> <span class="btn-arrow-icon">→</span>`;
                return;
            }
            currentUser = data.user;
            localStorage.setItem("campusos_user", JSON.stringify(currentUser));
            setLoginAlert("", false);
            toast(`Welcome back, ${currentUser.full_name}!`, "ok");
            renderDashboard();
        } else {
            setLoginAlert(data.message);
        }
    } catch (err) {
        setLoginAlert("Cannot reach server. Is app.py running?");
    } finally {
        btn.disabled = false;
        btn.innerHTML = `<span>Enter Workspace</span> <span class="btn-arrow-icon">→</span>`;
    }
}

function setLoginAlert(msg, isError = true) {
    const el = document.getElementById("loginAlert");
    if (!msg) { el.classList.add("hidden"); return; }
    el.textContent = msg;
    el.className   = `alert${isError ? "" : " success-alert"}`;
    el.classList.remove("hidden");
}

// ──────────────────────────────────────────────────────────
// REGISTER
// ──────────────────────────────────────────────────────────
async function handleRegister(e) {
    e.preventDefault();
    const btn = e.submitter;
    btn.disabled = true;
    btn.innerHTML = `<span>Creating Account…</span>`;

    const payload = {
        username:  document.getElementById("regUsername").value.trim(),
        password:  document.getElementById("regPassword").value,
        full_name: document.getElementById("regFullName").value.trim(),
        email:     document.getElementById("regEmail").value.trim(),
        role:      document.getElementById("regRole").value,
        college:   document.getElementById("regCollege").value,
        extra: {
            roll_no: document.getElementById("regRollNo").value.trim() || "CS-NEW",
            branch:  document.getElementById("regBranch").value.trim() || "Engineering"
        }
    };

    try {
        const res  = await fetch("/api/register", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });
        const data = await res.json();

        if (data.success) {
            toast(data.message, "ok");
            switchTab("login");
            document.getElementById("loginUsername").value = payload.username;
            e.target.reset();
            liveStrength("");
        } else {
            toast(data.message, "err");
        }
    } catch (err) {
        toast("Server error: " + err.message, "err");
    } finally {
        btn.disabled = false;
        btn.innerHTML = `<span>Create User Account</span> <span class="btn-arrow-icon">→</span>`;
    }
}

// ──────────────────────────────────────────────────────────
// LOGOUT
// ──────────────────────────────────────────────────────────
function handleLogout() {
    currentUser = null;
    localStorage.removeItem("campusos_user");
    document.getElementById("dashboardPage").classList.add("hidden");
    document.getElementById("loginPage").classList.remove("hidden");
    document.getElementById("loginForm").reset();
    setLoginAlert("");
    toast("Signed out successfully.", "warn");
}

// ──────────────────────────────────────────────────────────
// RENDER DASHBOARD
// ──────────────────────────────────────────────────────────
function renderDashboard() {
    document.getElementById("loginPage").classList.add("hidden");
    document.getElementById("dashboardPage").classList.remove("hidden");

    // Nav bar data
    document.getElementById("navUserName").textContent = currentUser.full_name;
    document.getElementById("navCollegeName").textContent = currentUser.college || "Global HQ";

    const initialEl = document.getElementById("userAvatarInitial");
    if (initialEl) {
        initialEl.textContent = (currentUser.full_name || "U")[0].toUpperCase();
    }

    const roleLabels = {
        platform_admin: "Platform Administrator",
        college_admin:  "College Administrator",
        teacher_admin:  "Faculty / Educator",
        student_admin:  "Enrolled Student"
    };
    document.getElementById("navRolePill").textContent = roleLabels[currentUser.role] || currentUser.role;

    // Hide all role views
    document.querySelectorAll(".role-view").forEach(v => v.classList.add("hidden"));

    // Route to the appropriate view
    if (currentUser.role === "platform_admin") {
        document.getElementById("dash-platform").classList.remove("hidden");
        fetchPlatformStats();
        fetchPlatformUsers();

    } else if (currentUser.role === "college_admin") {
        document.getElementById("dash-college").classList.remove("hidden");
        document.getElementById("collegeTitle").textContent = `${currentUser.college} — Portal`;
        document.getElementById("cbName").textContent = currentUser.college;
        document.getElementById("cbCode").textContent = currentUser.college_code || "COEP01";
        fetchCollegeMembers();

    } else if (currentUser.role === "teacher_admin") {
        document.getElementById("dash-teacher").classList.remove("hidden");
        document.getElementById("teacherTitle").textContent = `${currentUser.full_name} (${currentUser.college})`;
        fetchTeacherData();

    } else if (currentUser.role === "student_admin") {
        document.getElementById("dash-student").classList.remove("hidden");
        document.getElementById("studentTitle").textContent =
            `${currentUser.full_name}${currentUser.roll_no ? " · " + currentUser.roll_no : ""}`;
        fetchStudentData();
    }
}

// ──────────────────────────────────────────────────────────
// PLATFORM ADMIN
// ──────────────────────────────────────────────────────────
async function fetchPlatformStats() {
    try {
        const data = await get("/api/platform-stats");
        document.getElementById("pTotalUsers").textContent     = data.total_users;
        document.getElementById("pTotalColleges").textContent  = data.total_colleges;
        document.getElementById("pTotalTeachers").textContent  = data.role_counts.teacher_admin || 0;
        document.getElementById("pTotalStudents").textContent  = data.role_counts.student_admin || 0;
    } catch (_) {}
}

async function fetchPlatformUsers() {
    const tbody = document.getElementById("pUsersBody");
    try {
        const data  = await get("/api/all-users");
        const users = data.users || [];

        document.getElementById("pUserCount").textContent = `${users.length} records`;

        if (!users.length) {
            tbody.innerHTML = `<tr><td colspan="6" class="empty-cell">No users registered in system.</td></tr>`;
            return;
        }

        const roleTags = {
            platform_admin: `<span class="role-tag rt-platform">Platform Admin</span>`,
            college_admin:  `<span class="role-tag rt-college">College Admin</span>`,
            teacher_admin:  `<span class="role-tag rt-teacher">Teacher</span>`,
            student_admin:  `<span class="role-tag rt-student">Student</span>`
        };

        tbody.innerHTML = users.map((u, i) => `
            <tr>
                <td class="mono-tag" style="color:var(--text-muted)">${String(i+1).padStart(2,'0')}</td>
                <td><strong style="color:#fff">${h(u.username)}</strong></td>
                <td>${h(u.full_name)}</td>
                <td>${roleTags[u.role] || u.role}</td>
                <td><span style="color:var(--text-secondary)">${h(u.college || "—")}</span></td>
                <td>${u.username !== "admin"
                    ? `<button class="btn-remove" onclick="removeUser('${h(u.username)}')">Remove</button>`
                    : `<span style="color:var(--text-muted);font-size:0.68rem;font-family:var(--font-mono)">ROOT PROTECTED</span>`}
                </td>
            </tr>
        `).join("");
    } catch (_) {
        tbody.innerHTML = `<tr><td colspan="6" class="empty-cell">Failed to fetch database users.</td></tr>`;
    }
}

async function handleAddCollege(e) {
    e.preventDefault();
    const res  = await post("/api/add-college", {
        name: document.getElementById("colName").value,
        code: document.getElementById("colCode").value,
        city: document.getElementById("colCity").value
    });
    if (res.success) {
        toast(res.message, "ok");
        e.target.reset();
        fetchPlatformStats();
    } else {
        toast(res.message, "err");
    }
}

async function removeUser(username) {
    if (!confirm(`Are you sure you want to revoke access for "${username}"?`)) return;
    const res = await post("/api/remove-user", { username });
    if (res.success) { 
        toast(res.message, "ok"); 
        fetchPlatformStats(); 
        fetchPlatformUsers(); 
    } else { 
        toast(res.message, "err"); 
    }
}

// ──────────────────────────────────────────────────────────
// COLLEGE ADMIN
// ──────────────────────────────────────────────────────────
async function fetchCollegeMembers() {
    try {
        const data     = await get(`/api/college-members?college=${enc(currentUser.college)}`);
        const teachers = data.teachers || [];
        const students = data.students || [];

        document.getElementById("collegeRecordCount").textContent =
            `${teachers.length + students.length} members`;

        // Teachers list
        const tl = document.getElementById("teachersList");
        document.getElementById("teacherCount").textContent = teachers.length;
        if (!teachers.length) {
            tl.innerHTML = `<p class="empty-note">No teachers assigned to this campus yet.</p>`;
        } else {
            tl.innerHTML = teachers.map(t => `
                <div class="person-row">
                    <div>
                        <strong style="color:#fff">${h(t.full_name)}</strong>
                        <div style="color:var(--text-muted);font-size:0.75rem">${h(t.department || "Faculty")} • ${h(t.email || "No email")}</div>
                    </div>
                    <span class="cred-chip user-chip">@${h(t.username)}</span>
                </div>
            `).join("");
        }

        // Students list
        const sl = document.getElementById("studentsList");
        document.getElementById("studentCount").textContent = students.length;
        if (!students.length) {
            sl.innerHTML = `<p class="empty-note">No students enrolled yet.</p>`;
        } else {
            sl.innerHTML = students.map(s => `
                <div class="person-row">
                    <div>
                        <strong style="color:#fff">${h(s.full_name)}</strong>
                        <div style="color:var(--text-muted);font-size:0.75rem">${h(s.branch || "General Engineering")}</div>
                    </div>
                    <span class="cred-chip pass-chip">${h(s.roll_no || "N/A")}</span>
                </div>
            `).join("");
        }
    } catch (_) {}
}

async function handleAddTeacher(e) {
    e.preventDefault();
    const res = await post("/api/college-add-teacher", {
        college:    currentUser.college,
        username:   document.getElementById("tUsername").value.trim(),
        password:   document.getElementById("tPassword").value,
        full_name:  document.getElementById("tFullName").value.trim(),
        department: document.getElementById("tDept").value.trim(),
        email:      document.getElementById("tEmail").value.trim()
    });
    if (res.success) { toast(res.message, "ok"); e.target.reset(); fetchCollegeMembers(); }
    else             { toast(res.message, "err"); }
}

async function handleAddStudent(e) {
    e.preventDefault();
    const res = await post("/api/college-add-student", {
        college:   currentUser.college,
        username:  document.getElementById("sUsername").value.trim(),
        password:  document.getElementById("sPassword").value,
        full_name: document.getElementById("sFullName").value.trim(),
        roll_no:   document.getElementById("sRollNo").value.trim(),
        branch:    document.getElementById("sBranch").value.trim(),
        email:     ""
    });
    if (res.success) { toast(res.message, "ok"); e.target.reset(); fetchCollegeMembers(); }
    else             { toast(res.message, "err"); }
}

// ──────────────────────────────────────────────────────────
// TEACHER
// ──────────────────────────────────────────────────────────
async function fetchTeacherData() {
    const college = currentUser.college;
    try {
        const sData    = await get(`/api/teacher-students?college=${enc(college)}`);
        const students = sData.students || [];

        const opts = students.length
            ? students.map(s => `<option value="${h(s.username)}">${h(s.full_name)} (${h(s.roll_no || s.username)})</option>`).join("")
            : `<option value="">No enrolled students in this campus</option>`;

        document.getElementById("marksStudentSel").innerHTML = opts;
        document.getElementById("attStudentSel").innerHTML   = opts;

        // Class records table
        const rData = await get(`/api/teacher-records?college=${enc(college)}`);
        const marks = rData.marks || [];
        const att   = rData.attendance || [];
        const tbody = document.getElementById("teacherRecordsBody");

        if (!marks.length) {
            tbody.innerHTML = `<tr><td colspan="6" class="empty-cell">No academic records entered yet.</td></tr>`;
            return;
        }

        tbody.innerHTML = marks.map(m => {
            const attRec = att.find(a =>
                a.student_username === m.student_username &&
                a.subject.toLowerCase() === m.subject.toLowerCase()
            );
            const attDisplay = attRec ? `${attRec.attended_classes} / ${attRec.total_classes}` : "—";
            const pct        = attRec ? (attRec.attended_classes / attRec.total_classes * 100).toFixed(0) + "%" : "—";
            const pctClass   = attRec ? (attRec.attended_classes / attRec.total_classes >= 0.75 ? "att-ok" : "att-warn") : "";
            const gradeCls   = gradeClass(m.grade);

            return `<tr>
                <td><strong style="color:#fff">${h(m.student_username)}</strong></td>
                <td>${h(m.subject)}</td>
                <td><span style="font-family:var(--font-mono)">${m.marks} / ${m.max_marks}</span></td>
                <td><span class="grade ${gradeCls}">${m.grade}</span></td>
                <td><span style="font-family:var(--font-mono)">${attDisplay}</span></td>
                <td class="${pctClass}">${pct}</td>
            </tr>`;
        }).join("");
    } catch (err) { console.error(err); }
}

async function handleEnterMarks(e) {
    e.preventDefault();
    const student_username = document.getElementById("marksStudentSel").value;
    if (!student_username) { toast("Select a student first", "warn"); return; }

    const res = await post("/api/add-mark", {
        student_username,
        subject:    document.getElementById("marksSubject").value.trim(),
        marks:      document.getElementById("marksObtained").value,
        max_marks:  document.getElementById("marksMax").value
    });
    if (res.success) { toast(res.message, "ok"); fetchTeacherData(); }
    else             { toast(res.message, "err"); }
}

async function handleEnterAttendance(e) {
    e.preventDefault();
    const student_username = document.getElementById("attStudentSel").value;
    if (!student_username) { toast("Select a student first", "warn"); return; }

    const res = await post("/api/add-attendance", {
        student_username,
        subject:          document.getElementById("attSubject").value.trim(),
        total_classes:    document.getElementById("attTotal").value,
        attended_classes: document.getElementById("attAttended").value
    });
    if (res.success) { toast(res.message, "ok"); fetchTeacherData(); }
    else             { toast(res.message, "err"); }
}

// ──────────────────────────────────────────────────────────
// STUDENT
// ──────────────────────────────────────────────────────────
async function fetchStudentData() {
    const un = currentUser.username;
    try {
        // Marks / report card
        const mData = await get(`/api/student-report?username=${enc(un)}`);
        document.getElementById("sPct").textContent    = mData.percentage != null ? mData.percentage + "%" : "—";
        document.getElementById("sStatus").textContent = mData.status || "—";
        document.getElementById("sStatus").style.color = mData.percentage >= 40 ? "var(--accent-emerald)" : "var(--accent-rose)";

        const rBody = document.getElementById("sReportBody");
        if (mData.marks && mData.marks.length) {
            rBody.innerHTML = mData.marks.map(m => `
                <tr>
                    <td><strong style="color:#fff">${h(m.subject)}</strong></td>
                    <td><span style="font-family:var(--font-mono)">${m.marks}</span></td>
                    <td><span style="font-family:var(--font-mono)">${m.max_marks}</span></td>
                    <td><span class="grade ${gradeClass(m.grade)}">${m.grade}</span></td>
                </tr>
            `).join("");
        } else {
            rBody.innerHTML = `<tr><td colspan="4" class="empty-cell">No official marks published yet.</td></tr>`;
        }

        // Attendance
        const aData = await get(`/api/student-attendance?username=${enc(un)}`);
        document.getElementById("sAttPct").textContent    = aData.overall_percentage != null ? aData.overall_percentage + "%" : "—";
        document.getElementById("sEligible").textContent  = aData.status || "—";
        document.getElementById("sEligible").style.color  = aData.is_eligible ? "var(--accent-emerald)" : "var(--accent-rose)";

        const aBody = document.getElementById("sAttBody");
        if (aData.attendance && aData.attendance.length) {
            aBody.innerHTML = aData.attendance.map(a => {
                const pct = a.total_classes > 0 ? (a.attended_classes / a.total_classes * 100).toFixed(1) : 0;
                const cls = pct >= 75 ? "att-ok" : "att-warn";
                return `<tr>
                    <td><strong style="color:#fff">${h(a.subject)}</strong></td>
                    <td><span style="font-family:var(--font-mono)">${a.attended_classes}</span></td>
                    <td><span style="font-family:var(--font-mono)">${a.total_classes}</span></td>
                    <td class="${cls}">${pct}% ${pct >= 75 ? "✓ Eligible" : "⚠ Defaulter"}</td>
                </tr>`;
            }).join("");
        } else {
            aBody.innerHTML = `<tr><td colspan="4" class="empty-cell">No attendance recorded yet.</td></tr>`;
        }
    } catch (err) { console.error(err); }
}

// ──────────────────────────────────────────────────────────
// SHARED HELPERS
// ──────────────────────────────────────────────────────────
async function get(url) {
    const r = await fetch(url);
    return r.json();
}

async function post(url, body) {
    const r = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body)
    });
    return r.json();
}

function h(str) {
    if (!str) return "";
    return String(str)
        .replace(/&/g, "&amp;").replace(/</g, "&lt;")
        .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}

function enc(s) { return encodeURIComponent(s || ""); }

function gradeClass(grade) {
    if (!grade) return "";
    const g = grade.toUpperCase();
    if (g.startsWith("A")) return "grade-a";
    if (g.startsWith("B")) return "grade-b";
    if (g === "F")         return "grade-f";
    return "grade-c";
}

function toast(msg, type = "info") {
    const box = document.getElementById("toastBox");
    const el  = document.createElement("div");
    el.className = `toast ${type}`;
    el.innerHTML = `<span>${h(msg)}</span>`;
    box.appendChild(el);
    setTimeout(() => {
        el.style.opacity = "0";
        el.style.transform = "translateY(10px) scale(0.95)";
        el.style.transition = "all 0.3s ease";
        setTimeout(() => el.remove(), 300);
    }, 3200);
}
