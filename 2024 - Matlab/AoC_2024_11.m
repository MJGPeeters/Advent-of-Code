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

%% Solve part II
tic

stones = ones(numel(initialStones),2);
stones(:,1) = initialStones;

d = dictionary;
d(0) = 1;

for blink=1:75
    stonesLength = size(stones,1);
    newStones = zeros(stonesLength*2,2);
    k = 1;

    for j=1:stonesLength
        if isKey(d,stones(j,1))
            tmp = d(stones(j,1));
            for n=1:numel(tmp)
                newStones(k,1) = tmp(n);
                newStones(k,2) = stones(j,2);
                k = k+1;
            end
        elseif stones(j,1)==0
            newStones(k,1) = 1;
            newStones(k,2) = stones(j,1);
            k = k+1;
        elseif mod(num_digits(stones(j,1)),2)==0
            numDigitsNew = num_digits(stones(j,1))/2;
            newStones(k,1) = floor(stones(j,1)/10^numDigitsNew);
            newStones(k,2) = stones(j,2);
            newStones(k+1,1) = mod(stones(j,1),10^numDigitsNew);
            newStones(k+1,2) = stones(j,2);
            k = k+2;
        else
            newStones(k,1) = stones(j,1)*2024;
            newStones(k,2) = stones(j,2);
            k = k+1;
        end
    end

    tmpA = newStones(1:k-1,1);
    tmpB = newStones(1:k-1,2);
    tmpC = unique(tmpA);

    stones = zeros(numel(tmpC),2);

    for i=1:numel(tmpC)
        stones(i,1) = tmpC(i);
        stones(i,2) = sum(tmpB(tmpA==tmpC(i)));
    end
end

result2 = sum(stones(:,2));

time2 = toc;

%% Display results of part II
out2 = sprintf('After seventy-five blinks you will have %d stones.', result2);
tim2 = sprintf('Calculation took %f seconds.', time2);
disp(out2)
disp(tim2)