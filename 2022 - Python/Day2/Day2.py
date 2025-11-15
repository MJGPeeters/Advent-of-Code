from timeit import default_timer as timer

start_time_1 = timer()

TEST = False

if TEST:
    FILE_NAME = "Example.txt"
else:
    FILE_NAME = "Input.txt"

with open(FILE_NAME, 'r') as file:
    rounds = [[line[0], line[2]] for line in file]

play_dict = {'A':1, 'B':2, 'C':3, 'X':1, 'Y':2, 'Z':3}
score = 0

for round in rounds:
    opponent_play, response_play = play_dict[round[0]], play_dict[round[1]]
    if opponent_play==response_play:
        outcome = 3
    elif response_play==1:
        if opponent_play==2:
            outcome = 0
        else:
            outcome = 6
    elif response_play==2:
        if opponent_play==1:
            outcome = 6
        else:
            outcome = 0
    else:
        if opponent_play==1:
            outcome = 0
        else:
            outcome = 6
    
    score += response_play + outcome

end_time_1 = timer()

print(score)
#print(sum(max_calories))
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')
