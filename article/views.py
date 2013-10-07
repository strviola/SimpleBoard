# Create your views here.
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader, Context
from article.models import Article
from django import shortcuts
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


def test(request):
    return HttpResponse('Hello SimpleBoard application!')


def headline(request):
    # For practice, this view is written without shortcut.
    latest_post = Article.objects.order_by('-date')
    template = loader.get_template('headline.html')
    context = Context({'latest_post': latest_post})
    return HttpResponse(template.render(context))


def detail(request, article_id):
    a = Article.objects.get(pk=article_id)
    d = a.post_str()
    return shortcuts.render_to_response(
        'detail.html', {'article': a, 'date': d})


@login_required
def form(request):
    return shortcuts.render_to_response('form.html',
        context_instance=RequestContext(request))


@login_required
def post(request):
    try:
        title = request.POST['title']
        body = request.POST['body']
    except KeyError:
        return HttpResponseBadRequest()

    if title == '' or body == '':
        return HttpResponseBadRequest()

    Article.objects.create(title=title, body=body)
    return shortcuts.render_to_response('accept.html')
