nota(joao,5.0).
nota(maria,6.0).
nota(joana,8.0).
nota(mariana,9.0).
nota(cleuza,8.5).
nota(jose,6.5).
nota(jaoquim,4.5).
nota(mara,4.0).
nota(mary,10.0).

verify_student(X, aprovado) :- nota(X,Y), Y >= 7.0, Y =< 10.0.
verify_student(X, recuperação) :- nota(X,Y), Y >= 5.0, Y =< 6.9 .
verify_student(X, reprovado) :- nota(X,Y),Y >= 0.0 ,Y =< 4.9 .

