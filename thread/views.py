from django.views.generic import CreateView, FormView, DetailView, ListView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404


from . forms import TopicModelForm, CommentModelForm
from . models import Topic, Category, Comment

from django.contrib.auth.mixins import LoginRequiredMixin

class TopicAndCommentView(FormView):
    template_name = 'thread/detail_topic.html'
    form_class = CommentModelForm
    
    def form_valid(self, form):
        kwargs = {}
        kwargs['user'] = self.request.user
        form.save_with_topic(self.kwargs.get('pk'), **kwargs)
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('thread:topic', kwargs={'pk': self.kwargs['pk']})
    
    def get_context_data(self):
        ctx = super().get_context_data()
        ctx['topic'] = Topic.objects.get(id=self.kwargs['pk'])
        ctx['comment_list'] = Comment.objects.filter(
                topic_id=self.kwargs['pk']).order_by('no')
        return ctx

class TopicCreateView(LoginRequiredMixin,CreateView):
    template_name = 'thread/create_topic.html'
    form_class = TopicModelForm
    model = Topic
    success_url = reverse_lazy('base:top')

    def form_valid(self, form):
        ctx = {'form': form}
        if self.request.POST.get('next', '') == 'confirm':
            ctx['category'] = form.cleaned_data['category']
            return render(self.request, 'thread/confirm_topic.html', ctx)
        elif self.request.POST.get('next', '') == 'back':
            return render(self.request, 'thread/create_topic.html', ctx)
        elif self.request.POST.get('next', '') == 'create':
            form.save(self.request.user)
            return redirect(self.success_url)
        else:
            # 正常動作ではここは通らない。エラーページへの遷移でも良い
            return redirect(reverse_lazy('base:top'))

class CategoryView(ListView):
    template_name = 'thread/category.html'
    context_object_name = 'topic_list'

    def get_queryset(self):
        return Topic.objects.filter(category__url_code = self.kwargs['url_code'])
     
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['category'] = get_object_or_404(Category, url_code=self.kwargs['url_code'])
        return ctx
