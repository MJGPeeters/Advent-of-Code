function [carryIn,gates] = check_full_adder(zNum,dict,carryOut)

% Carry side
zName = sprintf('z%02d',zNum);

% Check if OR gate
carryGateOR = dict(carryOut);
carryGateOR = carryGateOR{1};
gates = string(carryOut);

if ~strcmp(carryGateOR{2},'OR')
    carryIn = 0;
    return
end

% Check if AND gate
carryGateAND1 = dict(carryGateOR{1});
carryGateAND1 = carryGateAND1{1};
gates = [gates;string(carryGateOR{1})];

if ~strcmp(carryGateAND1{2},'AND')
    carryIn = 0;
    return
end

% Check if AND gate
carryGateAND2 = dict(carryGateOR{3});
carryGateAND2 = carryGateAND2{1};
gates = [gates;string(carryGateOR{3})];

if ~strcmp(carryGateAND2{2},'AND')
    carryIn = 0;
    return
end

% If a gate is x.. AND y.., it is the AND gate connected to sum inputs
if strcmp(carryGateAND1{1}(2:3),zName(2:3))
    andCarry = carryGateAND2;
elseif strcmp(carryGateAND2{1}(2:3),zName(2:3))
    andCarry = carryGateAND1;
else
    carryIn = 0;
    return
end

% Sum side
xorOut = dict(zName);
xorOut = xorOut{1};
gates = [gates;zName];

if ~strcmp(xorOut{2},'XOR')
    carryIn = 0;
    return
end

if sort([andCarry{1},andCarry{3}])~=sort([xorOut{1},xorOut{3}])
    carryIn = 0;
    return
end

tmp1 = dict(andCarry{1});
tmp1 = tmp1{1};
tmp2 = dict(andCarry{3});
tmp2 = tmp2{1};

if strcmp(tmp1{1}(2:3),zName(2:3))
    carryIn = andCarry{3};
    gates = [gates;andCarry{1}];
elseif strcmp(tmp2{1}(2:3),zName(2:3))
    carryIn = andCarry{1};
    gates = [gates;andCarry{3}];
else
    carryIn = 0;
    return
end

end