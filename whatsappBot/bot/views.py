from django.shortcuts import render,HttpResponse
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt

account_sid = 'ACcdb78f04488ae9429c5ffd0be6430456'
auth_token = 'ae6eb124e22169ad73cca86ccde37090'
client = Client(account_sid, auth_token)

@csrf_exempt
def bot(request):
    # message= request.POST["message"]
    print(request.POST)

    # if message == "hi":
    #     client.messages.create(
    #     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
    #     from_='+15017122661',
    #     to='+15558675310'
    # )

    return HttpResponse("hello")