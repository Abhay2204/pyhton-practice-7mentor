"""
college_adin.py
Direct alias for college_admin.py to match exact file name from project screenshot.
"""

from college_admin import (
    get_college_members,
    add_teacher_for_college,
    add_student_for_college
)

__all__ = [
    "get_college_members",
    "add_teacher_for_college",
    "add_student_for_college"
]
