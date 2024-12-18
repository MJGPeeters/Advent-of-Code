function [pointer,regA,regB,regC,output,programIndex,viable] = adventComputerRegA(pointer,opcode,operand,regA,regB,regC,output,program,programIndex,viable)

comboOperands = [0,1,2,3,regA,regB,regC];

if opcode==0 %ADV
    regA = floor(regA/2^comboOperands(operand+1));
elseif opcode==1 %BXL
    regB = bitxor(regB,operand);
elseif opcode==2 %BST
    regB = mod(comboOperands(operand+1),8);
elseif opcode==3 %JNZ
    if regA~=0
        pointer = operand;
        return
    end
elseif opcode==4 %BXC
    regB = bitxor(regB,regC);
elseif opcode==5 %OUT
    output = [output mod(comboOperands(operand+1),8)];
    if output(end)~=program(programIndex)
        viable = 0;
    else
        programIndex = programIndex+1;
    end
elseif opcode==6 %BDV
    regB = floor(regA/2^comboOperands(operand+1));
elseif opcode==7 %CDV
    regC = floor(regA/2^comboOperands(operand+1));
end

pointer = pointer+2;

end