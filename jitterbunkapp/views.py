from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from jitterbunkapp.models import Bunk, User
from jitterbunkapp.forms import BunkForm
from datetime import datetime


def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details,
    # for example.
    context = RequestContext(request)

    bunk_list = Bunk.objects.all().order_by('id')

    # Construct a dictionary to pass to the template engine as its context.
    context_dict = {'bunk_list': bunk_list}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    return render_to_response('jitterbunkapp/index.html',
                              context_dict, context)


def userpage(request, user_id):
    # Request the context of the request.
    # The context contains information such as the client's machine details,
    # for example.
    context = RequestContext(request)

    # Get user data from db
    user = get_object_or_404(User, id=user_id)

    # Get all bunks including this user
    # https://docs.djangoproject.com/en/1.6/topics/db/queries/#complex-lookups-with-q-objects
    bunk_list = user.bunks_to_user.all() | user.bunks_from_user.all()
    bunk_list = bunk_list.order_by('id')

    # Construct a dictionary to pass to the template engine as its context.
    context_dict = {'user': user, 'bunk_list': bunk_list}

    # Return a rendered response to send to the client.
    return render_to_response('jitterbunkapp/userpage.html',
                              context_dict, context)


def add_bunk(request, user_id):
    # Get the context from the request
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        form = BunkForm(request.POST)
        # check if form is valid
        if form.is_valid():
            # save the new bunk
            form.save(commit=True)
            # call the userpage view
            return userpage(request, user_id)
        else:
            # for debugging, may want to provide info to user
            print form.errors
    else:
        form = BunkForm(initial={'from_user': user_id, 'time': datetime.now()})
        form.fields['to_user'].queryset = User.objects.exclude(id=user_id)

    context_dict = {'form': form}
    return render_to_response('jitterbunkapp/add_bunk.html', context_dict,
                              context)
