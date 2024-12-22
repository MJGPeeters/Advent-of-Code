%% Preamble
adventDay = 22;
testBool = 0;

if testBool
    fileName = "Tests/Test_2024_" + adventDay + ".txt";
else
    fileName = "Inputs/Input_2024_" + adventDay + ".txt"; 
end

%% Read data
importNumbers = importdata(fileName);

%% Solve part I
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

%% Display results of part I
fprintf('The sum of all the secret numbers is %d.\n', sum(tmp));
toc

%% Solve part II
tic

numBuyers = size(numberArray,1);
overviewArray = zeros(numBuyers,19^4);

for n=1:numBuyers
    for i=1997:-1:1
        m = sum([20^3 20^2 20 1].*(9+changeArray(n,i:i+3)));
        B = numberArray(n,i+4);
        overviewArray(n,m) = B;
    end
end

%% Display results of part II
fprintf('You can get at most %d bananas.\n', max(sum(overviewArray,1)));
toc