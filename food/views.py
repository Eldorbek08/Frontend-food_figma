
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny

from .models import Comments,Category,Foods,BookTable,Contact
from .serializers import CommentsSerializers,CategorySerializers,FoodsSerializers,BookTableSerializers,ContactSerializers

class CommentsViews(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializers
    permission_classes = [IsAuthenticated]
    
class CategoryViews(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    
class foodsViews(viewsets.ModelViewSet):
    queryset = Foods.objects.all()
    serializer_class = FoodsSerializers
    
class BookTableViews(viewsets.ModelViewSet):
    queryset = BookTable.objects.all()
    serializer_class = BookTableSerializers
    
class ContactViews(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers