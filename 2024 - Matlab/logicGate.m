function value = logicGate(valueIn, dict)

tmp = dict(valueIn);
tmp = tmp{1};

value1 = dict(tmp{1});
value1 = value1{1};
value2 = dict(tmp{3});
value2 = value2{1};

operator = tmp{2};

if ~isscalar(value1)
    value1 = logicGate(value1,dict);
end

if ~isscalar(value2)
    value2 = logicGate(value2,dict);
end

if numel(operator)==3 && all(operator=='AND')
    value = value1 && value2;
elseif numel(operator)==2 && all(operator=='OR')
    value = value1 || value2;
else
    value = xor(value1,value2);

end