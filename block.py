#!/usr/bin/python3

def __main__() :
    cache_tx = {}
    result = []

    def mempool_tx(txid, fee, weight, parents_ids) :
        try :
            if int(weight) < 4000000 :
                if txid in cache_tx :
                    print("repeated:")
                    print(txid)
                cache_tx[txid] = parents_ids

                # To check if the tx is valid or not
                is_valid = parents_ids != "" and all(parent in cache_tx for parent in parents_ids.split(';'))
                if is_valid :
                    result.append(txid)
        except ValueError as error:
            print('Error occured:', error)


    def parse_mempool_csv():
        try :
            with open('mempool.csv') as f:
                # To skip the csv headers
                next(f)
                for line in f.readlines() :
                    mempool_tx(*line.strip().split(','))
        except IOError as error:
            print('Error: ', error)

    
    parse_mempool_csv()
    print(len(result))

if __name__ == '__main__' :
    __main__()
