from django.contrib import admin
from . import views,step0,step1,step2,step3
from . import step5,step6,user_login,register
from . import savegen,refer_check,get_detail
from . import rate
from . import preview
from . import admin_view

from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'step0-edit$', step0.edit, ),
    url(r'step0-delete$', step0.delete, ),
    url(r'step1$', step1.step1, ),
    url(r'step2$', step2.step2, ),
    url(r'step2-saveFloor$', step2.saveFloor, ),
    url(r'step3-get-all-parts$', step3.get_all_parts, ),
    url(r'step3-save-elements$', step3.save_elements, ),
    url(r'step5$', step5.step5 ),
    url(r'step5-save-waves$', step5.save_waves ),
    url(r'step5-save-wave_file$', step5.save_wave_file ),
    url(r'step6$', step6.step6 ),
    url(r'rate$', rate.rate ),
    url(r'show_projects$', views.show_projects, ),
    url(r'brief_projects$', views.brief_projects, ),
    url(r'login$', user_login.login ),
    url(r'user_register$', register.user_register ),
    url(r'savegen$', savegen.savegen ),
    url(r'savegen_gen_info$', savegen.savegen_gen_info ),
    url(r'savegen_image$', savegen.savegen_image ),
    url(r'savegen_num$', savegen.savegen_num ),
    url(r'refer_check_statenum$', refer_check.refer_check_statenum ),
    url(r'refer_check_re_info$', refer_check.refer_check_re_info ),
    url(r'refer_check_re_costAndTime$', refer_check.refer_check_re_costAndTime),
    url(r'get_detail$', get_detail.get_detail),
    url(r'preview$',preview.preview),

    url(r'show_projects_all$', admin_view.show_projects_all ),
    ]