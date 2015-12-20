from django.shortcuts import render
 
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse
import random
 
 
question_list = []
answer_list = []
 
for i in xrange(1,30):
    question_list.append({
        'title' : 'What if??????{}'.format(i),
        'id' : i,
        'text' : 'wtff {}'.format(i),
        'rating' : random.randint(-100, 100),
        'answers_count' : random.randint(0, 100),
        })
 
def paginate(object_list, objects_count, page_num):
 
    paginator = Paginator(object_list, objects_count)
    try:
        objects_page = paginator.page(page_num)
    except EmptyPage:
            objects_page = paginator.page(paginator.num_pages)
    return objects_page
 
def index(request, page = 1):
     
    questions = paginate(question_list, 5, page)
 
    return render(request, 'ask/index.html', {
        'objects': questions,
        'view_name': 'index',
        'url_prefix': ''
    })
 
def hot_index(request, page = 1):
     
    sorted_q_list = sorted(question_list, key=lambda x: x['rating'], reverse=True)
    questions = paginate(sorted_q_list, 5, page)        
 
    return render(request, 'ask/hot.html', {
                'objects': questions,
                'view_name': 'hot_index',
                'url_prefix': '/hot'
        })
 
 
 
def signup(request):
 
    return render(request, 'ask/signup.html')
 
def login(request):
 
    return render(request, 'ask/login.html')
 
 
def ask(request):
 
        return render(request, 'ask/ask.html')
 
def answers(request, id, page=1):
    answer_list = []
    ans_count = question_list[int(id) -1 ]['answers_count']
    for i in xrange(1, ans_count+1):
        answer_list.append({
                'id' : i,
                'text' : 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed  {}'.format(i),
                })
        answers = paginate(answer_list, 5, page)
 
    return render(request, 'ask/answers.html', {
        'question': question_list[int(id) - 1],
        'objects': answers,
        'view_name': 'answers',
        'url_prefix': '/question/{}'.format(id),
        })
     
 
def tag_index(request, tag, page=1):
 
        questions = paginate(question_list, 5, page)
 
        return render(request, 'ask/tag_index.html', {
                'objects': questions,
                'view_name': 'tag_index',
                'current_tag': tag,
                'url_prefix': '/tag/{}'.format(tag)
        })
