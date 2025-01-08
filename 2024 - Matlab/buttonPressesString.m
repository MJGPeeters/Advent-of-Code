function [pressStringOut,countArrayOut] = buttonPressesString(code,codeCount,dict)

pressString = strings(1,numel(code));
pressCount = zeros(1,numel(code));

for n=1:numel(code)
    tmpCode = ['A',char(code(n))];
    tmpPressString = [];

    for i=1:strlength(tmpCode)-1
        tmpPressString = join([tmpPressString,dict(join([tmpCode(i),tmpCode(i+1)],""))],"");
    end
    
    pressString(n) = tmpPressString;
    pressCount(n) = codeCount(n);
end

groupStringSplit = [];
groupCountArray = [];

for i=1:numel(pressString)
    tmpPressChar = char(pressString(i));
    idx = [0,find(tmpPressChar=='A')];
    numGroups = numel(idx)-1;
    
    for j=1:numGroups
        groupStringSplit = [groupStringSplit, string(join(tmpPressChar(idx(j)+1:idx(j+1)),""))]; %#ok<AGROW>
        groupCountArray = [groupCountArray, pressCount(i)]; %#ok<AGROW>
    end
end

[counts,pressStringOut] = findgroups(groupStringSplit);
countArrayOut = accumarray(counts',groupCountArray);

end