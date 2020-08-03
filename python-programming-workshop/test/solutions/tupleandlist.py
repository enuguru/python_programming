

The key difference is that tuples are immutable. This means that 
you cannot change the values in a tuple once you have created it.

So if you're going to need to change the values use a List.

Benefits to tuples:

Slight performance improvement.

As a tuple is immutable it can be used as a key in a dictionary.

If you can't change it neither can anyone else, which is to say you 
don't need to worry about any API functions etc. changing your tuple 
without being asked.




Lists are for looping, tuples are for structures i.e. "%s %s" %tuple.

Lists are usually homogeneous, tuples are usually heterogeneous.

Lists are for variable length, tuples are for fixed length.



If you went for a walk, you could note your coordinates at any instant 
in an (x,y) tuple.

If you wanted to record your journey, you could append your location 
every few seconds to a list.

But you couldn't do it the other way around.
