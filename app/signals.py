from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

#create the function for the successful login
@receiver(user_logged_in,sender=User)
def login_successful(sender,request,user,**kwargs):
    #sender and **kwargs is mandatory parameter
    print('log in signal .......')
    print('sender',sender)
    print('reciver',user)
    print(f'kwargs:{kwargs}')

#now use .connect method manually
# user_logged_in.connect(login_successful,sender=User)
#we may use decorator instead fo the connect
#we have pass login successful as the callback function here
