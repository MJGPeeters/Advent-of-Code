%% Preamble
adventDay = 19;
testBool = 0;

if testBool
    fileName = "Tests/Test_2024_" + adventDay + ".txt";
else
    fileName = "Inputs/Input_2024_" + adventDay + ".txt"; 
end

%% Solve part I

tic

fileID = fopen(fileName);
line = fgetl(fileID);

allTowels = strsplit(line);
towels = {};
possibleCount = 0;
n = 1;

for i=1:numel(allTowels)
    tmp = allTowels{i}(1:end-1);

    if numel(tmp)>1 && strcmp(tmp(end-1:end),'br')
        towels{n} = tmp;
        n = n+1;
    end
end

fgetl(fileID);
line = fgetl(fileID);

while line~=-1
    pattern = line;

    possibleCount = possibleCount + pattern_check(pattern,towels);

    line = fgetl(fileID);
end

fclose(fileID);

%% Display results of part I
fprintf('%d designs are possible.\n', possibleCount);
toc

%% Solve part II

tic

fileID = fopen(fileName);
line = fgetl(fileID);

allTowels = strsplit(line);
towels = {};
totalOptions = 0;
patternDict = dictionary;
patternDict('g') = 1;

for i=1:numel(allTowels)
    if i<numel(allTowels)
        towels{i} = allTowels{i}(1:end-1);
    else
        towels{i} = allTowels{i};
    end
end

fgetl(fileID);
line = fgetl(fileID);

while line~=-1
    pattern = line;

    [numOptions,patternDict] = find_all_patterns(pattern,towels,patternDict);

    totalOptions = totalOptions + numOptions;

    line = fgetl(fileID);
end

fclose(fileID);

%% Display results of part II
fprintf('The total number of options is %d.\n', totalOptions);
toc