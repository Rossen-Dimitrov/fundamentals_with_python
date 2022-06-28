height = int(input())
test_height = height - 30
jump_counter = 0
bad_jump = 0
failed = False
while not failed:
    current_jump = int(input())
    jump_counter += 1
    if current_jump <= test_height:
        bad_jump += 1
        if bad_jump == 3:
            failed = True
    else:
        if current_jump >= height:
            break
        test_height += 5
        bad_jump = 0

if not failed:
    print(f"Tihomir succeeded, he jumped over {test_height}cm after {jump_counter} jumps.")
else:
    print(f"Tihomir failed at {test_height}cm after {jump_counter} jumps.")






