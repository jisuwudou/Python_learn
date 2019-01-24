from twilio.rest import Client
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC9a6e51be211f9a362cc8d069c6a157dc'
auth_token = 'c25c2d26aaf5d12a68a1702449431982'
client = Client(account_sid, auth_token)

# call = client.calls.create(
#                         url='http://demo.twilio.com/docs/voice.xml',
#                         to='+13380095905',
#                         from_='+16162083522',
#
#                     )
call = client.messages.create(

                        # to='+8613380095905',
                        # to='+13527752639',
                        to='+8613527891445',
                        from_='+16162083522',
                        body='test twilio',
                    )
print(call)