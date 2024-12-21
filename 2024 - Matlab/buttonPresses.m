function presses = buttonPresses(code,dict)

code = [100,code];
presses = zeros(1,3*length(code));
indexEnd = 1;

for i=1:numel(code)-1
    start = code(i);
    goal  = code(i+1);

    tmpPresses = dict(10*start+goal);
    tmpPresses = [tmpPresses{1},100];
    
    indexStart = indexEnd+1;
    indexSize = length(tmpPresses);
    indexEnd = indexStart+indexSize-1;

    presses(indexStart:indexEnd) = tmpPresses;
end

presses(presses==0) = [];

end