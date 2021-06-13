#!/usr/bin/python3

def __main__() :
    cache_tx = {}
    result = []

    def mempool_tx(txid, fee, weight, parents) :
        if int(weight) < 4000000 :
            if txid in cache_tx :
                print("repeated:")
                print(txid)
            cache_tx[txid] = parents
            is_valid = parents != "" and parents in cache_tx
            if is_valid :
                result.append(txid)

    def parse_mempool_csv():
        with open('mempool.csv') as f:
            # To skip the csv headers
            next(f)
            for line in f.readlines() :
                mempool_tx(*line.strip().split(','))
    
    
    parse_mempool_csv()
    print(len(result))
    print(len(cache_tx))

if __name__ == '__main__' :
    __main__()
