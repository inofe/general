from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import ToDoItem
from .forms import ToDoItemForm
from django.urls import reverse_lazy
from django.views.generic import (
    View,
    TemplateView,
    RedirectView,
    FormView,
    ListView,

    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    
)


# def index(request):
#     return render(request, "to_do/index.html")

class MyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "to_do/index.html",{})

    def post(self, request, *args, **kwargs):
        return HttpResponse("Hello, this is a POST request!")
    
class MyTemplateView(TemplateView):
    template_name="to_do/index.html"
    
class MyRedirectView(RedirectView):
    url="/to_do"
    
class MyFormView(FormView):
    template_name="to_do/index.html"
    form_class=ToDoItemForm
    success_url=reverse_lazy("to_do:myformview")
    
    def form_valid(self, form):
        
        #form lcass "from" adlı değişkende gönderilir template'e
        #form gecerli ise burada formla islemler yapilir
        # Form doğrulandıysa yapılacak islemler
        form.save()
        # print(form.cleaned_data)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
            # Şablona ekstra veri eklemek için
            #sablona eklenen veriler context adıyla gecer
            context = super().get_context_data(**kwargs)
            context["page_title"] = "Contact Us"  # Başlık ekliyoruz
            return context
        
class TodoListView(ListView):
    model=ToDoItem
    template_name="to_do/index.html"
    success_url= "to_do:index"
    context_object_name="todoitems"
    ordering=["-created"]

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["page_title"]="To Do App"
        
        return context

class TodoCreateView(CreateView):
    template_name="to_do/index.html"
    model=ToDoItem
    fields=["title","complated"]
    success_url="/to_do"
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["page_title"]="Add new"
        
        return context
    
class TodoUpdateView(UpdateView):
    template_name="to_do/index.html"
    model=ToDoItem
    fields=["title","complated"]
    success_url="/to_do"
    
class TodoDeleteView(DeleteView):
    template_name="to_do/index.html"
    model=ToDoItem
    success_url="/to_do"

class Advanced(ListView):
    model = ToDoItem
    template_name = 'to_do/advanced.html'
    context_object_name = 'todoitems'
    ordering = ['-created']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_form'] = ToDoItemForm()
        # Her öğe için bir düzenleme formu oluştur
        context['edit_forms'] = {item.id: ToDoItemForm(instance=item) for item in context['todoitems']}
        return context

    def post(self, request, *args, **kwargs):
        if 'create_form' in request.POST:
            create_form = ToDoItemForm(request.POST)
            if create_form.is_valid():
                create_form.save()
                return redirect('to_do:advancedlist')
        elif 'edit_form' in request.POST:
            item_id = request.POST.get('item_id')
            item = ToDoItem.objects.get(id=item_id)
            edit_form = ToDoItemForm(request.POST, instance=item)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('to_do:advancedlist')
        elif 'delete_form' in request.POST:
            item_id = request.POST.get('item_id')
            item = ToDoItem.objects.get(id=item_id)
            item.delete()
            return redirect('to_do:advancedlist')
        return self.get(request, *args, **kwargs)
