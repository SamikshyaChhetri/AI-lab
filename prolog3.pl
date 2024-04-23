% Facts
male(chhetri).
male(prasun).
male(medani).
female(kamala).
female(bimala).
female(samikshyaa).

parent(medani, chhetri).
parent(bimala, chhetri).
parent(chhetri, samikshya).
parent(chhetri, prasun).
parent(kamala, samikshya).
parent(kamala, prasun).

% Rules
mother(M, C) :- parent(M, C), female(M).
father(F, C) :- parent(F, C), male(F).
sibling(S, C) :- parent(P, C), parent(P, S), S \= C.
grandparent(GP, GC) :- parent(GP, X), parent(X, GC).
ancestor(A, D) :- parent(A, D).
