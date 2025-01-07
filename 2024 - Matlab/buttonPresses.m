function presses = buttonPresses(code,dict)

code = [100,code];
presses = [];

for i=1:numel(code)-1
    start = code(i);
    goal  = code(i+1);

    tmpPresses = dict(10*start+goal);
    presses = [presses, tmpPresses{1}, 100]; %#ok<AGROW>
end