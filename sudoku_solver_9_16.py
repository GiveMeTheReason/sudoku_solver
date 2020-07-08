size = 0
while not (size == 9 or size == 16):
    size = int(input())

quad_size = int(pow(size, 1/2))
if size == 9:
    set_range = set('123456789')
if size == 16:
    set_range = set('123456789ABCDEFG')
desk = []
flag = True
iteration = 0
has_solution = True

i = size
while i > 0:
    s = list(input())
    if len(s) == size:
        desk.append(s)
        i = i - 1
    else:
        print('String is incorrect! Repeat it')

while flag and has_solution:
    flag = False
    iteration = iteration + 1
    changes = 0
    for i in range(size):
        for j in range(size):
            if desk[i][j] not in set_range and has_solution:
                used_set = set()

                for string_check in range(size):
                    if type(desk[i][string_check]) == str:
                        used_set.add(desk[i][string_check])

                for row_check in range(size):
                    if type(desk[row_check][j]) == str:
                        used_set.add(desk[row_check][j])

                quad_i = i // quad_size
                quad_j = j // quad_size
                for quad_check_i in range(quad_i*quad_size, (quad_i+1)*quad_size):
                    for quad_check_j in range(quad_j*quad_size, (quad_j+1)*quad_size):
                        if type(desk[quad_check_i][quad_check_j]) == str:
                            used_set.add(desk[quad_check_i][quad_check_j])
                
                posibble_answer = set_range - used_set
                if len(posibble_answer) == 1:
                    desk[i][j] = ''.join(posibble_answer)
                    changes = changes + 1
                elif len(posibble_answer) == 0:
                    print('Puzzle has no solutions!')
                    has_solution = False
                else:
                    desk[i][j] = posibble_answer
                    flag = True

    if changes == 0 and flag and has_solution:
        for item in set_range:
            for i in range(size):
                pos = -1
                for string_check in range(size):
                    if desk[i][string_check] == item:
                        break
                    if type(desk[i][string_check]) == set:
                        if item in desk[i][string_check]:
                            if pos == -1:
                                pos = string_check
                            else:
                                pos = -1
                                break
                
                if pos != -1:
                    desk[i][pos] = item
                    changes = changes + 1
                    for row_check in range(size):
                        if type(desk[row_check][pos]) == set:
                            desk[row_check][pos] = desk[row_check][pos] - set(item)
                    quad_i = i // quad_size
                    quad_j = pos // quad_size
                    for quad_check_i in range(quad_i*quad_size, (quad_i+1)*quad_size):
                        for quad_check_j in range(quad_j*quad_size, (quad_j+1)*quad_size):
                            if type(desk[quad_check_i][quad_check_j]) == set:
                                desk[quad_check_i][quad_check_j] = desk[quad_check_i][quad_check_j] - set(item)
        
            for j in range(size):
                pos = -1
                for row_check in range(size):
                    if desk[row_check][j] == item:
                        break
                    if type(desk[row_check][j]) == set:
                        if item in desk[row_check][j]:
                            if pos == -1:
                                pos = row_check
                            else:
                                pos = -1
                                break
                
                if pos != -1:
                    desk[pos][j] = item
                    changes = changes + 1
                    for string_check in range(size):
                        if type(desk[pos][string_check]) == set: 
                            desk[pos][string_check] = desk[pos][string_check] - set(item)
                    quad_i = pos // quad_size
                    quad_j = j // quad_size
                    for quad_check_i in range(quad_i*quad_size, (quad_i+1)*quad_size):
                        for quad_check_j in range(quad_j*quad_size, (quad_j+1)*quad_size):
                            if type(desk[quad_check_i][quad_check_j]) == set:
                                desk[quad_check_i][quad_check_j] = desk[quad_check_i][quad_check_j] - set(item)

            for i in range(0, size, quad_size):
                for j in range(0, size, quad_size):
                    pos_i = -1
                    pos_j = -1
                    quad_i = i // quad_size
                    quad_j = j // quad_size
                    flag_1 = True
                    for quad_check_i in range(quad_i*quad_size, (quad_i+1)*quad_size):
                        for quad_check_j in range(quad_j*quad_size, (quad_j+1)*quad_size):
                            if desk[quad_check_i][quad_check_j] == item:
                                flag_1 = False
                            if type(desk[quad_check_i][quad_check_j]) == set and flag_1:
                                if item in desk[quad_check_i][quad_check_j]:
                                    if pos_i == -1 and pos_j == -1:
                                        pos_i = quad_check_i
                                        pos_j = quad_check_j
                                    else:
                                        pos_i = -1
                                        pos_j = -1
                                        flag_1 = False
                    
                    if pos_i != -1 and pos_j != -1:
                        desk[pos_i][pos_j] = item
                        changes = changes + 1
                        for string_check in range(size):
                            if type(desk[pos_i][string_check]) == set:
                                desk[pos_i][string_check] = desk[pos_i][string_check] - set(item)
                        for row_check in range(size):
                            if type(desk[row_check][pos_j]) == set:
                                desk[row_check][pos_j] = desk[row_check][pos_j] - set(item)
    
    if changes == 0 and has_solution:
        print('Puzzle has multiple solutions!')
        print('Final point:')
        break

for i in range(size):
    for j in range(size):
        if type(desk[i][j]) == set:
            desk[i][j] = '-'

if has_solution:
    for i in range(size):
        print(desk[i])

print('Iterations: ', iteration)
