from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Board

# Create your views here.
def home(request):
    boards = Board.objects.all()
    # board_names = list()

    # for board in boards:
    #     board_names.append(board.name)

    # response_html = '<br>'.join(board_names)

    # return HttpResponse(response_html)
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    # try:
    #     board = Board.objects.get(pk=pk)
    # except Board.DoesNotExist:
    #     raise Http404
    #
    #shortcut to get object or 404
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})
