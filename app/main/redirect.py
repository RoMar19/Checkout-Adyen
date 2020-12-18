import Adyen
import json

'''
For redirect payment methods, handle redirect back to website
For redirect methods, pull payload from form data
For 3DS payments, pull MD and PaRes from form data
Return response as dictionary to make success/failure redirect in init.py easier
'''


def handle_shopper_redirect(values):
    adyen = Adyen.Adyen()
    adyen.payment.client.platform = "test"
    adyen.client.xapikey = "AQEyhmfxKYLObRNKw0m/n3Q5qf3VaY9UCJ14XWZE03G/k2NFisuRs7z7KhB9kBC+ZOWG3q8QwV1bDb7kfNy1WIxIIkxgBw==-4HKICWIDhG8LHS5WQIjtc87Qxi+fkyN1wJo3s2XzGEU=-78wF+<p7,84eKmX;"
    
    details_request = values
    
    print("/payments/details request:\n" + str(details_request))
    
    details_response = adyen.checkout.payments_details(details_request)
    
    print("payments/details response:\n" + details_response.raw_response.decode("UTF-8"))
    return json.loads(details_response.raw_response)