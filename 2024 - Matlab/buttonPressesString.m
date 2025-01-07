function presses = buttonPressesString(code,dict)

code = ['A',code];
presses = [];

for i=1:strlength(code)-1
    presses = join([presses,dict(join([code(i),code(i+1)],""))],"");
end

presses = char(presses);

end