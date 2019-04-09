# Sets

Set _object_ is an unordered collection of distinct hashable objects. Which means all entries in a set are unique.

## 
**Where can they be used?**
> To remove duplicates from a sequence.
> Mathematical operations such as intersection, union, difference, and symmetric difference.

> Sets support _x in set_, _len(set)_, and _for x in set_

> Being unordered collection, sets do not record elemental positions or order of insertion.
> So, Sets **do not support** _indexing_, _slicing_, or other sequence like behaviour.


### Types of Sets:
1. set
2. frozen set

**Difference between them**:

#### set:
> Set type is mutable - meaning they can be modified.

> You can use methods like _add()_, _remove()_

> _Since set is mutable it has not hash value._

> And for same reason, sets cannot be used as either _dictionary key_ or as an _element of another set_.

#### frozenset:
> frozenset is immutable - meaning they cannot be modified.

> _So it will have a hash value._

> And for this reason, we can use it as a _dictionary key_ or as an _element of another set_.