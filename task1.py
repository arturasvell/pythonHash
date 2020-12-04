from bitcoin.rpc import RawProxy

p=RawProxy()

txid=raw_input("Write transaction id:")



raw_tx=p.getrawtransaction(txid)

decoded_tx=p.decoderawtransaction(raw_tx)

output=0

for i in decoded_tx['vout']:
        output+=i['value']
print(txid)

value_first=0

for value in decoded_tx['vin']:
        value_txid=value['txid']
        value_result=value['vout']

        value_tx=p.getrawtransaction(value_txid)
        decoded_value_tx=p.decoderawtransaction(value_tx)
        value_first+=decoded_value_tx['vout'][value_result]['value']

txfee=value_first-output
print(txfee)
