%% Preamble
adventDay = 17;
testBool = 0;

if testBool
    fileName = "Tests/Test_2024_" + adventDay + "-1.txt";
else
    fileName = "Inputs/Input_2024_" + adventDay + ".txt"; 
end

%% Read data
fileID = fopen(fileName);

line = fgetl(fileID);
program = [];

while ~isscalar(line)
    tmp = strsplit(line,':');
    if ~isempty(tmp{1,1})
        if tmp{1,1}(1)=='P'
            programCell = strsplit(line,':');
            programCell = strsplit(programCell{1,2},',');
            for i=1:numel(programCell)
                program = [program double(string(programCell{i}))];
            end
        elseif all(tmp{1,1}=='Register A')
            regA = double(string(tmp{1,2}));
        elseif all(tmp{1,1}=='Register B')
            regB = double(string(tmp{1,2}));
        elseif all(tmp{1,1}=='Register C')
            regC = double(string(tmp{1,2}));
        end
    end
    line = fgetl(fileID);
    i = i+1;
end
fclose(fileID);

% %% Solve part I
% tic
% 
% programLength = numel(program);
% pointer = 0;
% output = [];
% 
% while pointer<programLength-1
%     opcode = program(pointer+1);
%     operand = program(pointer+2);
%     [pointer,regA,regB,regC,output] = adventComputer(pointer,opcode,operand,regA,regB,regC,output);
% end
% 
% outputString = '';
% for i=1:numel(output)
%     outputString = [outputString char(string(output(i))) ','];
% end
% 
% time1 = toc;

% %% Display results of part I
% out1 = sprintf('The output of the program is %s.', output);
% tim1 = sprintf('Calculation took %f seconds.', time1);
% disp(out1)
% disp(tim1)

%% Solve part II
tic 

programLength = numel(program);

regAStart = 0;
counter = 0;
output = [];

for programIndex=programLength:-1:1
    regAStart = regAStart*8;

    while 1
        output = [];
        regA = regAStart;
        regB = 0;
        regC = 0;
        
        for pointer=0:2:14
            opcode = program(pointer+1);
            operand = program(pointer+2);
            [regA,regB,regC,output] = adventComputerRegA(pointer,opcode,operand,regA,regB,regC,output,program,programIndex);
        end

        if ~(isempty(output) || output~=program(programIndex))
            break
        end

        regAStart = regAStart+1;
    end
end

result2 = regAStart+counter;

time2 = toc;

%% Display results of part II
out2 = sprintf('The program outputs itself for register A equals %d', result2);
tim2 = sprintf('Calculation took %f seconds.', time2);
disp(out2)
disp(tim2)