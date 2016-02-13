def get_currency_rate(currency_list):

# get currency exchange rate from Web
    import urllib2
    s = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%3D%22USDBYR%2CEURBYR%2CBYRRUB%22&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'
    u = urllib2.urlopen(s)
    u.getcode()
    data = u.read()

# parse json

    import json
    parsed_data = json.loads(data)

    l_rates_ws = parsed_data['query']['results']['rate']

    d_rates = {}

    for rate in l_rates_ws:
        d_rates[rate['id']] = rate['Rate']

# save useful info to dictionary

    res_data = {}

    for currency in currency_list:
        if currency in d_rates:
            res_data[currency] = d_rates[currency]
        else:
            res_data[currency] = 'Note found'

    return res_data

print(get_currency_rate(['BYRUSD', 'BYREUR', 'USDBYR']))