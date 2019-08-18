from db_tools.data.product_data import row_data

for i in range(len(row_data)):
    del row_data[i]['market_price']
    del row_data[i]['goods_desc']
    row_data[i]['price'] = row_data[i].get('sale_price')
    del row_data[i]['sale_price']
print(row_data)