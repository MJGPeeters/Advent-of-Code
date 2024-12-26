function value = logicGate(statementIn, dict)

tmp = statementIn{1};

value1 = dict(tmp{1});
value2 = dict(tmp{3});

operator = tmp{2};

if ~isscalar(value1{1})
    value1 = logicGate(value1,dict);
end

if ~isscalar(value2{1})
    value2 = logicGate(value2,dict);
end

if numel(operator)==3 && all(operator=='AND')
    value = {value1{1} && value2{1}};
elseif numel(operator)==2 && all(operator=='OR')
    value = {value1{1} || value2{1}};
else
    value = {xor(value1{1},value2{1})};
end

end