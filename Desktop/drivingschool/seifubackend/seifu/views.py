from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import ResultForm
from seifu.models import NewStudent, StudentResult
from seifu.serializer import NewStudentSerializer, StudentResultSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def Home(request):
    student = NewStudent.objects.all()
    return render(request, 'home.html', {'student': student})

def Result(request):
    if request.method == "POST":
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/results')
    else:
        form = ResultForm()

    return render(request, 'results.html', {'form': form})

("""
@csrf_exempt
@api_view(['POST', 'OPTIONS'])
def submit_form(request):
    if request.method == 'OPTIONS':
        response = Response(status=status.HTTP_200_OK)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        return response
    elif request.method == 'POST':
        # Handle form submission
        full_name = request.data.get('full_name')
        phone_number = request.data.get('phone_number')
        wanted_licence = request.data.get('wanted_licence')
        # Process the data as needed
        return Response({'message': 'Form submitted successfully'}, status=status.HTTP_200_OK)
""")

class NewStudentView(APIView):
    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NewStudentViewset(viewsets.ModelViewSet):
    queryset = NewStudent.objects.all()
    serializer_class = NewStudentSerializer

class StudentResultViewset(viewsets.ModelViewSet):
    queryset = StudentResult.objects.all()
    serializer_class = StudentResultSerializer