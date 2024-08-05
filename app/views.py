from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.hashers import  check_password
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# import datetime
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Person, FaildLogin
from .serializers import PersonSerializer
# Create your views here.

class PersonAuthentication(APIView):

    def post(self, request):
            person_ins = get_object_or_404(Person, person_number=request.data.get("person_number"))
            serializer = PersonSerializer(instance=person_ins, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return render(request, "app/register.html", context={"info" : "login"}) 



class PersonLogin(APIView):

    def post(self, request):
        if request.data and request.session.get('visited'):
            if request.session.get("has_blocked"):
                time_remain = request.session.get_expiry_age()
                time_minute = int(time_remain/60)
                time_second = time_remain % 60
                return Response({"message" : f'{time_minute} دقیقه {time_second}'})

            person_num = request.data.get('person_number')
            person_pass = request.data.get('password')
            person_ins = get_object_or_404(Person, person_number=person_num)

            if check_password(person_pass,person_ins.password):
                person_faild_attempt = FaildLogin.objects.filter(person_id=person_ins).delete()
                return Response({"message" : "با موفقیت وارد شدید", "session" : request.session}, status=status.HTTP_200_OK)
            else:
                person_faild_attempt = FaildLogin.objects.filter(person_id=person_ins)
                FaildLogin.objects.create(person_id=person_ins)

                if person_faild_attempt.count() >= 3:
                    request.session['has_blocked'] = True
                    request.session.set_expiry(timezone.now() + timezone.timedelta(minutes=10))
                    person_faild_attempt.delete()
                    return Response({"has_blocked" : request.session.get('has_blocked') , "time" : request.session.get_expiry_date()})
                return Response({"message" : "پسورد اشتباه است یا کاربر پیدا نشد"}, status=status.HTTP_404_NOT_FOUND)
        else:
            request.session['visited'] = True
            return render(request, "app/register.html", context={"info" : "new_pass"}) 
