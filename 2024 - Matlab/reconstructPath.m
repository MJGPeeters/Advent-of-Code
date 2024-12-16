function path = reconstructPath(originDict, current)

current = 1e4*current(1)+10*current(2)+current(3);
path = current;

while isKey(originDict,current)
    current = originDict(current);
    path = [current path];
end

end