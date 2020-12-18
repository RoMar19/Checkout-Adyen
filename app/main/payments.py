import Adyen
from random import randint
from flask import json

'''
perform a call to /payments
Taking in the following object from our frontend_request. billingAddress and browserInfo only sent for cards
	{
		paymentMethodData: {
			type: "scheme",
			encryptedCardNumber: "adyenjs_0_1_25$DQ3JeLb...,
			encryptedExpiryMonth: "adyenjs_0_1_25$B1JSCp...,
			encryptedExpiryYear: "adyenjs_0_1_25$h86PBBe...,
			encryptedSecurityCode: "adyenjs_0_1_25$hrwG6...,
			holderName: "Joe Bob"
		},
		billingAddress: {
			street: "Brannan Street",
			city: "San Francisco",
			stateOrProvince: "California",
			postalCode: "94107",
			country: "US",
			houseNumberOrName: 274
		},
		browserInfo: {
			acceptHeader: "*/*",
			colorDepth: 24,
			language: "en-US",
			javaEnabled: false,
			screenHeight: 1440,
			screenWidth: 2560,
			userAgent: "Mozilla/5.0...,
			timeZoneOffset: 480
		}
	};
	
Will use this as the base of our payment request and add the necessary components from our backend. Feel free to modify
these values in the frontend adyen_implementations.js file or to override them here
Returns JSON representation of response
'''


def adyen_payments(frontend_request):
	adyen = Adyen.Adyen()
	adyen.client.platform = 'test'
	adyen.client.xapikey = 'AQEyhmfxKYLObRNKw0m/n3Q5qf3VaY9UCJ14XWZE03G/k2NFisuRs7z7KhB9kBC+ZOWG3q8QwV1bDb7kfNy1WIxIIkxgBw==-4HKICWIDhG8LHS5WQIjtc87Qxi+fkyN1wJo3s2XzGEU=-78wF+<p7,84eKmX;'
	
	payment_info = frontend_request.get_json()
	txvariant = payment_info["paymentMethod"]["type"]
	
	payments_request = {
		'amount': {
			'value': 1000,
			'currency': choose_currency(txvariant)
		},
		'channel': 'Web',
		'reference': 'RocioMartin_adyenrecruitment' + str(randint(0, 10000)),
		'shopperReference': "Python Checkout Shopper",
		'returnUrl': "https://docs.adyen.com ( https://docs.adyen.com/ ) ( https://docs.adyen.com ( https://docs.adyen.com/ )/ ) ]",
		'countryCode': 'NL',
		'shopperLocale': "en_US",
		'storePaymentMethod': 'true',
		'merchantAccount': AdyenRecruitmentCOM
	}
	payments_request.update(payment_info)
	
	if txvariant == 'alipay':
		payments_request['countryCode'] = 'CN'
	
	elif 'klarna' in txvariant:
		payments_request['shopperEmail'] = "myEmail@adyen.com"
		payments_request['lineItems'] = [
			{
				'quantity': "1",
				'amountExcludingTax': "450",
				'taxPercentage': "1111",
				'description': "Sunglasses",
				'id': "Item #1",
				'taxAmount': "50",
				'amountIncludingTax': "500",
				'taxCategory': "High"
			},
			{
				'quantity': "1",
				'amountExcludingTax': "450",
				'taxPercentage': "1111",
				'description': "Headphones",
				'id': "Item #2",
				'taxAmount': "50",
				'amountIncludingTax': "500",
				'taxCategory': "High"
			}]
	elif txvariant == 'directEbanking' or txvariant == 'giropay':
		payments_request['countryCode'] = "DE"
	
	elif txvariant == 'dotpay':
		payments_request['countryCode'] = "PL"
	
	elif txvariant == 'scheme':
		payments_request['additionalData'] = {"allow3DS2": "true"}
		payments_request['origin'] = "http://localhost:8080"
	
	elif txvariant == 'ach' or txvariant == 'paypal':
		payments_request['countryCode'] = 'US'
	
	print("/payments request:\n" + str(payments_request))
	
	payments_response = adyen.checkout.payments(payments_request)
	
	print("/payments response:\n" + payments_response.raw_response.decode("UTF-8"))
	return remove_unnecessary_data(payments_response.raw_response)


def choose_currency(payment_method):
	if payment_method == "alipay":
		return "CNY"
	elif payment_method == "dotpay":
		return "PLN"
	elif payment_method == "boletobancario":
		return "BRL"
	elif payment_method == "ach" or payment_method == "paypal":
		return "USD"
	else:
		return "EUR"


# Custom payment error class
class PaymentError(Exception):
	def __init__(self, value):
		self.value = value
	
	def __str__(self):
		return repr(self.value)
	

# Format response being passed back to frontend. Only leave resultCode and action
def remove_unnecessary_data(response):
	dict_response = json.loads(response)
	if "resultCode" in dict_response:
		new_response = {"resultCode": dict_response["resultCode"]}
		if "action" in dict_response:
			new_response["action"] = dict_response["action"]
		return json.dumps(new_response)
	else:
		raise PaymentError(response)
