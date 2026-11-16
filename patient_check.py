import csv

with open("patients.csv", "r", newline="" , encoding="utf-8-sig") as data_file: 
     reader = csv.DictReader(data_file)
     patients = list(reader)

for patient in patients:
     age_text = patient["age"]
     if age_text is None:
          age_text = ""
     age_text = age_text.strip()

     if age_text == "":
          age = None 
     else:
          try: 
               age = float(age_text)
          except ValueError:
               age = age_text
     patient["age"] = age
     

issue_count = 0
issues = []
seen_ids = set()

for row_number, patient in enumerate(patients , start = 2): 
    patient_id = patient["id"].strip()
    age = patient["age"]
    if patient_id == "":
         print("Row", row_number, patient_id, "Missing ID")
         issues.append({
              "row": row_number,
              "patient_id" : patient_id,
              "message" : "Missing ID"
         })
    elif patient_id in seen_ids:
         print("Row", row_number, patient_id, "Duplicate ID")
         issues.append({
              "row" : row_number,
              "patient_id" : patient_id,
              "message" : "Duplicate ID"
         })
    else:
         seen_ids.add(patient_id)
    if age is None:
        print("Row", row_number, patient["id"], "Missing age")
        issue_count += 1
        issues.append({
            "row" : row_number,
            "patient_id" : patient["id"],
            "message" : "Missing Age"
        })
    elif not isinstance(age, (int, float)):
        print("Row", row_number, patient["id"], "Age must be a number")
        issue_count += 1
        issues.append({
            "row" : row_number,
            "patient_id" : patient["id"],
            "message" : "Age must be a number "
        })
    elif age < 0:
        print("Row", row_number, patient["id"], "Negative age")
        issue_count += 1
        issues.append({
            "row" : row_number,
            "patient_id" : patient["id"],
            "message" : "Negative age"
        })
    else:
        print("Row", row_number, patient["id"], "Age passed these checks")

print(" Total patients: ", len(patients))
print("Patients with age issues :" , issue_count)
print("Total issues:", len(issues))

with open("issues_report.csv", "w", newline="", encoding="utf-8-sig") as report_file: 
        writer = csv.DictWriter(report_file, fieldnames=["row", "patient_id", "message"])
        writer.writeheader()
        writer.writerows(issues)
        