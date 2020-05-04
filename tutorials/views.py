from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
# from rest_framework.response import Response
from rest_framework import status
from tutorials.models import Tutorials
from tutorials.serializers import TutorialSerializer
from rest_framework.decorators import api_view
from django.http import HttpResponse



@api_view(['GET', 'POST', 'DELETE'])
def get_all_tutorials(request):
    if request.method == 'GET':
        tutorials = Tutorials.objects.all()
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorials_serializer = TutorialSerializer(data=tutorial_data)
        if tutorials_serializer.is_valid():
            tutorials_serializer.save()
            return JsonResponse(tutorials_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorials_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Tutorials.objects.all().delete()
        return JsonResponse({'msg': '{} Tutorials was deleted successfully!'.format(count[0])},  status=status.HTTP_204_NO_CONTENT)




# Find a single tutorial with an ID
@api_view(['GET', 'PUT', 'DELETE'])
def get_tutorial_details(request, pk):
    try:
        tutorials = Tutorials.objects.get(pk=pk)

    except Tutorials.DoesNotExist:
        return JsonResponse({'msg': 'The tutorial does not exist'}, status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tutorials_serializer = TutorialSerializer(tutorials)
        return JsonResponse(tutorials_serializer.data, safe=False)
    
    elif request.method == 'PUT':
        tutorial_data = JSONParser().parse(request)
        tutorials_serializer = TutorialSerializer(tutorials, data=tutorial_data)
        if tutorials_serializer.is_valid():
            tutorials_serializer.save()
            return JsonResponse(tutorials_serializer.data)
        return JsonResponse(tutorials_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tutorials.delete()
        return JsonResponse({'msg': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)



# Find tutorials with published is True
@api_view(['GET'])
def tutorials_published(request):
    tutorials = Tutorials.objects.filter(published=True)
    if request.method == 'GET':
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)

# Find tutorials with published is False
@api_view(['GET'])
def tutorials_published_false(request):
    tutorials = Tutorials.objects.filter(published=False)
    if request.method == 'GET':
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)

# Find or search tutorials by title
@api_view(['GET', 'PUT', 'DELETE'])
def get_tutorial_by_title(request):
    if request.method == 'GET':
        tutorials = Tutorials.objects.all()
        title = request.Get.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title___icontains=title)
        tutorials_serializer  = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)


