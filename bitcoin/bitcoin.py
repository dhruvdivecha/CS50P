import requests
import sys

if len(sys.argv) == 2:
    value = float(sys.argv[1])

else:
    print("Enter a number")
    sys.exit(1)

try:
    price = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    response = price.json()
    bitcoin = (response['bpi']['USD']['rate_float'])
    total_amount = bitcoin * value
    print(f"${total_amount:,.4f}")

except requests.RequestException:
    print("RequestException")
    sys.exit(1)

