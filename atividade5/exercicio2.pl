remover([X|L2],X,L2).
remover([X1|L2],X,[X1|L1]) :- remover(L2,X,L1).