%% Preamble
adventDay = 13;
testBool = 0;

if testBool
    fileName = "Test_2024_" + adventDay + ".txt";
else
    fileName = "Input_2024_" + adventDay + ".txt"; 
end

%% Solve part I
tic

fileID = fopen(fileName);

tokens = 0;
tmp = 0;

while tmp~=-1
    buttons = zeros(2);

    buttons(:,1) = sscanf(fgets(fileID),'Button A: X+%d, Y+%d');
    buttons(:,2) = sscanf(fgets(fileID),'Button B: X+%d, Y+%d');
    prize = sscanf(fgets(fileID),'Prize: X=%d, Y=%d');
    tmp = fgets(fileID);
    
    presses = buttons\prize;
    
    if sum(abs(presses-round(presses)))<0.0001
        tokens = tokens + presses(1)*3 + presses(2);
    end
end

fclose(fileID);

result1 = tokens;

time1 = toc;

%% Display results of part I
out1 = sprintf('You have to spend at least %d tokens.', result1);
tim1 = sprintf('Calculation took %f seconds.', time1);
disp(out1)
disp(tim1)

%% Solve part II
tic

fileID = fopen(fileName);

tokens = 0;
tmp = 0;

while tmp~=-1
    buttons = zeros(2);

    buttons(:,1) = sscanf(fgets(fileID),'Button A: X+%d, Y+%d');
    buttons(:,2) = sscanf(fgets(fileID),'Button B: X+%d, Y+%d');
    prize = sscanf(fgets(fileID),'Prize: X=%d, Y=%d')+1e13;
    tmp = fgets(fileID);
    
    presses = buttons\prize;
    
    if sum(abs(presses-round(presses)))<0.0001
        tokens = tokens + presses(1)*3 + presses(2);
    end
end

fclose(fileID);

result2 = tokens;

time2 = toc;

%% Display results of part I
out2 = sprintf('Now you have to spend at least %d tokens.', result2);
tim2 = sprintf('Calculation took %f seconds.', time2);
disp(out2)
disp(tim2)