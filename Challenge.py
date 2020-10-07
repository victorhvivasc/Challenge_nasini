# -*- coding: utf 8 -*-
import sys
import pyRofex

# aunque en el ejemplo no se muestra agrego el account como parametro por ser necesario para los BIDS nuevos
# tambien se agrega verificación minima de parametros ingresaados junto con correccion asistida de los mismos

try:
    instrumento = sys.argv[1]
    REMARKETS_USER = sys.argv[3] if sys.argv[2] == "-u" else input('Ingrese el usuario por favor: ')
    REMARKETS_PASS = sys.argv[5] if sys.argv[4] == "-p" else input('Ingrese la contraseña por favor: ')
    ACCOUNT = sys.argv[7] if sys.argv[6] == "-a" else input('Ingrese la cuenta a utilizar por favor: ')
    PRECIO_BASE = 75.25
except Exception as e:
    print("Por favor configure el comando con el siguiente formato: \n \n "
          ">>>python challenge.py -u NOMBRE_USUARIO -p CONTRASEÑA -a CUENTA\n \n")

try:
    print('Iniciando sesión en Remarkets')
    init = pyRofex.initialize(user=REMARKETS_USER,
                              password=REMARKETS_PASS,
                              account=ACCOUNT,
                              environment=pyRofex.Environment.REMARKET)
# separo la consulta en consulta 1 y 2 por solicitud explicita, pero podria hacerse en 1 linea.
    consulta1 = [pyRofex.MarketDataEntry.LAST]
    ultima = pyRofex.get_market_data(instrumento, consulta1, depth=1)

    # La API verifica la cuenta pero no el instrumento en esta instancia por eso agrego el assert
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

        # En caso de que la cuenta suministrada sea incongruente con los datos se eleva este error
        assert(order["status"] == "OK"), "No se pudo concretar la orden, fallo en la cuenta suministrada"
        print("Orden Completada")
        print("Cerrando sesión en Remarkets")
    else:
        print("No hay BID's activos"+"\n"+f"Ingresando orden a ${PRECIO_BASE}")
        order = pyRofex.send_order(ticker=instrumento,
                                   side=pyRofex.Side.BUY,
                                   size=1,
                                   price=PRECIO_BASE,
                                   order_type=pyRofex.OrderType.LIMIT)
        assert (order["status"] == "OK"), "No se pudo concretar la orden, fallo en la cuenta suministrada"
        print("Orden Completada")
        print("Cerrando sesión en Remarkets")
except Exception as e:
    print("Error: ", e)
    print("Cerrando sesión en Remarkets")
