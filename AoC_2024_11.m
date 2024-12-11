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

% %% Solve part I
% 
% stones = initialStones;
% 
% for blink=1:25
%     stonesLength = numel(stones);
%     newStones = zeros(stonesLength*2,1);
%     k = 1;
% 
%     for j=1:stonesLength
%         if stones(j)==0
%             newStones(k) = 1;
%             k = k+1;
%         elseif mod(num_digits(stones(j)),2)==0
%             numDigitsNew = num_digits(stones(j))/2;
%             newStones(k) = floor(stones(j)/10^numDigitsNew);
%             newStones(k+1) = mod(stones(j),10^numDigitsNew);
%             k = k+2;
%         else
%             newStones(k) = stones(j)*2024;
%             k = k+1;
%         end
%     end
% 
%     stones = newStones(1:k-1);
% end
% 
% result1 = numel(stones);
% 
% time1 = toc;
% 
% %% Display results of part I
% out1 = sprintf('After twenty-five blinks you will have %d stones.', result1);
% tim1 = sprintf('Calculation took %f seconds.', time1);
% disp(out1)
% disp(tim1)

%% Solve part II
tic

stones = initialStones;

% We know the evolution from every single digit stone. Once you arrive at a
% single digit stone, recursively (?) calculate what happens to it. Every
% time, check how far it is from blink 75. For every digit, if that is more
% than the number of steps until you arrive at only single digits again,
% return the number of stones at blink 75. 

% digitSteps = {
%     [1 1 2 4];
%     [1 2 4];
%     [1 2 4];
%     [1 2 4];
%     [1 2 4];
%     [1 1 2 4 8];
%     [1 1 2 4 8];
%     [1 1 2 4 8];
%     [1 1 2 4 8];
%     [1 1 2 4 8]
%     };
% 
% digitMap = {
%     [4 2 0 2 4];
%     [3 2 0 2 4];
%     [3 4 0 4 8];
%     [3 6 0 7 2];
%     [3 8 0 9 6];
%     [5 2 0 4 8 2 8 8 0];
%     [5 2 4 5 7 9 4 5 6];
%     [5 2 8 6 7 6 0 3 2];
%     [5 3 2 7 7 2 6 0 8];
%     [5 3 6 8 6 9 1 8 4];
%     };
% 
% 
% 
% stonesOut = stoneDigit(8,50,digitMap,digitSteps,0);

d = dictionary;

for blink=1:75
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



result2 = stonesOut;

time1 = toc;

%% Display results of part I
out1 = sprintf('After seventy-five blinks you will have %d stones.', result2);
tim1 = sprintf('Calculation took %f seconds.', time1);
disp(out1)
disp(tim1)