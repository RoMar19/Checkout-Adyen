import Adyen
import json


'''
Retrieve available payment methods by calling /paymentMethods
Request only needs to include merchantAccount, but you can include more information to get a more refined response
Should have a payment state on your server from which you can fetch information like amount and shopperReference
'''


def adyen_payment_methods():
    adyen = Adyen.Adyen()
    adyen.client.platform = 'test'
    adyen.client.xapikey = 'AQEyhmfxKYLObRNKw0m/n3Q5qf3VaY9UCJ14XWZE03G/k2NFisuRs7z7KhB9kBC+ZOWG3q8QwV1bDb7kfNy1WIxIIkxgBw==-4HKICWIDhG8LHS5WQIjtc87Qxi+fkyN1wJo3s2XzGEU=-78wF+<p7,84eKmX;'

    payment_methods_request = {
        'merchantAccount': "AdyenRecruitmentCOM",
        'reference': 'RocioMartin_adyenrecruitment',
        'shopperReference': 'Python Checkout Shopper',
        'channel': 'Web',
    }
    
    print("/paymentMethods request:\n" + str(payment_methods_request))

    payment_methods_response = adyen.checkout.payment_methods(payment_methods_request)
    formatted_response = json.dumps((json.loads(payment_methods_response.raw_response)))
    
    print("/paymentMethods response:\n" + formatted_response)
    return formatted_response


# def filter_unsupported_methods(adyen_result):
#     pm_dict = json.loads(adyen_result.raw_response)
#     pm_dict["paymentMethods"] = [value for value in pm_dict["paymentMethods"] if value["type"] in config.supported_integrations or value["type"] == "scheme"]
#     new_string = json.dumps(pm_dict)
#     return new_string



