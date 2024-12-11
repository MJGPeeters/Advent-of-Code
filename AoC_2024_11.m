%% Preamble
adventDay = 11;
testBool = 0;

if testBool
    fileName = "Test_2024_" + adventDay + ".txt";
else
    fileName = "Input_2024_" + adventDay + ".txt"; 
end

%% Read data
tic

fileID = fopen(fileName);
initialStones = fgetl(fileID);
initialStones = sscanf(initialStones,'%d')';
fclose(fileID);

%% Solve part I

% Rules
% - If stone is 0, it becomes 1
% - If the stone has an even number of digits n, leftmost n/2 digits become
%   one new stone, rightmost n/2 digits become another new stone
% - If previous rules do not apply, stones number is multiplied by 2024

stones = initialStones;

for blink=1:25
    stonesLength = numel(stones);
    newStones = zeros(stonesLength*2,1);
    k = 1;

    for j=1:stonesLength
        if stones(j)==0
            newStones(k) = 1;
            k = k+1;
        elseif mod(num_digits(stones(j)),2)==0
            numDigitsNew = num_digits(stones(j))/2;
            newStones(k) = floor(stones(j)/10^numDigitsNew);
            newStones(k+1) = mod(stones(j),10^numDigitsNew);
            k = k+2;
        else
            newStones(k) = stones(j)*2024;
            k = k+1;
        end
    end

    stones = newStones(1:k-1);
end

result1 = numel(stones);

time1 = toc;

%% Display results of part I
out1 = sprintf('After twenty-five blinks you will have %d stones.', result1);
tim1 = sprintf('Calculation took %f seconds.', time1);
disp(out1)
disp(tim1)

% %% Solve part II
% tic
% 
% result2 = 0;
% 
% time2 = toc;
% 
% %% Display results of part II
% out2 = sprintf('The new checksum is %d', result2);
% tim2 = sprintf('Calculation took %f seconds.', time2);
% disp(out2)
% disp(tim2)