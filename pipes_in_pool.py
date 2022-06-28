vol_ltr = int(input())
debit_p_1 = int(input())
debit_p_2 = int(input())
hours = float(input())

p_1_v = debit_p_1 * hours
p_2_v = debit_p_2 * hours
p_1_v_percent = (p_1_v * 100) / (p_1_v + p_2_v)
p_2_v_percent = (p_2_v * 100) / (p_1_v + p_2_v)


total_percent_full = ((p_1_v + p_2_v) * 100) / vol_ltr

if (p_1_v + p_2_v) <= vol_ltr:
    print(f"The pool is {total_percent_full}% full. Pipe 1: {p_1_v_percent:.2f}%. Pipe 2: {p_2_v_percent:.2f}%.")
else:
    print(f"For {hours} hours the pool overflows with {p_1_v + p_2_v - vol_ltr} liters.")
