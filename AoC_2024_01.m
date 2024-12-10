%% Read data
testData = importdata('Test_2024_01.txt');
inputData = importdata('Input_2024_01.txt');

%% Solve part I
sortedData = sort(inputData,1);
distance = abs(sortedData(:,1)-sortedData(:,2));
totalDistance = sum(distance);

%% Display result of part I
out1 = sprintf('The total distance equals %d.', totalDistance);
disp(out1)

%% Solve part II
simScore = 0;

for i=1:length(inputData)
    locID = inputData(i,1);
    simScore = simScore + locID*numel(find(inputData(:,2)==locID));
end

%% Display result of part II
out2 = sprintf('The similarity score is %d.', simScore);
disp(out2)