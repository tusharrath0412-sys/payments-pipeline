def failure_rate(total_txn, failed_txn):
    if total_txn == 0:
        return 0
    return round((failed_txn/total_txn) * 100, 2)