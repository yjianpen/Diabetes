%
%% loop hints
%Ga = max(0, G_A - G);
%Gi = max(0, G - G_I);
%Gr = max(0, G - G_0);
%Ar = max(0, A - A_0);
%Ir = max(0, I - I_0);
%
%
%
%dG = - X*G + alpha*A*Ga + E(t)*Gr + beta*F(t);
%dI = -d_I*Ir + gamma_I*Gi;
%dX = -d_X*X + gamma_X*Ir;
%dA = -d_A*Ar + gamma_A*Ga;
%
%G = G + dG;
%I = I + dI;
%X = X + dX;
%A = A + dA;
%
1;
% main


function Fsingle = SingleMeal(GI, Carb)
  % Assumption: Carb is digested by GI% per hour.
  Fsingle = [];
  C = Carb;
  while C > 0
    d = min(Carb*GI/100/60, C);
    C = C - d;
    Fsingle(end+1) = d; 
  end
end

function F = Intake(meal)
  % meal = [ [GI_1, Carb_1]; [GI_2, Carb_2]; [GI_3, Carb_3]];
  F = zeros(1, 1440);
  T = [0, 240, 600] .+ 1;
  for i = 1:3
    Fsingle = SingleMeal(meal(i,1), meal(i, 2));
    F(T(i):T(i)-1 + length(Fsingle)) = F(T(i):T(i)-1 + length(Fsingle)) + Fsingle;
  end
end

% Delta t = 1 min; T(1) = 8:00 am.
T = 1:48*60; 

% Exercise.  Sleep during 10pm ~ 7 pm
E = [ones(1,840), zeros(1, 1380-840), ones(1, 60)]; % awake = 1; rest = 0
% 8:00 ~ 22:00; 22:00 ~ 7:00; 7:00 ~ 8:00



p1 = 2.96/100;
p0 = 2.96/100;
E = p0*~E + p1*E; % p0 = rest/sleep, p1 = active/awake


meal = [70, 40; 52, 55; 69, 60]; % I made this up

F = Intake(meal); % food

 % TODO
 % 
 %  - write loops
 %
 %  - test parameters:
 %      alpha:           effeciency of glucagon raising glucose
 %      beta:            intake effeciency of food glucose
 %      d_{I, X, A}:     degradation rate of {I, X, A}
 %      gamma_{I, X, A}: secretion rate of {I, X, A}
 %      
 %      
 %      
 %      
 %      
 %
 
% from bergmann
d_X = 0.0086; % p2
gamma_X = 6.51e-6; % p3
d_I = 0.23; % n
G_I = 100; % h
G_0 = 120;
G_A = 200;
I_0 = 5;
gamma_I = 5.36*10^(-3);

beta = 1;

% no glucagon
alpha = 1e-4;
d_A = d_I;
gamma_A = 1.5*gamma_I;
A_0 = 5;

% start
I = 6;
G = 126;
A = 8;
X = 6e-4;

R = zeros(24*60, 4);
R(1,:) = [G, I, X, A];

% 1st day: all resting
for t = 2:24*60
  Ga = max(0, G_A - G);
Gi = max(0, G - G_I);
Gr = max(0, G - G_0);
Ar = max(0, A - A_0);
Ir = max(0, I - I_0);



dG = - X*G + alpha*A*Ga - E(t)*Gr + beta*F(t);
dI = -d_I*Ir + gamma_I*Gi;
dX = -d_X*X + gamma_X*Ir;
dA = -d_A*Ar + gamma_A*Ga;

G = G + dG;
I = I + dI;
X = X + dX;
A = A + dA;

R(t,:) = [G, I, X, A];
end

% 2nd day: active during 7~22
E([1:840, 1381:1440]) = p1*2;
for t = 1:24*60
  Ga = max(0, G_A - G);
Gi = max(0, G - G_I);
Gr = max(0, G - G_0);
Ar = max(0, A - A_0);
Ir = max(0, I - I_0);



dG = - X*G + alpha*A*Ga - E(t)*Gr + beta*F(t);
dI = -d_I*Ir + gamma_I*Gi;
dX = -d_X*X + gamma_X*Ir;
dA = -d_A*Ar + gamma_A*Ga;

G = G + dG;
I = I + dI;
X = X + dX;
A = A + dA;

R(24*60+t,:) = [G, I, X, A];
end

xtl = {'8',' ',' ',' ','12',' ',' ','15',' ',' ','18',' ',' ','21',' ',' ','24',' ',' ',' ',' ',' ',' ',' ','8'}
xtl = [xtl xtl{2:end}]; %dual

subplot(2,2,1)
plot(T, R(:, 1),[0; 50*60], [G_0; G_0])
set(gca,'XTick',0:60:2880, 'XTicklabel', xtl)
xlim([0, 50*60])
legend({'G', 'G_0'})
title('Glucose')

subplot(2,2,2)
plot(T, R(:, 2), [0; 50*60], [I_0; I_0])
set(gca,'XTick',0:60:2880, 'XTicklabel', xtl)
xlim([0, 50*60])
legend({'I', 'I_0' })
title('Insulin')

subplot(2,2,3)
plot(T, R(:, 3))
set(gca,'XTick',0:60:2880, 'XTicklabel', xtl);
xlim([0, 50*60])
title('X')

subplot(2,2,4)
plot(T, R(:, 4),[0; 50*60], [A_0; A_0])
set(gca,'XTick',0:60:2880, 'XTicklabel', xtl);
xlim([0, 50*60])
legend({'A', 'A_0' })
title('Glucagon')
