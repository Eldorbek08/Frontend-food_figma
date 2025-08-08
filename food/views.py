
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Comments,Category,Foods,BookTable,Contact
from .serializers import CommentsSerializers,CategorySerializers,FoodsSerializers,BookTableSerializers,ContactSerializers

class CommentsViews(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializers
    permission_classes = [AllowAny] 
    
class CategoryViews(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [AllowAny]  # Bu yerda token kerak bo‘lmaydi
    
class foodsViews(viewsets.ModelViewSet):
    queryset = Foods.objects.all()
    serializer_class = FoodsSerializers
    permission_classes = [AllowAny]
    
class BookTableViews(viewsets.ModelViewSet):
    queryset = BookTable.objects.all()
    serializer_class = BookTableSerializers
    
class ContactViews(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers