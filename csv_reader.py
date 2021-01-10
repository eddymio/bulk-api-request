import csv


# person_id, person_name, trade_amount, trade_type, date_of_trade
def read_csv(path='data.csv'):
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        all_data = []
        for row in csv_reader:
            # we do skip the header line
            if line_count > 0:
                all_data.append({
                    'personId': row[0],
                    'personName': row[1],
                    'tradeAmount': row[2],
                    'tradeType': row[3],
                    'dateOfTrade': row[4]
                })
            line_count += 1
        return all_data


if __name__ == '__main__':
    data = read_csv('data.csv')
    for trade in data:
        print(f'\tPerson id : { trade.get("personId") }, Person name : { trade.get("personName") }, Trade amount : { trade.get("tradeAmount") }, Trade type : { trade.get("tradeType") }, Trade date : { trade.get("dateOfTrade") }')
