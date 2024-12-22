%% Preamble
adventDay = 22;
testBool = 1;

if testBool
    fileName = "Tests/Test_2024_" + adventDay + ".txt";
else
    fileName = "Inputs/Input_2024_" + adventDay + ".txt"; 
end

%% Read data
importNumbers = importdata(fileName);

%% Solve part I

tic

importNumbers = [1 2 3 2024];

tmp = importNumbers;

for i=1:2000
    tmp = mod(bitxor(tmp*64,tmp),16777216);
    tmp = mod(bitxor(floor(tmp/32),tmp),16777216);
    tmp = mod(bitxor(tmp*2048,tmp),16777216);
end

sumTotal = sum(tmp);

result1 = sumTotal;

time1 = toc;

%% Display results of part I
fprintf('The sum of all the secret numbers is %d.\n', result1);
fprintf('Calculation took %f seconds.\n', time1);

%% Solve part II

tic

tmp = importNumbers;

numberArray = zeros(numel(importNumbers),2001);
numberArray(:,1) = mod(tmp,10);

changeArray = zeros(numel(importNumbers),2000);

for i=1:2000
    tmp = mod(bitxor(tmp*64,tmp),16777216);
    tmp = mod(bitxor(floor(tmp/32),tmp),16777216);
    tmp = mod(bitxor(tmp*2048,tmp),16777216);
    numberArray(:,i+1) = mod(tmp,10);
    changeArray(:,i) = numberArray(:,i+1)-numberArray(:,i);
end

minChange = -20;
maxChange = +20;

sumArray = [];

for i=minChange:maxChange
    for j=minChange:maxChange
        for k=minChange:maxChange
            for l=0:maxChange
                tmp = 0;
                for n=1:size(changeArray,1)
                    changes = [i,j,k,l];
                    
                    index = strfind(changeArray(n,:),changes);
                    if ~isempty(index)
                        out = numberArray(n,index+4);
                        tmp = tmp+out;
                    end
                end
                if tmp==23
                    disp([i j k l])
                end
                sumArray = [sumArray, tmp];
            end
        end
    end
end


result2 = 0;

time2 = toc;

%% Display results of part II
fprintf('You can get at most %d bananas.\n', result2);
fprintf('Calculation took %f seconds.\n', time2);