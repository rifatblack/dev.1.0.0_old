from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView

from product.forms import VariantForm
from product.models import Variant

from product.models import Product


class BaseVariantView(generic.View):
    form_class = VariantForm
    model = Variant
    template_name = 'variants/create.html'
    success_url = '/product/variants'


class VariantView(BaseVariantView, ListView):
    template_name = 'variants/list.html'
    #context_object_name = Product
    paginate_by = 2
    model = Product

    def get_queryset(self):
        filter_string = {}
        print(self.request.GET)
        for key in self.request.GET:
            if self.request.GET.get(key):
                filter_string[key] = self.request.GET.get(key)
        return Variant.objects.filter(**filter_string)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = True
        context['request'] = ''
        if self.request.GET:
            context['request'] = self.request.GET['title__icontains']
        return context


class VariantCreateView(BaseVariantView, CreateView):
    pass


class VariantEditView(BaseVariantView, UpdateView):
    pk_url_kwarg = 'id'
