# # Multiple Questions: Add imports here
# import json
# from assessment.models import fruit_to_dict, Fruit
# from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
# from django.shortcuts import get_object_or_404
# from django.urls import reverse
# from http import HTTPStatus

# def fruit_list(request):
#     # Question 1: Complete this function body
#     if request.method == "GET":
#         return handle_list_get()

#     if request.method == "POST":
#         return handle_list_post(request.body)

#     return HttpResponseNotAllowed(["GET", "POST"])

# def fruit_detail(request, pk):
#     # Question 2: Complete this function body

#     if request.method == "GET":
#         return handle_detail_get(pk)
#     elif request.method == "PUT":
#         return handle_detail_put(pk, request.body)
#     elif request.method == "DELETE":
#         return handle_detail_delete(pk)

#     return HttpResponseNotAllowed(["GET", "PUT", "DELETE"])

# def handle_list_get():
#     # Question 3: Complete this function body
#     fruits = Fruit.objects.all()
#     posts_as_dict = [fruit_to_dict(p) for p in fruits]
#     return JsonResponse({"data": posts_as_dict})



# def handle_detail_get(pk):
#     # Question 3: Complete this function body
#     # Question 3: Complete this function body
#     post = get_object_or_404(Fruit, pk=pk)

#     return JsonResponse(fruit_to_dict(post))



# def handle_list_post(body):
#     # Question 4: Complete this function body
#     post_data = json.loads(body)
#     post = Fruit.objects.create(**post_data)
#     return HttpResponse(
#         status=HTTPStatus.CREATED,
#         headers={"Location": reverse("api_fruit_detail", args=(post.pk,))},
#     )


# def handle_detail_put(pk, body):
#     # Question 5: Complete this function body
#     post = get_object_or_404(Fruit, pk=pk)
#     post_data = json.loads(body)
#     for field, value in post_data.items():
#         setattr(post, field, value)
#     post.save()
#     return HttpResponse(status=HTTPStatus.NO_CONTENT)


# def handle_detail_delete(pk):
#     # Question 5: Complete this function body
#     post = get_object_or_404(Fruit, pk=pk)
#     post.delete()
#     return HttpResponse(status=HTTPStatus.NO_CONTENT)


# def post_to_dict(post):
#     return {
#         "pk": post.pk,
#         "author_id": post.author_id,
#         "created_at": post.created_at,
#         "modified_at": post.modified_at,
#         "published_at": post.published_at,
#         "title": post.title,
#         "slug": post.slug,
#         "summary": post.summary,
#         "content": post.content,
#     }


# @csrf_exempt
# def post_list(request):
#     if request.method == "GET":
#         posts = Post.objects.all()
#         posts_as_dict = [post_to_dict(p) for p in posts]
#         return JsonResponse({"data": posts_as_dict})
#     elif request.method == "POST":
#         post_data = json.loads(request.body)
#         post = Post.objects.create(**post_data)
#         return HttpResponse(
#             status=HTTPStatus.CREATED,
#             headers={"Location": reverse("api_post_detail", args=(post.pk,))},
#         )

#     return HttpResponseNotAllowed(["GET", "POST"])


# @csrf_exempt
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)

#     if request.method == "GET":
#         return JsonResponse(post_to_dict(post))
#     elif request.method == "PUT":
#         post_data = json.loads(request.body)
#         for field, value in post_data.items():
#             setattr(post, field, value)
#         post.save()
#         return HttpResponse(status=HTTPStatus.NO_CONTENT)
#     elif request.method == "DELETE":
#         post.delete()
#         return HttpResponse(status=HTTPStatus.NO_CONTENT)

#     return HttpResponseNotAllowed(["GET", "PUT", "DELETE"])
