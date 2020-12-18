import Adyen

'''
perform a call to /payments/details
Passing in the component state.data object as frontend_request, This looks like the following:
    {
        details: {
            "threeds2.fingerprint/challengeResult" : "eyJ0aHJlZURTQ29tcEluZCI6IlkifQ==""
        }
        paymentData : "Ab02b4c0!BQABAgB/3ckQEAf5YOdAT83NDjdf+AR4hmjf1fohm2Q8gSe95qb6hE3+GnxfBaK..."
    }
'''


def get_payment_details(frontend_request):
    adyen = Adyen.Adyen()
    adyen.payment.client.platform = "test"
    adyen.client.xapikey = "AQEyhmfxKYLObRNKw0m/n3Q5qf3VaY9UCJ14XWZE03G/k2NFisuRs7z7KhB9kBC+ZOWG3q8QwV1bDb7kfNy1WIxIIkxgBw==-4HKICWIDhG8LHS5WQIjtc87Qxi+fkyN1wJo3s2XzGEU=-78wF+<p7,84eKmX;"
    
    details_request = frontend_request.get_json()
    
    print("/payments/details request:\n" + str(details_request))
    
    details_response = adyen.checkout.payments_details(details_request)

    print("payments/details response:\n" + details_response.raw_response.decode("UTF-8"))
    return details_response.raw_response