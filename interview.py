import csv

file_path = input("Enter CSV file path: ")

with open(file_path, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    headers = next(reader)

print("\nAvailable columns:")
for i, h in enumerate(headers):
    print(f"{i+1}. {h}")

col_index = int(input("\nEnter column number: ")) - 1
colname = headers[col_index]

names_list = []
department_set = set()
interview_data = []  
total = 0
attended_count = 0
skipped = 0

with open(file_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for row in reader:
        value = row[colname].strip()

        if col_index == 0:
            names_list.append(value)

        if col_index == 1:
            department_set.add(value)

        if col_index == 2:
            if value == "":
                skipped += 1
                continue
            try:
                num = float(value)
                total += num
                attended_count += 1
                interview_data.append((row[headers[0]], num))   
            except:
                skipped += 1

print("\n------------------ Result ------------------")

if col_index == 0:
    print(f"Total Members: {len(names_list)}")
    print("Names:")
    for name in names_list:
        print(" -", name)

elif col_index == 1:
    print(f"Total Departments: {len(department_set)}")
    print("Departments:")
    for d in department_set:
        print(" -", d)

elif col_index == 2:
    print(f"Total Interview Count = {total}")
    print(f"Total Attended = {attended_count}, Skipped = {skipped}")
    print("\nAttendance Details:")
    for name, count in interview_data:
        print(f" - {name}: {count}")
