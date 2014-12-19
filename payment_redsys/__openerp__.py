# -*- coding: utf-8 -*-

{
    'name': 'Redsys Payment Acquirer',
    'category': 'Hidden',
    'summary': 'Payment Acquirer: Redsys Implementation',
    'version': '1.0',
    'description': """

========================
Pasarela de pago Redsys
========================


Este modulo añade la opcion de pago a traves de la pasarela de Redsys



PARAMETROS:

Nombre del comercio: Indicaremos el nombre del comercio.

Número de comercio (FUC): Indicaremos el número de comercio que

nuestra entidad nos ha comunicado.

Clave secreta de encriptación: Indicaremos la clave de encriptación

que tiene el comercio.

Número de terminal: Indicaremos el terminal del TPV.

Tipo de firma: Seleccionaremos el tipo de firma del comercio.

Tipo de moneda: Seleccionaremos la moneda de nuestro terminal TPV
(Normalmente Euros).

Tipo de transacción: Indicaremos el tipo de transacción, 0.

Idiomas TPV: Indicaremos el idiomas en el TPV.

URL_OK/URL_KO: durante el proceso del pago, y una vez que
se muestra al cliente la pantalla con el resultado del mismo, es
posible redirigir su navegador a una URL para las transacciones
autorizadas y a otra si la transacción ha sido denegada. A estas
se las denomina URL_OK y URL_KO, respectivamente. Se trata
de dos URL que pueden ser proporcionadas por el comercio.

    """,
    'author': 'Incaser Informatica S.L.',
    'depends': ['payment'],
    'data': [
        'views/redsys.xml',
        'views/payment_acquirer.xml',
        'data/redsys.xml',
    ],
    'installable': True,
}
