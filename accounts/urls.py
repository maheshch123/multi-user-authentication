from django.urls import path
from . import views

urlpatterns = [path('register', views.register, name='register'),
               path('login', views.login, name='login'),
               path('logout', views.logout, name='logout'),
               path('teach', views.teach, name='teach'),
               path('teach1', views.teach1, name='teach1'),
               path('stud', views.stud, name='stud'),
               path('stud1', views.stud1, name='stud1'),
               path('reg', views.reg, name='reg'),
               path('log', views.log, name='log'),
               # path('logout1', views.logout1, name='logout1'),
               path('details',views.details, name='details'),
               path('accounts/delete/<int:id>',views.delete, name='delete'),
               path('accounts/edit/<int:id>',views.edit, name='edit'),
               path('accounts/edit/update/<int:id>',views.update, name='update'),

    
               
            ]