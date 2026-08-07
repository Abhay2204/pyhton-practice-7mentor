# Question:
# Create a record for 'Rubi Hospital' containing 4 patients with Indian names:
# fields: patient_name, dr_name, room_no, disease.
# Then arrange:
# - patient_name in ascending order
# - dr_name in descending order
# - room_no in ascending order
# - disease in descending order

rubi_hospital = {
    "patient_name": ["Rahul", "Ananya", "Amit", "Priya"],
    "dr_name": ["Dr. Sharma", "Dr. Kulkarni", "Dr. Gupta", "Dr. Patil"],
    "room_no": [104, 101, 203, 102],
    "disease": ["Fever", "Diabetes", "Asthma", "Dengue"]
}

rubi_hospital["patient_name"].sort()
rubi_hospital["dr_name"].sort(reverse=True)
rubi_hospital["room_no"].sort()
rubi_hospital["disease"].sort(reverse=True)

print(rubi_hospital)
