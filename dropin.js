const {Client, Config, CheckoutAPI} = require('@adyen/api-library');
const config = new Config();
// Set your X-API-KEY with the API key from the Customer Area.
config.apiKey = '[AQEyhmfxKYLObRNKw0m/n3Q5qf3VaY9UCJ14XWZE03G/k2NFisuRs7z7KhB9kBC+ZOWG3q8QwV1bDb7kfNy1WIxIIkxgBw==-4HKICWIDhG8LHS5WQIjtc87Qxi+fkyN1wJo3s2XzGEU=-78wF+<p7,84eKmX;]';
config.merchantAccount = '[AdyenRecruitmentCOM]';
const client = new Client({ config });
client.setEnvironment("TEST");
const checkout = new CheckoutAPI(client);
const paymentsResponse = checkout.paymentMethods({ 
    merchantAccount: config.merchantAccount,
    countryCode: "NL",
    shopperLocale: "nl-NL",
    amount: { currency: "EUR", value: 1000, },
    channel: "Web"
}).then(res => res);
// Pass the response to your front end
