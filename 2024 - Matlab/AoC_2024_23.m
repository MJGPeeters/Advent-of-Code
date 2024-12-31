%% Preamble
adventDay = 23;
testBool = 0;

if testBool
    fileName = "Tests/Test_2024_" + adventDay + ".txt";
else
    fileName = "Inputs/Input_2024_" + adventDay + ".txt"; 
end

%% Read data
tic
fileID = fopen(fileName);
line = fgetl(fileID);

d = dictionary;
tmpSorted = sort([string(line(1:2)),string(line(4:5))]);
tmp1 = string(tmpSorted(1));
tmp2 = {string(tmpSorted(2))};
d(tmp1) = tmp2;
line = fgetl(fileID);

while line~=-1
    tmpSorted = sort([string(line(1:2)),string(line(4:5))]);

    if isKey(d,tmpSorted(1))
        tmpMembers = d(tmpSorted(1));
        tmpMembers = [tmpMembers{1}; tmpSorted{2}];
        tmpMembers = sort(tmpMembers);
        d(tmpSorted(1)) = {tmpMembers};
    else
        tmp1 = string(tmpSorted(1));
        tmp2 = {string(tmpSorted(2))};
        d(tmp1) = tmp2;
    end

    line = fgetl(fileID);
end
toc
%% Solve part I

tic

sortedKeys = sort(keys(d));
networks = [];

for i=1:numel(sortedKeys)
    member1 = sortedKeys(i);
    char1 = char(member1);
    memberList = d(member1);
    memberList = memberList{1};
    for n=1:numel(memberList)-1
        member2 = memberList(n);
        char2 = char(member2);
        try
            memberList2 = d(member2);
            memberList2 = memberList2{1};
            for m=n+1:numel(memberList)
                member3 = memberList(m);
                char3 = char(member3);
                if any(memberList2==member3)
                    if char1(1)=='t' || char2(1)=='t' || char3(1)=='t'
                        networks = [networks; member1 member2 member3];
                    end
                end
            end
        end
    end
end

result1 = size(networks,1);

%% Display results of part I
fprintf('%d networks contain at least one valid computer.\n', result1);
toc

% %% Solve part II
% 
% tic
% 
% 
% 
% result2 = 0;
% 
% %% Display results of part II
% fprintf('Now, the sum of the complexities is %d.\n', result2);
% toc