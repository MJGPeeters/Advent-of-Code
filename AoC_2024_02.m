%% Read data
testData = importDataFile('Test_2024_02.txt',[6,5]);
inputData = importDataFile('Input_2024_02.txt',[1000,8]);

%% Solve part I
safeNumber = 0;

for i=1:size(inputData)
    report = inputData(i,:);
    report = report(~isnan(report));

    diffReport = diff(report);

    parityCheck = diffReport(1)*diffReport;

    if all(parityCheck>0) && all(abs(diffReport)>0 & abs(diffReport)<4)
        safeNumber = safeNumber+1;
    end
end

%% Display results of part I
out1 = sprintf('The number of safe reports is %d without dampener.', safeNumber);
disp(out1)

%% Solve part II
safeNumberDampener = 0;

for i=1:size(inputData)
    report = inputData(i,:);
    report = report(~isnan(report));
    dampenerHelps = 0;

    for j=1:numel(report)
        tmpReport = report;
        tmpReport(j) = [];
        diffReport = diff(tmpReport);
    
        parityCheck = diffReport(1)*diffReport;
    
        if all(parityCheck>0) && all(abs(diffReport)>0 & abs(diffReport)<4)
            dampenerHelps = 1;
        end
    end
    
    if dampenerHelps
        safeNumberDampener = safeNumberDampener+1;
    end
end

%% Display results of part II
out2 = sprintf('The number of safe reports is %d with dampener.', safeNumberDampener);
disp(out2)