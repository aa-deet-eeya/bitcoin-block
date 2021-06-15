#!/usr/bin/python3

from datetime import datetime

cache_tx = {}
cache_result = []
result = []
max_weight = 4000000
        
def mempool_tx(txid, fee, weight, parents_ids) :
    try :
        global cache_result
        cache_tx[txid] = { 'fee': fee, 'weight': weight }
        # To check if the tx is valid or not
        is_valid = parents_ids == "" or all(parent in cache_tx for parent in parents_ids.split(';'))
        if is_valid:
            cache_result.append({ 'tx': txid, 'weight': int(weight),'index': len(cache_result), 'ratio': int(fee)/int(weight) });
            
    except ValueError as error:
        print('Error occured:', error)
    
def parse_mempool_csv():
    try :
        with open('mempool.csv') as mempool_file :# , open('block.txt', 'w') as result_file :
            
            # To skip the csv headers
            next(mempool_file)
            for line in mempool_file.readlines() :
                # result = 
                mempool_tx(*line.strip().split(','))
                
                # if result :
                #     result_file.write(result + '\n')
    except IOError as error:
        print('Error: ', error)


def writeFinalResult() :
    # try :
    total_wt = 0
    required_index = 0

    # Sort the List based on the Ratio and choose the first X
    # transactions who have toatal weight combined under 4mil
    cache_result.sort(key=lambda x: x['ratio'], reverse=True)
    for tx in cache_result :
        total_wt += tx['weight']
        if total_wt > max_weight :
            break
        required_index +=1

    # Slice the cache_result list with only the required tx which
    # have a total weight under 4mil and sort it back according to
    # their index and write to the block.txt file
    cache_result[0:required_index+1]
    cache_result.sort(key=lambda x: x['index'], reverse=False)

    with open('block.txt', 'w') as result_file :
        for tx in cache_result :
            result_file.write(tx['tx'] + '\n')

    # except IOError as error:
    #     print('Error: ', error)
            

def __main__() :
    parse_mempool_csv()

    # start = datetime.now()
    writeFinalResult()
    # print("Time Taken: ", datetime.now()-start)

if __name__ == '__main__' :
    __main__()
