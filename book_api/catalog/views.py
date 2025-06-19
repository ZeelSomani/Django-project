from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Book
from .serializers import BookSerializer
from .decorators import require_api_key

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['POST'])
@require_api_key
def book_create(request):
    serializer = BookSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    serializer = BookSerializer(book, context={'request': request})
    return Response(serializer.data)

@api_view(['PUT'])
@require_api_key
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    serializer = BookSerializer(book, data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@require_api_key
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return Response(status=204)

@api_view(['POST'])
@require_api_key
@parser_classes([MultiPartParser, FormParser])
def upload_cover(request, pk):
    book = get_object_or_404(Book, pk=pk)
    cover = request.FILES.get('cover')
    if not cover:
        return Response({"error": "NO_FILE", "message": "No file uploaded"}, status=400)
    if cover.size > 2 * 1024 * 1024:
        return Response({"error": "FILE_TOO_LARGE", "message": "File size exceeds 2MB"}, status=413)
    if not cover.content_type in ["image/jpeg", "image/png", "image/webp"]:
        return Response({
            "error": "INVALID_FILE_TYPE",
            "message": "Only JPG, PNG, and WEBP files are allowed",
            "allowed_types": ["jpg", "png", "webp"],
            "received_type": cover.content_type.split('/')[-1]
        }, status=400)
    book.cover_image = cover
    book.save()
    return Response({
        "id": book.id,
        "title": book.title,
        "cover_url": request.build_absolute_uri(book.cover_image.url),
        "message": "Cover uploaded successfully"
    }, status=200)
