# miniDB
Super simplified relation database engine implementation for self-learning purpose

Initial plan is to create a working prototype using Python.

Next step is to implement the database in either C++ or C (To be decided).

Some module might be written in Python or Scala (leverage the development speed and easy parallelism support of these language to create a MVP)

## Feature road map (in no particular order)

- Hash index
  - Static hashing
  - Extensible hashing
  - Linear hashing
- BTree index
- Cluster index
- Join
  - Hash join
  - merge join
- SQL syntax parser and RepL
- XML support
- Json support
- Key constraint
  - Unique key
  - foreign key
- Transaction support
- Concurrency support
  - 2PL
- Query Plan execution and optimization
- Distributed Query Processing
