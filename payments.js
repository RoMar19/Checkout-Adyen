const {Client, Config, CheckoutAPI} = require('@adyen/api-library');
const config = new Config();
// Set your X-API-KEY with the API key from the Customer Area.
config.apiKey = '[AQEyhmfxKYLObRNKw0m/n3Q5qf3VaY9UCJ14XWZE03G/k2NFisuRs7z7KhB9kBC+ZOWG3q8QwV1bDb7kfNy1WIxIIkxgBw==-4HKICWIDhG8LHS5WQIjtc87Qxi+fkyN1wJo3s2XzGEU=-78wF+<p7,84eKmX;]';
config.merchantAccount = '[AdyenRecruitmentCOM]';
const client = new Client({ config });
client.setEnvironment("TEST");
const checkout = new CheckoutAPI(client);
checkout.payments({ 
    merchantAccount: config.merchantAccount,
// STATE_DATA is the paymentMethod field of an object passed from the front end or client app, deserialized from JSON to a data structure.
    paymentMethod: STATE_DATA,
    amount: { currency: "EUR", value: 1000, },
    reference: "RocioMartin_adyenrecruitment",
    returnUrl: "https://docs.adyen.com ( https://docs.adyen.com/ ) ( https://docs.adyen.com ( https://docs.adyen.com/ )/ ) ]"
}).then(res => res);
