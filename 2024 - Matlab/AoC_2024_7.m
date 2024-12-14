%% Preamble
adventDay = 7;
testBool = 0;

if testBool
    fileName = "Test_2024_" + adventDay + ".txt";
    numCalibrations = 9;
else
    fileName = "Input_2024_" + adventDay + ".txt"; 
    numCalibrations = 850;
end

%% Read data
dataCell = {};

fileID = fopen(fileName,'rt');

for i=1:numCalibrations
    line = fgetl(fileID);
    splitLine = split(line,':')';

    dataCell{i,1} = str2double(splitLine{1});

    numbers = str2double(split(splitLine{2}));
    dataCell{i,2} = numbers(~isnan(numbers));
end

fclose(fileID);

% %% Solve part I
% tic 
% 
% result1 = 0;
% outcomeArray = zeros(numCalibrations,1);
% 
% for i=1:numCalibrations
%     testValue = dataCell{i,1};
%     numbers = dataCell{i,2};
% 
%     numOptions = 2^(numel(numbers)-1);
%     numOperators = ceil(log2(numOptions));
%     
%     for j=0:numOptions-1
%         equationResult = testValue;
% 
%         for k=numOperators:-1:1
%             tmp = bitand(j,2^(k-1));
%             
%             if tmp>0 && mod(equationResult,numbers(k+1))==0
%                 equationResult = equationResult/numbers(k+1);
%             elseif tmp==0 
%                 equationResult = equationResult-numbers(k+1);
%             else
%                 break
%             end
%         end
% 
%         if equationResult==numbers(1)
%             result1 = result1 + testValue;
%             outcomeArray(i) = 1;
%             break
%         end
%     end
% end
% 
% time1 = toc;
% 
% %% Display results of part I
% out1 = sprintf('The total calibration result is %d.', result1);
% tim1 = sprintf('Calculation took %f seconds.', time1);
% disp(out1)
% disp(tim1)

%% Solve part II
tic 

result2 = 0;

for i=1:numCalibrations
    testValue = dataCell{i,1};
    numbers = dataCell{i,2};

    if outcomeArray(i)==1
        result2 = result2 + testValue;
        continue
    end

    numOptions = 3^(numel(numbers)-1);
    numOperators = floor(log(numOptions)/log(3));

    for j=0:numOptions-1
        tmp = dec2base(j,3,numOperators);
        equationResult = testValue;

        for k=numOperators:-1:1
            tmp2 = str2double(tmp(k));

            if tmp2==2
                num = numbers(k+1);
                numDigits = floor(log10(num))+1;
                if mod(equationResult-num,10^numDigits)==0
                    equationResult = (equationResult-num)/10^numDigits;
                else
                    break
                end
            elseif tmp2==1 && mod(equationResult,numbers(k+1))==0
                equationResult = equationResult/numbers(k+1);
            elseif tmp2==0
                equationResult = equationResult-numbers(k+1);
            else
                break
            end
        end

        if equationResult==numbers(1)
            result2 = result2 + testValue;
            break
        end
    end
end

time2 = toc;

% Display results of part II
out2 = sprintf('The new calibration result is %d.', result2);
tim2 = sprintf('Calculation took %f seconds.', time2);
disp(out2)
disp(tim2)