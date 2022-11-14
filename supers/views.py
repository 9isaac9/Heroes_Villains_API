from django.shortcuts import get_object_or_404  
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super




# Create your views here.
@api_view(['GET', 'POST'])
def supers_list(request):
    
    if request.method == 'GET':
        
        querparams= request.query_params.get('type')
        print (querparams)  

        queryset = Super.objects.all()

        if querparams:
            queryset = queryset.filter(super_type__type=querparams)

            
     

        serializer = SuperSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super);
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save
        return Response(serializer.data)

    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def get(request):

    hero = Super.objects.filter(super_type=1)
    villain = Super.objects.filter(super_type=2)

    hero__type_serializer = SuperSerializer(hero, many=True),
    villain_type_serializer = SuperSerializer(villain, many=True)

    custom_response_dict = {
        "Hero":hero__type_serializer.data,
        "Villain":villain_type_serializer.data
    }
    return Response(custom_response_dict)
      
    



        


       

        

    
