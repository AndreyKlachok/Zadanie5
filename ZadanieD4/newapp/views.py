from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from .models import New, Category
from datetime import datetime
from .filters import NewFilter
from .forms import NewForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin



class NewList(ListView):
    model = New
    template_name = 'New_list.html'
    context_object_name = 'news'
    ordering = ['-datetime']
    paginate_by = 5

    def get_filter(self):
        return NewFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            'filter': self.get_filter(),
            'time_now': datetime.utcnow(),
            'form': NewForm()
        }


class NewDetailView(DetailView):
    template_name = 'newapp/news_detail.html'
    queryset = New.objects.all()


class NewCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'newapp/news_create.html'
    form_class = NewForm
    permission_required = ('new.add_new', 'new.create_new')


class NewUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'newapp/news_create.html'
    form_class = NewForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return New.objects.get(pk=id)


class NewDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'newapp/news_delete.html'
    queryset = New.objects.all()
    success_url = '/news/'