import os

def populate():
    user0 = add_user("John")
    user1 = add_user("Kyle")
    user2 = add_user("Vanessa")
    user3 = add_user("Laura")
    user4 = add_user("Jackie")

    #user bunking self? should this be allowed?
    add_bunk(user0,user0)
    #John->Kyle
    add_bunk(user0,user1)
    #Kyle->John
    add_bunk(user1,user0)
    #Jackie->Laura
    add_bunk(user4,user3)
    #Vanessa->Laura
    add_bunk(user2,user3)

    # Print out what we have added to the user.
    for b in Bunk.objects.all():
        print(b)

def add_bunk(from_user, to_user):
    b = Bunk.objects.get_or_create(from_user=from_user,to_user=to_user)[0]
    return b

def add_user(name):
    u = User.objects.get_or_create(username=name)[0]
    return u

# Start execution here!
#By doing the main check, you can have that code only execute
#when you want to run the module as a program and not have it
#execute when someone just wants to import your module and call
#your functions themselves
if __name__ == '__main__':
    print "Starting Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jitterbunk.settings')
    from jitterbunkapp.models import Bunk, User
    populate()

