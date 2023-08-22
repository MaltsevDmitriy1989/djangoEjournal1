from django.urls import path, re_path
from quest import views
# from quest.views import QuestionView
app_name = 'quest'

urlpatterns = [
    path('', views.begin),


    path('admin_code', views.admin_code, name = 'admin_code'),
    path('superadmin', views.superadmin),	
    path('admin', views.admin),
    path('admin_parol', views.admin_parol),
    path('parol_insert', views.parol_insert),
    path('parol_edit', views.parol_edit),
    path('admin_plan', views.admin_plan),
    path('plan_insert', views.plan_insert),
    path('plan_edit', views.plan_edit),
    path('question', views.question_form, name='question'),

    path('proba', views.proba, name='proba'),
    path('student', views.student, name='student'),
    path('kagalym', views.kagalym, name='kagalym'),
    path('kagalym_rez', views.result_kag, name='kagalym_rez'),

#    path('anketa_admin_code', anketa.anketa_admin_code),		
]
