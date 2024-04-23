% Facts
male(tom).
male(jim).
male(alex).
male(theo).
male(joe).
female(marry).
female(betty).
female(alice).
female(dorothy).
female(jill).

parent(alice, marry).
parent(tom, jim).
parent(betty, jim).
parent(marry, alex).
parent(tom, alex).
parent(dorothy, tom).
parent(dorothy, theo).
parent(marry, joe).
parent(tom, joe).
parent(theo, jill).

% Rules
mother(M, C) :- parent(M, C), female(M).
grandparent(GP, GC) :- parent(GP, P), parent(P, GC).
ancestor(A, D) :- parent(A, D).
ancestor(A, D) :- parent(A, D1), ancestor(D1, D).
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
cousin(X, Y) :- grandparent(G, X), grandparent(G, Y), X \= Y, \+ sibling(X, Y).
