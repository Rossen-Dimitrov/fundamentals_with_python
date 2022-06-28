time_period = int(input())
treated = 0
untreated = 0
doctors = 7
for days in range(1, time_period + 1):
    patients = int(input())
    if days % 3 == 0 and untreated > treated:
        doctors += 1
    if patients <= doctors:
        treated += patients
    elif patients > doctors:
        treated += doctors
        untreated += patients - doctors
print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")
