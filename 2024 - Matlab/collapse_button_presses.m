function [pressStringOut,countArrayOut] = collapse_button_presses(pressStringIn,countArrayIn)

% Inputs
% pressStringIn - string array of button presses
% countArrayIn  - associated array with counts for every button press

% Outputs
% pressStringOut - string array of button presses, divided in sections
%                  starting after A (unique instances)
% countArrayOut  - associated array with counts for every unique button 
%                  press present in pressStringOut

groupStringSplit = [];
groupCountArray = [];

for i=1:numel(pressStringIn)
    tmpPresses = char(pressStringIn(i));
    idx = [0,find(tmpPresses=='A')];
    numGroups = numel(idx)-1;
    
    for j=1:numGroups
        groupStringSplit = [groupStringSplit, string(join(presses(idx(j)+1:idx(j+1)),""))]; %#ok<AGROW>
        groupCountArray = [groupCountArray, countArrayIn(i)*ones(1,idx(j+1)-idx(j))]; %#ok<AGROW>
    end
end

[counts,pressStringOut] = findgroups(groupStringSplit);
countArrayOut = histcounts(counts);

end