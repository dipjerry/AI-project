parent(john, jim).
parent(john, ann).
parent(mary, ann).
parent(mary, jim).

grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
