from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def hello_api(request):
    return Response({"message":"안녕하세요, DRF API입니다!"})