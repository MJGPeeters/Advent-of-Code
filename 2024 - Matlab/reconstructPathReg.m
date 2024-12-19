function path = reconstructPathReg(originDict, current)

current = 100*current(1)+current(2);
path = current;

while isKey(originDict,current)
    current = originDict(current);
    path = [current path];
end

end