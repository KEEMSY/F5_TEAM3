# from django.shortcuts import render, redirect
# from articleapp.models import Article
#
# # Create your views here.
#
#
#
# def show_article(request):
#     articles = Article.objects.all()
#     return render(request, 'templates/community.html', {'articles':articles})
#
# # def index(request):
# #     articles = Article.objects.all()
# #     return render(request, 'blog/index.html', {'articles': articles})
#
#
# # @login_required(login_url='signin')
# def new(request):
#     if request.method == 'POST':
#         # POST 일때는 글 수정
#         article = Article.objects.create(
#             author=request.user,
#             title=request.POST['title'],
#             content=request.POST['content']
#         )
#         return redirect('detail', article.pk)
#     else:
#         return render(request, 'templates/new.html')
#
# # @login_required(login_url='signin')
# def detail(request, pk):
#     article = Article.objects.get(pk=pk)  #L=필드명, R=변수
#     return render(request, 'blog/detail.html', {'article': article})  # L=html 변수, R=views 변수
#
# # @login_required(login_url='signin') # 로그인하지 않을 경우 리다이렉트
# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     # 남이 쓴 글 수정 방지
#     if request.user == article.author:
#         if request.method == 'POST':
#             # POST 일때는 글 수정
#             article.title = request.POST['title']
#             article.content = request.POST['content']
#             article.save()
#             return redirect('detail', article.pk)
#         else:
#             return render(request, 'templates/edit.html', {'article': article})
#     else:
#         return render(request, 'templates/edit.html', {'error': '잘못된 접근'})
#
# # @login_required(login_url='signin')  # 로그인하지 않을 경우 리다이렉트
# def delete(request, pk):
#     article = Article.objects.get(pk=pk)
#     # 남이 쓴 글 수정 방지
#     if request.user == article.author:
#         article.delete()
#         return redirect('index')
#     else:
#         return redirect('detail', article.pk)
#
#
#
#
#
#
#
#
#
#
#
