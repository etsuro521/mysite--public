from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from thread.models import Topic
# Create your views here.
class TopicListView(ListView):
    template_name = 'base/top.html'
    queryset = Topic.objects.order_by('-created')
    context_object_name = 'topic_list'
    paginate_by = 10
    page_kwarg = 'p'