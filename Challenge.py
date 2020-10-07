# -*- coding: utf 8 -*-
import sys
import pyRofex
# aunque en el ejemplo no se muestra agrego el account como parametro por ser necesario para los BIDS nuevos
REMARKETS_USER = sys.argv[3]
REMARKETS_PASS = sys.argv[5]
ACCOUNT = sys.argv[5]
instrumento = sys.argv[1]
PRECIO_BASE = 75.25

try:
    print('Iniciando sesión en Remarkets')
    init = pyRofex.initialize(user=REMARKETS_USER,
                              password=REMARKETS_PASS,
                              account=ACCOUNT,
                              environment=pyRofex.Environment.REMARKET)
# separo la consulta en consulta 1 y 2 por solicitud explicita, pero podria hacerse en 1 linea.
    consulta1 = [pyRofex.MarketDataEntry.LAST]
    ultima = pyRofex.get_market_data(instrumento, consulta1, depth=1)
    assert(ultima['status'] == 'OK'), "Simbolo invalido"
    print(f"Consultando simbolo:   {instrumento}" + "\n" +
          f"Ultimo precio operado: ${ultima['marketData']['LA']['price']}")
    print("Consultando BID")

    consulta2 = [pyRofex.MarketDataEntry.BIDS]
    bid = pyRofex.get_market_data(instrumento, consulta2, depth=5)
    if len(bid['marketData']['BI']) > 0:
        ultimo_bid = bid["marketData"]["BI"][0]["price"]
        bid_nuevo = round(ultimo_bid-0.01, 2)
        print(f"Precio de BID: ${ultimo_bid}" + "\n" +
              f"Ingresando orden a: ${bid_nuevo}")

        order = pyRofex.send_order(ticker=instrumento,
                                   side=pyRofex.Side.BUY,
                                   size=1,
                                   price=bid_nuevo,
                                   order_type=pyRofex.OrderType.LIMIT)
        print("Cerrando sesión en Remarkets")
    else:
        print("No hay BID's activos"+"\n"+f"Ingresando orden a ${PRECIO_BASE}")
        order = pyRofex.send_order(ticker=instrumento,
                                   side=pyRofex.Side.BUY,
                                   size=1,
                                   price=PRECIO_BASE,
                                   order_type=pyRofex.OrderType.LIMIT)
        print("Cerrando sesión en Remarkets")
except Exception as e:
    print("Error: ", e)
    print("Cerrando sesión en Remarkets")
