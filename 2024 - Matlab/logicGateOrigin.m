function output = logicGateOrigin(statementIn, dict, output)

tmp = statementIn{1};

if ~xor(tmp{1}(1)~='x',tmp{1}(1)~='y')
    value1 = logicGateOrigin(dict(tmp{1}),dict,'');
    value2 = logicGateOrigin(dict(tmp{3}),dict,'');
else
    value1 = tmp{1};
    value2 = tmp{3};
end

operator = tmp{2};

output = [output string(value1) string(operator) string(value2)];

end