import random
from collections import Counter

# รวบรวมหมายเลขที่ถูกรางวัลทั้งหมดลงในรายการเดียว
winning_numbers = [
    367336, 434503, 518504, 530593, 205690, 980116, 327106, 803481, 997626,
    253603, 941395, 607063, 105979, 625544, 356757, 251097, 557990, 743951,
    931446, 727202, 320812, 915478, 471782, 260453, 169530, 922605, 264872,
    125272, 132903, 843019, 984906, 87907, 25873, 417652, 590417, 297411,
    812519, 157196, 845093, 375805, 121789, 913106, 613106, 484669, 943703,
    929332, 331583, 436594, 620405, 981417, 361807, 510541, 529924, 453522,
    17223, 967375, 812564, 691197, 340388, 798787, 775476, 387006, 369765,
    943647, 174055, 516461, 962526, 61324, 570331, 109767, 724628, 345650,
    74824, 967134, 197079, 735867, 356564, 21840, 989903, 149840, 200515,
    452643, 149760, 734510, 586117, 386602, 596324, 963623, 223131, 988117,
    75629, 248038, 739229, 412073, 218559, 759415, 309915, 26853, 203832,
    911234, 955596, 451005, 292391, 533726, 413494, 880714, 817927, 641524,
    644742, 388881, 11421, 543466, 506260, 605704, 48151, 240237, 1864,
    155537, 244351, 461704, 948354, 480449, 479804, 206608, 656409, 375615,
    772269, 856763, 662842, 766391, 468728, 378477, 673920
]

# นำหมายเลขที่ถูกรางวัลทั้งหมดมาเป็นสตริง
winning_numbers_str = "".join(map(str, winning_numbers))

# นับความถี่ของแต่ละคู่ของตัวเลขสองหลัก
two_digit_frequency = Counter(winning_numbers_str[i:i+2] for i in range(len(winning_numbers_str)-1))

# นับความถี่ของแต่ละคู่ของตัวเลขสามหลัก
three_digit_frequency = Counter(winning_numbers_str[i:i+3] for i in range(len(winning_numbers_str)-2))

# ทำการปรับความถี่ให้เป็นความน่าจะเป็น
total_two_digits = sum(two_digit_frequency.values())
total_three_digits = sum(three_digit_frequency.values())

two_digit_probabilities = {digits: freq / total_two_digits for digits, freq in two_digit_frequency.items()}
three_digit_probabilities = {digits: freq / total_three_digits for digits, freq in three_digit_frequency.items()}

# สร้างหมายเลข 6 หลักใหม่โดยใช้ความน่าจะเป็นที่ได้จากเลข 2 หลักและ 3 หลัก
def generate_weighted_random_number():
    # เลือกเลข 2 หลักแรก
    first_two_digits = random.choices(list(two_digit_probabilities.keys()), weights=two_digit_probabilities.values(), k=1)[0]
    
    # เลือกเลข 3 หลักถัดไป
    middle_three_digits = random.choices(list(three_digit_probabilities.keys()), weights=three_digit_probabilities.values(), k=1)[0]
    
    # เลือกเลข 1 หลักสุดท้ายจากเลข 2 หลักอีกครั้ง
    last_digit = random.choices(list(two_digit_probabilities.keys()), weights=two_digit_probabilities.values(), k=1)[0][0]
    
    # รวมเป็นเลข 6 หลัก
    return first_two_digits + middle_three_digits + last_digit

# สร้างหมายเลข 6 หลักใหม่จำนวน 3 ชุด
new_numbers = [generate_weighted_random_number() for _ in range(3)]

# แสดงผลลัพธ์
print(new_numbers)