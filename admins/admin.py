from django.contrib import admin
from django.contrib.auth.hashers import make_password, check_password
from .models import Admin as AdminModel
# Register your models here.

class AdminPanel(admin.ModelAdmin):
  list_display = ('name','email')
  list_filter = ('name', 'email')
  #prepopulated_fields = {'slug': ('email',)}
  def save_model(self, request, obj, form, change):
    obj.password = make_password(form.cleaned_data.get('password'))
    super().save_model(request, obj, form, change)


admin.site.register(AdminModel, AdminPanel)
