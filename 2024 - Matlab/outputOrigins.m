function [inputs,outputs,returnFlag] = outputOrigins(inputGate,dict,inputs,outputs,inputGoalLength,returnFlag)

inputGate = inputGate{1};

checkOutputs = strjoin(outputs);

if numel(inputs)>inputGoalLength || returnFlag==1 || ~isempty(strfind(checkOutputs,inputGate{1})) || ~isempty(strfind(checkOutputs,inputGate{3}))
    returnFlag = 1;
    return
end


if ~(inputGate{1}(1)=='x' || inputGate{1}(1)=='y')
    outputs = [outputs; inputGate{1}; inputGate{3}];

    [inputs,outputs,returnFlag] = outputOrigins(dict(inputGate{1}),dict,inputs,outputs,inputGoalLength,returnFlag);
    if returnFlag
        return
    end
    [inputs,outputs,returnFlag] = outputOrigins(dict(inputGate{3}),dict,inputs,outputs,inputGoalLength,returnFlag);
    if returnFlag
        return
    end
else
    inputs = [inputs; inputGate{1}; inputGate{3}];
end

inputs(inputs=="") = [];
outputs(outputs=="") = [];

end