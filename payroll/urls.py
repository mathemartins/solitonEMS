from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Pages
    path('', views.payroll_page, name="payroll_page"),
    path('manage_payroll_records_page', views.manage_payroll_records_page, name="manage_payroll_records_page"),
    path('view_payroll_records_page', views.view_payroll_records_page, name="view_payroll_records_page"),
    path('edit_period_page/<int:id>/', views.edit_period_page, name="edit_period_page"),
    path('payroll_record_page/<int:id>/', views.payroll_record_page, name="payroll_record_page"),
    path('view_payslip_page', views.view_payslip_page, name='view_payslip_page'),
    path('payslip_page/<int:id>', views.payslip_page, name='payslip_page'),
    path('payslips/<int:payroll_record_id>/', views.payslips_page, name="payslips_page"),
    path('your_payslip', views.your_payslip_page, name="your_payslip"),
    # Processing
    path('add_period/', views.add_period, name="add_period"),
    path('delete_period/<int:id>/', views.delete_period, name="delete_period"),
    path('edit_period/', views.edit_period, name="edit_period"),
    path('generate_payroll/<int:id>', views.create_payroll_payslips, name="generate_payroll"),
    path('add_prorate/', views.add_prorate, name="add_prorate"),
    path('add_bonus/', views.add_bonus, name="add_bonus"),
    path('add_overtime/', views.add_overtime, name="add_overtime"),
    path('payroll_download/<int:id>/', views.payroll_download, name="payroll_download"),
    path('generate_payslip_pdf/<int:id>/', views.generate_payslip_pdf, name="generate_payslip_pdf"),
]
