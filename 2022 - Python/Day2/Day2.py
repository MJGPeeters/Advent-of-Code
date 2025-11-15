from timeit import default_timer as timer

start_time_1 = timer()

TEST = False

if TEST:
    FILE_NAME = "Example.txt"
else:
    FILE_NAME = "Input.txt"

with open(FILE_NAME, 'r') as file:
    rounds = [[line[0], line[2]] for line in file]

play_dict1 = {'A':1, 'B':2, 'C':3, 'X':1, 'Y':2, 'Z':3}
score1 = 0

for round in rounds:
    opponent_play, response_play = play_dict1[round[0]], play_dict1[round[1]]
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
    
    score1 += response_play + outcome

play_dict2 = {'A':1, 'B':2, 'C':3, 'X':0, 'Y':3, 'Z':6}
score2 = 0

for round in rounds:
    opponent_play, outcome = play_dict2[round[0]], play_dict2[round[1]]
    if outcome==3:
        response_play = opponent_play
    elif outcome==0:
        if opponent_play==1:
            response_play = 3
        elif opponent_play==2:
            response_play = 1
        else:
            response_play = 2
    elif outcome==6:
        if opponent_play==1:
            response_play = 2
        elif opponent_play==2:
            response_play = 3
        else:
            response_play = 1
    
    score2 += response_play + outcome

end_time_1 = timer()

print(score1)
print(score2)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')
