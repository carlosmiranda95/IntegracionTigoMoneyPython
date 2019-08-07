from tigomoney import TigoMoneyApi

soap_url = 'https://172.16.62.187:8181/PasarelaServices_V2/CustomerServices?wsdl'
identification_key = 'f401408244902997aa56fb8c6e44a47f4d028a48f8524c938434c70addb6728dc1d7375575390ae2321b549cfc46cbc2e538dda4cdc15453df1b639b1dc577c5'
encryption_key = '9J1OJXI6QRM39WXA8GQQOQH2'

api = TigoMoneyApi(soap_url, identification_key, encryption_key)

data = {
    'pv_nroDocumento': '123456',
    'pv_orderId': 2450,
    'pv_monto': 15.5,
    'pv_linea': '69178351',
    'pv_nombre': 'Jorge Moreira',
    'pv_urlCorrecto': '',
    'pv_urlError': '',
    'pv_confirmacion': 'Gracias por su compra',
    'pv_notificacion': 'Orden: 2450',
    'pv_items': '*i1|1|Producto 1|15.50|15.50',
    'pv_razonSocial': 'Linkux It',
    'pv_nit': '0'
}

# Pago sincrono
response = api.call('solicitarPago', **data)

print response

# Pago Asincrono
# api.call('solicitarPagoAsincrono', **data)

# Consulta de Transaccion
# api.call('consultarEstado', 'ID_TRANSACCION')
