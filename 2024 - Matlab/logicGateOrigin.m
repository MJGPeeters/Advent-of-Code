function [output,logicTreeOutputs,logicInputs] = logicGateOrigin(statementIn, dict, output,logicTreeOutputs,logicInputs)

%% TO DO
% Make a list of all the outputs in the logic tree

if numel(output)>500 || numel(logicTreeOutputs)>200
    return
end

tmp = statementIn{1};

if ~xor(tmp{1}(1)~='x',tmp{1}(1)~='y')
    logicTreeOutputs = [logicTreeOutputs; tmp{1}; tmp{3}];

    [value1,logicTreeOutputs,logicInputs] = logicGateOrigin(dict(tmp{1}),dict,'',logicTreeOutputs,logicInputs);
    [value2,logicTreeOutputs,logicInputs] = logicGateOrigin(dict(tmp{3}),dict,'',logicTreeOutputs,logicInputs);
else
    value1 = tmp{1};
    value2 = tmp{3};
    try
        logicInputs = [logicInputs;value1;value2];
    catch
        disp('test')
    end
end

operator = tmp{2};

output = [output string(value1) string(operator) string(value2)];

output(output=="") = [];
logicTreeOutputs(logicTreeOutputs=="") = [];

end