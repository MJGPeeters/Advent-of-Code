%% Preamble
adventDay = 23;
testBool = 0;

if testBool
    fileName = "Tests/Test_2024_" + adventDay + ".txt";
else
    fileName = "Inputs/Input_2024_" + adventDay + ".txt"; 
end

%% Read data
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

%% Solve part I

tic

sortedKeys = sort(keys(d));
k = 0;

for i=1:numel(sortedKeys)
    member1 = sortedKeys(i);
    char1 = char(member1);
    memberList = d(member1);
    memberList = memberList{1};
    for n=1:numel(memberList)-1
        member2 = memberList(n);
        char2 = char(member2);
        if isKey(d,member2)
            memberList2 = d(member2);
            memberList2 = memberList2{1};
            for m=n+1:numel(memberList)
                member3 = memberList(m);
                char3 = char(member3);
                if any(memberList2==member3) && (char1(1)=='t' || char2(1)=='t' || char3(1)=='t')
                   k = k+1;
                end
            end
        end
    end
end

result1 = k;

%% Display results of part I
fprintf('%d networks contain at least one valid computer.\n', result1);
toc

%% Solve part II

tic

sortedKeys = sort(keys(d));
mostMembers = 0;

for i=1:numel(sortedKeys)
    member1 = sortedKeys(i);
    char1 = char(member1);
    memberList = d(member1);
    memberList = memberList{1};

    n = 0;

    while numel(memberList)+1-n>mostMembers && n<3
        if n==0 && check_all_connections(memberList,d)
            mostMembers = numel(memberList)+1;
            largestNetwork = [member1; memberList];
        elseif n==1
            for k=1:numel(memberList)
                tmpMemberList = memberList;
                tmpMemberList(k) = [];
                if check_all_connections(tmpMemberList,d)
                    mostMembers = numel(tmpMemberList)+1;
                    largestNetwork = [member1; tmpMemberList];
                end
            end
        end
        n = n+1;
    end
end

networkString = '';
for i=1:numel(largestNetwork)
    networkString = [networkString ',' largestNetwork(i)];
end

networkString = join(networkString(3:end),'');

%% Display results of part II
fprintf('The password is %s.\n', networkString);
toc