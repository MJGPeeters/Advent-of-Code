%% Read data
testData  = importdata("Test_2024_04.txt");
inputData = importdata("Input_2024_04.txt");

%% Solve part I

unpaddedData = inputData;
numXMAS = 0;

clear data

% Add padding
data{1} = char(ones(1,length(unpaddedData{1})+6)*46);
data{2} = char(ones(1,length(unpaddedData{1})+6)*46);
data{3} = char(ones(1,length(unpaddedData{1})+6)*46);
data{numel(unpaddedData)+4} = char(ones(1,length(unpaddedData{1})+6)*46);
data{numel(unpaddedData)+5} = char(ones(1,length(unpaddedData{1})+6)*46);
data{numel(unpaddedData)+6} = char(ones(1,length(unpaddedData{1})+6)*46);

for i=1:numel(unpaddedData)
    data{i+3} = append('...',unpaddedData{i},'...');
end

for i=4:numel(data)-3
    xArray = find(data{i}=='X');

    for n=1:numel(xArray)
        j = xArray(n);
        
        % Horizontal
        if all(data{i}(j-1:-1:j-3)=='MAS')
            numXMAS = numXMAS+1; end
        if all(data{i}(j+1:j+3)=='MAS')
            numXMAS = numXMAS+1; end

        % Vertical 
        if all([data{i-1}(j) data{i-2}(j) data{i-3}(j)]=='MAS')
            numXMAS = numXMAS+1; end
        if all([data{i+1}(j) data{i+2}(j) data{i+3}(j)]=='MAS')
            numXMAS = numXMAS+1; end

        % Diagonal one way
        if all([data{i-1}(j-1) data{i-2}(j-2) data{i-3}(j-3)]=='MAS')
            numXMAS = numXMAS+1; end
        if all([data{i+1}(j+1) data{i+2}(j+2) data{i+3}(j+3)]=='MAS')
            numXMAS = numXMAS+1; end

        % Diagonal other way
        if all([data{i-1}(j+1) data{i-2}(j+2) data{i-3}(j+3)]=='MAS')
            numXMAS = numXMAS+1; end
        if all([data{i+1}(j-1) data{i+2}(j-2) data{i+3}(j-3)]=='MAS')
            numXMAS = numXMAS+1; end
    end
end

%% Display results of part I
out1 = sprintf('XMAS appears %d times in the word search.', numXMAS);
disp(out1)

%% Solve part II

numXofMAS = 0;

data2 = unpaddedData;

for i=2:numel(data2)-1
    xArray = find(data2{i}=='A');

    for n=1:numel(xArray)
        if xArray(n)==1 || xArray(n)==140
            continue
        end

        j = xArray(n);

        if all(ismember([data2{i-1}(j-1) data2{i-1}(j+1) data2{i+1}(j-1) data2{i+1}(j+1)],{'MMSS','SSMM','MSMS','SMSM'}))
            numXofMAS = numXofMAS+1; 
        end

    end
end

%% Display results of part II
out2 = sprintf('An X of MAS appears %d times in the word search.', numXofMAS);
disp(out2)