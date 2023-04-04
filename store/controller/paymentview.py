from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import stripe

# stripe.api_key = 'sk_test_51MrhFfSHZAJJXMruYFXUPbEM3Edu1WmjQ0BszczBCkfpqiZigNPKMAwQUrjDNs2nBUJLKNOcQ3GjNNjUr5Q3hGdG00R7bYLdM2'
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def charge(request):
    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
        amount = int(request.POST['amount'])
        token = request.POST['stripeToken']

        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                description='Payment',
                source=token
            )
            return redirect('success')
        except stripe.error.CardError as e:
            return render(request, 'payment.html', {'error': e})
    return render(request, 'payment.html')

def success(request):
    return render(request,'store/success.html')
