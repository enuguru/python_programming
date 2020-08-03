


tuples are immutable lists, frozensets are immutable sets.

tuples are indeed an ordered collection of objects, but they can contain 
duplicates and unhashable objects, and have slice functionality

frozensets aren't indexed, but you have the functionality of sets - O(1) element 
lookups, and functionality such as unions and intersections. They also can't 
contain duplicates, like their mutable counterparts.
``
