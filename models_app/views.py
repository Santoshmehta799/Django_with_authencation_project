from rest_framework import status
from django.shortcuts import render
from auth_app_user.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from models_app.serializer import FilterGetSerializer, ProductTypeSerializer
from models_app.models import PickUpWarehouseLocation, Product, ProductQualityEnums, ProductType, Category, PriceStructure

# Create your views here.

# class FilterApi(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#     def get(self, request, *args, **kwargs):
#         user = request.user
#         user_get = PickUpWarehouseLocation.objects.all()
#         serilizer = FilterGetSerializer(user_get, many=True)
#         return Response({
#             "status":200,
#             "message":"successfully get",
#             "data": serilizer.data
#         })

class FilterApi(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        user = request.user
        print("--------------->>",user)
        category_id = 'b6d261bd-86a9-4760-aa8e-cb158bc5fa25'
        product_name = "laptop device"
        category_id = Category.objects.get(id='3ae4d47d-c004-4ea2-a7af-57b29c2708a7')
        craete_obj = ProductType.objects.create(name="speaker",category=category_id, product_quality='GOOD')
        craete_obj.save()
        print('=====>',craete_obj)
        # all_obj = ProductType.objects.all()
        # category_get = ProductType.objects.filter(category__id=category_id)
        # exclude_obj = ProductType.objects.exclude(name=product_name)  # ish name ko chor ka baki ka sab dega name
        # get_obj = ProductType.objects.get(id="918ad077-dc8b-4362-95eb-7b23e885f5d2")
        # count_obj = ProductType.objects.filter(name=product_name).count()
        # first_obj = ProductType.objects.first()
        # last_obj = ProductType.objects.last()
        # exist_obj = ProductType.objects.filter(product_quality=ProductQualityEnums.GOOD.value).exists()
        # ordered_objects = ProductType.objects.order_by('category')
        # ordered_objects = ProductType.objects.order_by('-category')
        # ordered_objects = ProductType.objects.order_by('-created_at')
        # ordered_objects = ProductType.objects.order_by('created_at')
        # value_obj = ProductType.objects.values('name')
        # values_list_obj =ProductType.objects.values_list('name', flat=True)
        # distinct_obj = ProductType.objects.distinct('name')
        # delete_obj = ProductType.objects.filter(name='dummpy').delete()
        # update_obj = ProductType.objects.filter(name='check').update(slug='check')



        # print("--category_get-->",category_get)
        # print("--exclude--->",exclude_obj)
        # print("==get_obj===>",get_obj)
        # print("==count_obj===>",count_obj)
        # print('---all_obj==>',all_obj)
        # print("--first-->",first_obj)
        # print("-last--->",last_obj)
        # print("---exist-->",exist_obj)
        # print("----ordered_objects==>",ordered_objects)
        # print('---value_obj==>',value_obj)
        # print('---values_list_obj==>',values_list_obj)
        # print("--distinct_obj-->",distinct_obj)
        # print("---delete_obj-->",delete_obj)
        # print("----update_obj-->",update_obj)
        return Response({
            "status":'200ok',
            "message":"request os run"
        })
                                             
class CreateApi(APIView):
    pass
#     def post(self, request, *args, **kwargs):
#         name = request.data.get('name')
#         product_quality = request.data.get('product_quality')
#         category_instance = Category.objects.get(id=request.data.get('category'))
#         product_obj = ProductType.objects.create(
#             name=name,
#             product_quality=product_quality,
#             category=category_instance
#         )
#         return Response({
#             "status" : "200 okay",
#             "message": "this is create request",
#         })

# simple create

class CreateApi(APIView):
    pass
#     def post(self, request, *args, **kwargs):
#         print('------>>',request.data)
#         serializer = ProductTypeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 "status" : "200 okay",
#                 "message": "this is create request",
#                 "data":serializer.data
#             },status=status.HTTP_201_CREATED)
#         else:
#             return Response({
#                 "status" : "200 okay",
#                 "message": "this is create request",
#                 "data":serializer.errors
#             }, status=status.HTTP_400_BAD_REQUEST)


# get_or_create

class CreateApi(APIView):
    pass
#     def post(self, request, *args, **kwargs):
#         name = request.data.get('name')
#         product_quality = request.data.get('product_quality')
#         category_instance = Category.objects.get(id=request.data.get('category'))

#         product_obj, created = ProductType.objects.get_or_create(
#             name=name,
#             product_quality=product_quality,
#             category=category_instance
#         )

#         if created:
#             message = "Product created successfully"
#             status_code = status.HTTP_201_CREATED
#         else:
#             message = "Product alreday created successfully"
#             status_code = status.HTTP_201_CREATED

#         seralizer = ProductTypeSerializer(product_obj)
#         return Response({
#             "status": f"{status_code} ok",
#             "message": message,
#             "data":seralizer.data
#         },status=status.HTTP_201_CREATED)


# update without serilizer

class UpdateApi(APIView):
    pass
#     def put(self, request, *args, **kwargs):
        # id=request.headers.get('id')
        # product_obj = ProductType.objects.get(id=id)
        # if product_obj:
        #     product_obj.name = request.data.get('name')
        #     product_obj.product_quality = request.data.get('product_quality')
        #     product_obj.save()
        #     return Response({
        #         "status": "201 created",
        #         "message": "successfully update"
        #     })

        # else:
        #     return Response({
        #         "status":"400 error",
        #         "message":"producttype id does not match"
        #     })
        
# update with seralizer

# class UpdateApi(APIView):
#     def put(self, request, product_type_id, *args, **kwargs):
#         try:
#             product_obj = ProductType.objects.get(id=product_type_id)
#         except ProductType.DoesNotExist:
#             return Response({
#                 "status": "404 not found",
#                 "message": "ProductType with the given ID does not exist"
#             },status=status.HTTP_404_NOT_FOUND)
        
#         product_obj.name = request.data.get('name')
#         product_obj.product_quality = request.data.get('product_quality')
#         product_obj.save()

#         serializer = ProductTypeSerializer(product_obj)

#         return Response({
#             "status": "200 ok",
#             "message": "ProductType successfully updated",
#             "data":serializer.data
#         },status=status.HTTP_201_CREATED)
    

# class UpdateApi(APIView):
#     def put(self, request, product_type_id, *args, **kwargs):
#         try:
#             product_obj = ProductType.objects.get(id=product_type_id)
#         except ProductType.DoesNotExist:
#             return Response({
#                 "status": "404 not found",
#                 "message": "ProductType with the given ID does not exist"
#             },status=status.HTTP_404_NOT_FOUND)

#         new_name = request.data.get('name')
#         new_product_quality = request.data.get('product_quality')

#         if new_name and ProductType.objects.filter(name=new_name).exclude(id=product_type_id).exists():
#             return Response({
#                 "status": "400 bad request",
#                 "message": "ProductType with this name already exists"
#             }, status=status.HTTP_400_BAD_REQUEST)

#         if new_product_quality and ProductType.objects.filter(product_quality=new_product_quality).exclude(id=product_type_id).exists():
#             return Response({
#                 "status": "400 bad request",
#                 "message": "ProductType with this product_quality already exists"
#             }, status=status.HTTP_400_BAD_REQUEST)
        
#         product_obj.name = request.data.get('name')
#         product_obj.product_quality = request.data.get('product_quality')
#         product_obj.save()
#         serializer = ProductTypeSerializer(product_obj)
#         return Response({
#             "status": "200 ok",
#             "message": "ProductType successfully updated product_quality",
#             "Data":serializer.data
#             },status=status.HTTP_201_CREATED)
    

class CraetePriceStructure(APIView):
    def post(self, request, *args, **kwargs):
        price_obj = PriceStructure.objects.all()

        category_name = request.data.get('category_name')
        
        product_type_name = request.data.get('product_type_name')
        product_quality = request.data.get('product_quality')
        
        product_tittle = request.data.get('product_tittle')
        about_the_brand = request.data.get('about_the_brand')
        product_brand = request.data.get('product_brand')

        hsn_code = request.data.get('hsn_code')
        sale_price = request.data.get('sale_price')
        mrp = request.data.get('mrp')
        tax_code = request.data.get('tax_code')



        category_obj = Category.objects.create(name=category_name)
       
        product_type_obj = ProductType.objects.create(
            name=product_type_name,
            category=category_obj,
            product_quality=product_quality
        )

        product_obj = Product.objects.create(
            user=request.user,
            product_type=product_type_obj,
            category=category_obj,
            product_tittle=product_tittle,
            about_the_brand=about_the_brand,
            product_brand=product_brand,
        )

        price_structure_obj = PriceStructure.objects.create(
            product=product_obj,
            hsn_code=hsn_code,
            sale_price=sale_price,
            mrp=mrp,
            tax_code=tax_code,
        )


        print("====get prices structure===>>",price_obj)
        return Response({
            "status": "200 ok",
            "message": "All 4 model create successfully",
        },)
    
# class GetpriceStructure(APIView):
#     def get(self, request, price_id):
#         price_obj = PriceStructure.objects.all()
#         check = price_obj.first()
#         check.product.id
#         print("------->>",check)
#         product_id = check.product.id
#         product_tittle = Product.objects.get(id=product_id)
#         print(product_tittle.product_tittle)
#         product_type_id = product_tittle.product_type.id
#         product_type = ProductType.objects.get(id=product_type_id)
#         category_id = product_type.category.id
#         category_obj = Category.objects.get(id=category_id)
#         print('===',category_obj.name)
#         print('===',category_obj.slug)

#         return Response({
#             "status": "200 ok",
#             "message": "run",
#         },)


class GetpriceStructure(APIView):
    def get(self, request, price_id):
        category_id = "a8e0ec44-2f65-4429-828d-18fee30719c0"
        price_obj = PriceStructure.objects.filter(product__product_type__category__id=category_id)
        print("------price_id-------->>",price_obj)

        return Response({
            "status": "200 ok",
            "message": "run",
        },)



# =============================================================>
from models_app.models import Author, Book, Genre, Profile
from django.http import JsonResponse

# 1. ForeignKey Queries 

def foreign_get(request):
    print("---->",request.user)

    author_obj = Author.objects.get(name="santosh")
    print("--->",author_obj)

    books_by_author = Book.objects.filter(author=author_obj)
    print("---->",books_by_author)

    book = Book.objects.get(title="motivation your self")
    book_author = book.author
    print("==book_author===>",book_author)

    author = Author.objects.get(name=book_author)
    books_by_author = author.book.all()
    print("---books_by_author--->",books_by_author)

    return JsonResponse({
        "status": "200 ok",
        "message": "run",
    })

# 2. OneToOneField Queries

def one_get(request):
    author = Author.objects.get(name="yaahu")
    author_profile = author.profile
    print("===========>>",author_profile)

    profile = Profile.objects.get(author__name=author)
    profile_author = profile.author.bio
    profile_author = profile.author
    print("------profile------>>",profile_author)

    return JsonResponse({
        "status": "200 ok",
        "message": "run",
    })

# 3. ManyToManyField Queries

def many_get(request):
    book = Book.objects.get(title="motivation your self")
    book_genres = book.genres.filter(name='yaahu')
    book_genres = book.genres.all()
    book_genres = book.genres.get(id=4)
    print("==book_genres==>",book_genres)


    genre = Genre.objects.get(id=1)
    books_in_genre = genre.books.all()
    for i in books_in_genre:
        print(i.title)

    genre_obj = Genre.objects.get(id=2)
    book = Book.objects.get(title="etaching")
    genre_obj.books.add(book)
    print("============>>>successfuly add =>")

    gerre_objs = Genre.objects.get(id=2)
    book_obj = Book.objects.get(title='etaching')
    gerre_objs.books.remove(book_obj)
    print("============>>>successfuly remove =>")



    genre = Genre.objects.get(id=4)
    print("--sss-",genre)
    authors_in_genre = Author.objects.filter(book__genres=genre).distinct()

    print("=====authors_in_genre====>>",authors_in_genre)


    # genres = Genre.objects.filter(books__author__name="Santosh").distinct()
    return JsonResponse({
        "status": "200 ok",
        "message": "run",
    })

def advance_get(request):
    genre = Genre.objects.get(id=6)
    # print("=====>",genre)
    # print("=====>",type(genre))
    profiles_of_authors_in_genre = Profile.objects.filter(author__book__genres__name="fall inl ove").distinct()
    # print("===========advance==>>",profiles_of_authors_in_genre)


    author = Author.objects.get(name="dhruv")
    print("-->",author)
    genres_for_author_books = Genre.objects.filter(books__author=author).distinct()
    # print("=====genres_for_author_books======???>>>",genres_for_author_books)

    profile_obj = Profile.objects.get(id=6)
    book_obj = Book.objects.filter(author__profile__website=profile_obj.website)
    # print("========book_obj=======>>",book_obj)


    # Using select_related and prefetch_related  =================================>>>

    # books_select_rel = Book.objects.select_related('author').all()
    # # print("============>>",books_select_rel)
    # for book in books_select_rel:
    #     print(f"==>{book.title} by {book.author.name}") 
        # pass


    # books_prefetch_rel = Book.objects.prefetch_related('genres').all()
    # # print("=====>",books_prefetch_rel)
    # for books in books_prefetch_rel:
    #     print("======>",books.title)
    #     for genre in books.genres.all():
    #         print("====genre===>>",genre.name)


    # books_select_prefetch = Book.objects.select_related('author').prefetch_related('genres').all()
    # for book in books_select_prefetch:
    #     print(f"{book.title} by {book.author.name}")

    #     for genre in book.genres.all():
    #         print(f"Name: {genre.name}, List_of_genere:{genre.list_of_name}")

    books_sel_pre = Book.objects.all()
    for i in books_sel_pre:
        print("============>>",i)
        for j in i.genres.all():
            print(f"Name: {j.name}, List_of_genere:{j.list_of_name}")



    # genres_with_books = Genre.objects.prefetch_related('books').all()
    # authors_with_books_and_genres = Author.objects.prefetch_related('book__genres').all()
    # print("======genres_with_books=======>>>",genres_with_books)
    # print("======authors_with_books_and_genres=======>>>",authors_with_books_and_genres)


    return JsonResponse({
        "status": "200 ok",
        "message": "run",
    })

class ImageUpload(APIView):
    def post(self, request, *args, **kwargs):
        website=request.headers.get("website")
        author=Author.objects.get(id=3)
        profile_image = request.FILES.get("profile_image") 
        try:
            profile_obj,created = Profile.objects.get_or_create(
                author=author,
                website=website,
                prfoile_image=profile_image,
            )
            print("=================>>",created)
            # if not created:
            #     profile_obj.profile_image = profile_image
            #     profile_obj.save()
            return JsonResponse({
                "status": "200 ok",
                "message": "Profile created successfully",
            })
        except Exception as e:
            print(f"That author name alreday exist in db{e}")

            return JsonResponse({
                "status": "500 error",
                "message": f"An error occurred request Because that Author alreday exist in DB:=> {author}",
            }, status=500)   

# class SignalApi(APIView):
#     def post(self, request, *args, **kwargs):
#         name=request.data.get('name')
#         bio = request.data.get('bio')
#         print("============>>",name)
#         print("============>>",bio)
#         author_obj = Author.objects.create(name=name, bio=bio)
#         author_obj.save()
#         return Response({
#             "status":200,
#             "mesaage":"author create successsfuly"
#         })



@api_view(['POST'])
def signal_api (request):
    name=request.data.get('name')
    bio = request.data.get('bio')
    author_obj = Author.objects.create(name=name, bio=bio)
    author_obj.save()
    return Response({
        "status":200,
        "mesaage":"author create successsfuly"
    })

@api_view(['POST'])
def book_signal_genre(request):
    title = request.data.get('title')
    publication_date = request.data.get('publication_date')
    author =request.headers.get('author')
    authr_instance= Author.objects.get(id=author)
    book_obj = Book.objects.create(title=title, publication_date=publication_date, author=authr_instance)
    book_obj.save()

    return Response({
        "status":200,
        "mesaage":"book create successsfuly"
    })


# ====================================aggregate and annotate ==========================================================>>

from django.db.models import Avg, Max, Min, Sum
from django.db.models import Count, Avg


average_id = Book.objects.all().aggregate(Avg('id'))
print("========avg price==>>",average_id)


total_id = Book.objects.all().aggregate(Sum('id'))
print("=======sum======>>",total_id)

price_range = Book.objects.all().aggregate(Max('id'), Min('id'))
print("======min max=========>>",price_range)


authors_with_book_count = Author.objects.annotate(num_books=Count('book'))
for author in authors_with_book_count:
    print(f'=========>{author.name} has written {author.num_books} books.')


authors_with_avg_book_price = Author.objects.annotate(avg_price=Avg('book__id'))
for author in authors_with_avg_book_price:
    print(f'---->{author.name} has an average book price of {author.avg_price}.')


    

# request.headers.get("website")   # this is header get
# request.FILES.get("profile_image")  # this is body inside form-data file and images get
# request.data.get('sale_price')  # this is body get
    



