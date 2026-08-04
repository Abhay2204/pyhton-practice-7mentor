clg = ["COEP", "MIT", "DY Patil", "PICT", "VIT"]

print("Accessed Clg:", clg[1])

idx_dy = clg.index("DY Patil")
rem_clg = clg.pop(idx_dy)
print("Removed Clg:", rem_clg)

idx_mit = clg.index("MIT")
clg.insert(idx_mit + 1, "ASM CSIT")
print("Updated Clg:", clg)

grades = ["A++", "A+", "A", "A+", "A+"]
print("Grades:", grades)

rec = dict(zip(clg, grades))
print("Final Record:", rec)
