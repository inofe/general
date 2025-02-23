from django.urls import path
from . import views


app_name = 'to_do'
urlpatterns = [
    # path('', views.index, name='index'),
    path('myview/', views.MyView.as_view(), name='myview'),
    path("templateview/",views.MyTemplateView.as_view(),name="templateview"),
    path("redirectview/",views.MyRedirectView.as_view(),name="redirectview"),
    path("myformview/",views.MyFormView.as_view(),name="myformview"),
    
    #real to do app
    path("", views.TodoListView.as_view(),name="todolistview"),
    path("add/",views.TodoCreateView.as_view(),name="todocreateview"),
    path("<int:pk>/update",views.TodoUpdateView.as_view(),name="todoupdateview"),
    path("<int:pk>/delete",views.TodoDeleteView.as_view(),name="tododeleteview"),
      
    #advanced
    path("advanced/",views.Advanced.as_view(),name="advancedlist"),
    
]