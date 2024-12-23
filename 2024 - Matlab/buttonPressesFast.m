function pressesOut = buttonPressesFast(pressesIn,dict)

% Input: pressesIn - 2*n array, with the first row the movements (48, 62,
% 1004 etc.) and the second row the number of instances for each. 

% Output: pressesOut - 2xn array, with the first row the movements and the
% second row the number of instances for each. 

indexEnd = 0;

tmpPresses = ones(2,3*size(pressesIn,2));

for i=1:size(pressesIn,2)
    tmp = dict(pressesIn(1,i));
    tmp = [tmp{1},100];
    
    indexStart = indexEnd+1;
    indexEnd = indexStart+length(tmp)-1;
    tmpPresses(1,indexStart:indexEnd) = tmp;
    tmpPresses(2,indexStart:indexEnd) = pressesIn(2,i);
end

tmpPresses(:,tmpPresses(1,:)==1) = [];


%% Reshape data to make it a good input for the function
pressesOut = ones(2,size(tmpPresses,2)-1);

for i=1:size(tmpPresses,2)
    start = tmpPresses(i);
    goal  = tmpPresses(i+1);

    pressesOut(1,i) = 10*start+goal;
end

% Count unique instances of movements
for i=length(pressesOut):-1:1
    idxs = find(pressesOut(1,:)==pressesOut(1,i));
    pressesOut(2,idxs(1)) = pressesOut(2,idxs(1)) + numel(idxs)-1;
    if numel(idxs)>1
        pressesOut(:,idxs(end)) = [];
    end
end


%%

end