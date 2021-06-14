# Bitcoin Block Constructor

Given: mempool.csv with `<txid>,<fee>,<weight>,<parent_txids>` format

Output: block.txt with `<txid>` format

<br>
<br>

### Some Assumptions

1. All txids are unique and not repeated
2. Only considering tx given in the mempool set (and not before the set or after the set)
3. Miner does not have a limit on how many tx he needs to select 
4. The mempool.csv is not massive (enough to crash the system due to insufficient memory)
5. A tx is only valid if it has parents and all the parents have occurred before it

### About the Solution

1. This solution uses a hashmap implementation (for the python implementation I've used build in type dictonary),
2. A hashmap `cache_tx` stores all the txids and parent_ids as `txid: parent_ids` key pair value,
3. Since all the parents_ids should occur before the txid we check if all the parent_ids exist as a key before or not in `cache_tx`,
4. And for the O(1) lookup time we tradeoff O(n) space (which means the dictionary will fail if the mempool.csv is larger than free memory available on the system).