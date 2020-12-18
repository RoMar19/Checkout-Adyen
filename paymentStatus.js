// Show a success message
dropin.setStatus('success');
dropin.setStatus('success', { message: 'Payment successful!' });
 
// Show an error message
dropin.setStatus('error');
dropin.setStatus('error', { message: 'Something went wrong.'});
 
// Set a loading state
dropin.setStatus('loading'); // start the loading state
dropin.setStatus('ready'); // set back to the initial state