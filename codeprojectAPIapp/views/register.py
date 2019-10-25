import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.db import IntegrityError
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from codeprojectAPIapp.models import Coder


@csrf_exempt
def login_user(request):
    '''Handles the authentication of a user

    Method arguments:
      request -- The full HTTP request object
    '''

    req_body = json.loads(request.body.decode())

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':

        # Use the built-in authenticate method to verify
        username = req_body['username']
        password = req_body['password']
        authenticated_user = authenticate(username=username, password=password)

        # If authentication was successful, respond with their token
        if authenticated_user is not None:
            token = Token.objects.get(user=authenticated_user)
            data = json.dumps({"valid": True, "token": token.key})
            return HttpResponse(data, content_type='application/json')

        else:
            # Bad login details were provided. So we can't log the user in.
            data = json.dumps({"valid": False})
            return HttpResponse(data, content_type='application/json')


@csrf_exempt
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''
    # try:
    
    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    #Check if Username or Email Exists

    if User.objects.filter(username=req_body['username']).exists():
        raise ValidationError("Username exists")
        return JsonResponse({'message': "Username already Exists"}, status=500)

    if User.objects.filter(email=req_body['email']).exists():
        raise ValidationError("Email exists")
        return JsonResponse({'message': "Email already Exists"}, status=500)

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    new_user = User.objects.create_user(
        username=req_body['username'],
        password=req_body['password'],
        first_name=req_body['first_name'],
        last_name=req_body['last_name'],
        email=req_body['email']
    )
        

    coder = Coder.objects.create(
        profile_image=req_body['profile_image'],
        primary_language=req_body['primary_language'],
        github=req_body['github'],
        user=new_user
    )

    # Commit the user to the database by saving it
    coder.save()

    # Use the REST Framework's token generator on the new user account
    token = Token.objects.create(user=new_user)

    # Return the token to the client
    data = json.dumps({"token": token.key})
    return HttpResponse(data, content_type='application/json')

    # except IntegrityError as ex:
    #     return HttpResponse(ex, content_type='application/json')
