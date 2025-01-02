function [output,logicTreeOutputs] = logicGateOrigin(statementIn, dict, output,logicTreeOutputs)

%% TO DO
% Make a list of all the outputs in the logic tree

tmp = statementIn{1};

if ~xor(tmp{1}(1)~='x',tmp{1}(1)~='y')
    logicTreeOutputs = [logicTreeOutputs; tmp{1}; tmp{3}];
    value1 = logicGateOrigin(dict(tmp{1}),dict,'',logicTreeOutputs);
    value2 = logicGateOrigin(dict(tmp{3}),dict,'',logicTreeOutputs);
else
    value1 = tmp{1};
    value2 = tmp{3};
end

operator = tmp{2};

output = [output string(value1) string(operator) string(value2)];

output(output=="") = [];
logicTreeOutputs(logicTreeOutputs=="") = [];

end