total = 0
# calibration value 
# Part: 1
def calibration_value(sentence):
    global total
    curr_sum = 0
    nums = [] 
    for letter in list(sentence):
        if letter.isdigit():
            nums.append(int(letter))

    curr_sum = (curr_sum * 10) + nums[0]
    curr_sum = (curr_sum * 10) + nums[-1]
    total += curr_sum
    


with open('input.txt', 'r') as input_file:
    for line in input_file.readlines():
        calibration_value(line) 
# calibration_value("rstsevensix4oneseven7mrccrxmht") - 47
print(total)