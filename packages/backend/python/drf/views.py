from rest_framework.response import Response
from rest_framework.views import APIView
from .lib.database.client import get_db

class HelloWorld(APIView):
    def get(self, request):
        db = get_db()
        users = db.users.find_one()
        print(users)
        return Response({"message": "Hello, World!"})