# LMDB module for node and backendjs

# Usage

## Env class
 - `new Env(options)` - create new environment
 - The options properties:
   - path - the database file path
   - flags - bitmask of LMDB_ flags
   - dbs - number of databases
## Database class
- `new Database(env, options, callback)` - create new database object
- Properties:
  - open - 1 if the db is open
  - name - the database file name
- Methods:
  - close - close the database
  - drop - drop the database file
  - get(key, callback) - return value for the given key
  - put(key, value [, flags] [, callback]) - store a value for the given key
  - incr(key, num [, flags] [, callback]) - increment a value by a number
  - del(key [, value] [,callback]) - delete a key
  - select(start, end [,flags] [, callback]) - return list of matching records
    The flags are:
     - desc - 1 to return in descendent order
     - begins_with - 1 if match by beginning of the start key
     - count - number of records to return

# Author

Vlad Seryakov

