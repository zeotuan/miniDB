# miniDB

Super simplified relation database engine implementation for self-learning purpose

Initial plan is to create a working prototype using Python.

Next step is to implement the database in either C++ or C (To be decided).

Some module might be written in Python or Scala (leverage the development speed and easy parallelism support of these language to create a MVP)

## Feature road map (in no particular order but of course some cannot be done without the other)

- CRUD operation
  - Select
  - Update
  - Insert
  - Delete
  - Compare and Set
- Hash index
  - Static hashing
  - Extensible hashing
  - Linear hashing
- BTree index
- Cluster index
- Join
  - Nested loop join
  - Hash join
  - merge join
- Query Processer
  - Parser: parsed SQL query
  - Rewriter: Simplified written query
  - Executor: Generate execution plan
  - Optimizor
- Storage Manager
  - Data Access
  - Buffer Manager
  - Transaction Manager
  - Recovery Manager
- RepL
- XML support
- Json support
- Key constraint
  - Unique key
  - foreign key
- Transaction support + T-SQL
- Concurrency support
  - 2PL
- Distributed Query Processing
