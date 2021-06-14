#!/usr/bin/python3


def __main__() :
    cache_tx = {}
    
    def mempool_tx(txid, fee, weight, parents_ids) :
        try :
            if int(weight) < 4000000 :
                cache_tx[txid] = parents_ids

                # To check if the tx is valid or not
                is_valid = parents_ids != "" and all(parent in cache_tx for parent in parents_ids.split(';'))
                if is_valid :
                    return txid
                
        except ValueError as error:
            print('Error occured:', error)
    
    def parse_mempool_csv():
        try :
            with open('mempool.csv') as mempool_file, open('block.txt', 'w') as result_file :
                # To skip the csv headers
                next(mempool_file)
                for line in mempool_file.readlines() :
                    result = mempool_tx(*line.strip().split(','))
                    
                    if result :
                        result_file.write(result + '\n')
                    
        except IOError as error:
            print('Error: ', error)

    
    parse_mempool_csv()

if __name__ == '__main__' :
    __main__()
