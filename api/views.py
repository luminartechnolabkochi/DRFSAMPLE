from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from api.models import Movie


# localhost:8000/helloworld/
# method:get
# response{"message":"helloworld"}

class HelloWorldView(APIView):

    def get(self,request,*args,**kwargs):

        # process
        context={"message":"helloworld"}
        return Response(data=context)


# localhost:8000/morning/
# method:get
# response{"message":"good morning"}


class MorningView(APIView):

    def get(self,request,*args,**kwargs):

        context={"message":"good morning"}

        return Response(data=context)



# localhost:8000/addition/
# method:post
# data={"num1":100,"num2":200}
    

class AdiitionView(APIView):

    def post(self,request,*args,**kwargs):

        n1=request.data.get("num1")

        n2=request.data.get("num2")

        result=int(n1)+int(n2)

        context={"result":result}
        return Response(data=context)



# url:localhost:8000/division/
    
# method:post
    
# data={"num1":100,"num2":80}


class DivionView(APIView):

    def post(self,request,*args,**kwargs):

        n1=request.data.get("num1")

        n2=request.data.get("num2")

        result=int(n1)/int(n2)

        context={"result":result}

        return Response(data=context)



# url:localhost:8000/bmi/
    
# method:post

# data={"height":120,"weight":75}
    


class BmiView(APIView):

    def post(self,request,*args,**kwargs):

        height_in_cm=int(request.data.get("height"))

        weight_in_kg=int(request.data.get("weight"))


        height_in_meter=height_in_cm/100

        bmi=weight_in_kg/(height_in_meter)**2

        context={"result":bmi}

        return Response(data=context)
    



# url:localhost:8000/calories/
# method:post
# data={"height":156,"weight":76,"age":21,"gender":"male|female"}
    

class CalorieView(APIView):

    def post(self,request,*args,**kwargs):

        height=int(request.data.get("height"))

        weight=int(request.data.get("weight"))

        age=int(request.data.get("age"))

        gender=request.data.get("gender")

        bmr=0

        if gender == "male":
            #10 * weight (kg) + 6.25 * height(cm) - 5 * age(y) + 5 for (man)
            bmr=(10*weight)+(6.25*height)-(5*age)+5

        elif gender == "female":

            #10 * weight(kg) + 6.25 * height(cm) - 5 * age(y) - 161 for ​(woman)
            bmr=(10*weight)+(6.25*height)-(5*age)-161

        context={"result":bmr}

        return Response(data=context)





# ALBUM CRUD
# =========api for listing all albums
    # url:localhost:8000/api/albums/
    # method:get
    # data:nill
    
# =========api for creating new album
    # url:localhost:8000/api/albums/
    #method:post
    #data{}
    
class AlbumsView(APIView):

    def get(self,request,*args,**kwargs):

        qs=Movie.objects.all()#qs

        data=[]
        for movie_obj in qs:
            dictionary={
            "title":movie_obj.title,
            "director":movie_obj.director,
            "genre":movie_obj.genre,
            "run_time":movie_obj.run_time,
            "language":movie_obj.language,
            "year":movie_obj.year
        }
            data.append(dictionary)


        return Response(data=data)
    
    def post(self,request,*args,**kwargs):

        context={"message":"logic for creating new album"}

        print(request.data)

        movie_obj=Movie.objects.create(
            title=request.data.get("title"),
            director=request.data.get("director"),
            genre=request.data.get("genre"),
            run_time=request.data.get("run_time"),
            language=request.data.get("language"),
            year=request.data.get("year")
        )
        # movie_obj is not json serializable
        # python_native type => json
        # [{}] () {}

        data={
            "title":movie_obj.title,
            "director":movie_obj.director,
            "genre":movie_obj.genre,
            "run_time":movie_obj.run_time,
            "language":movie_obj.language,
            "year":movie_obj.year
        }
        

        return Response(data=data)
    

    





