function path = reconstructPath(originDict, current)

current = current(1)+100*current(2);
path = current;

while isKey(originDict,current)
    current = originDict(current);
    path = [current path];
end

end