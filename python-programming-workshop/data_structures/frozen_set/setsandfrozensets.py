
Set Types -- set, frozenset

A set object is an unordered collection of immutable values. Common uses include 
membership testing, removing duplicates from a sequence, and computing mathematical 
operations such as intersection, union, difference, and symmetric difference. 
New in version 2.4.

Like other collections, sets support x in set, len(set), and for x in set. 
Being an unordered collection, sets do not record element position or order of 
insertion. Accordingly, sets do not support indexing, slicing, or other 
sequence-like behavior.

There are currently two builtin set types, set and frozenset. The set type is 
mutable -- the contents can be changed using methods like add() and remove(). 
Since it is mutable, it has no hash value and cannot be used as either a dictionary 
key or as an element of another set. The frozenset type is immutable and hashable -- 
its contents cannot be altered after is created; however, it can be used as a 
dictionary key or as an element of another set.

Instances of set and frozenset provide the following operations:

Operation 	Equivalent 	Result
len(s) 		cardinality of set s
x in s 		test x for membership in s
x not in s 		test x for non-membership in s
s.issubset(t) 	s <= t 	test whether every element in s is in t
s.issuperset(t) 	s >= t 	test whether every element in t is in s
s.union(t) 	s | t 	new set with elements from both s and t
s.intersection(t) 	s & t 	new set with elements common to s and t
s.difference(t) 	s - t 	new set with elements in s but not in t
s.symmetric_difference(t) 	s ^ t 	new set with elements in either 
                                s or t but not both
s.copy() 		new set with a shallow copy of s

Note, the non-operator versions of union(), intersection(), difference(), 
and symmetric_difference(), issubset(), and issuperset() methods will accept 
any iterable as an argument. In contrast, their operator based counterparts 
require their arguments to be sets. This precludes error-prone constructions 
like set('abc') & 'cbs' in favor of the more readable set('abc').intersection('cbs').

Both set and frozenset support set to set comparisons. Two sets are equal if and only if every element of each set is contained in the other (each is a subset of the other). A set is less than another set if and only if the first set is a proper subset of the second set (is a subset, but is not equal). A set is greater than another set if and only if the first set is a proper superset of the second set (is a superset, but is not equal).

Instances of set are compared to instances of frozenset based on their members. 
For example, "set('abc') == frozenset('abc')" returns True.

The subset and equality comparisons do not generalize to a complete ordering function. 
For example, any two disjoint sets are not equal and are not subsets of each other, 
so all of the following return False: a<b, a==b, or a>b. Accordingly, sets do not 
implement the __cmp__ method.

Since sets only define partial ordering (subset relationships), the output of the 
list.sort() method is undefined for lists of sets.

Set elements are like dictionary keys; they need to define both __hash__ and 
__eq__ methods.

Binary operations that mix set instances with frozenset return the type of the first 
operand. For example: "frozenset('ab') | set('bc')" returns an instance of frozenset.

The following table lists operations available for set that do not apply to 
immutable instances of frozenset:

Operation 	         Equivalent 	Result
s.update(t) 	     s |= t 	       update set s, adding elements from t
s.intersection_update(t) 	s &= t 	update set s, keeping only elements found in both s and t
s.difference_update(t) 	s -= t 	update set s, removing elements found in t
s.symmetric_difference_update(t) 	s ^= t 	update set s, keeping only elements found in either s or t but not in both
s.add(x) 		add element x to set s
s.remove(x) 		remove x from set s; raises KeyError if not present
s.discard(x) 		removes x from set s if present
s.pop() 		remove and return an arbitrary element from s; raises KeyError if empty
s.clear() 		remove all elements from set s

Note, the non-operator versions of the update(), intersection_update(), difference_update(), and symmetric_difference_update() methods will accept any iterable as an argument.

The design of the set types was based on lessons learned from the sets module. 
