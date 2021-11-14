from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name="home"),
    path('sapli/',views.StdApplication,name="saplication"),
    path('saplisave/',views.SApliSave,name="sasave"),
    path('sreg/',views.Sregister,name="sreg"),
    path('srsave/',views.StdReg,name="srsave"),
    path('slogin/',views.Login,name="slogin"),
    path('stfreg/',views.Staffreg,name="stafreg"),
    path('stfsave/',views.staff_save,name="stfsave"),
    path('stflogin/',views.Stflogin,name="stflogin"),
    path('scheck/',views.check,name="scheck"),
    path('stdetails/',views.Stddetails,name="stdetails"),
    path('stdlist/',views.Stdlist,name="stdlist"),
    path('stflist/',views.Stflist,name="stflist"),
    path('slogout/',views.stdlogout,name="slogout"),
    path('stfcheck/',views.Staffcheck,name="stfcheck"),
    path('stflogout/',views.stafflogout,name="stflogout"),
    path('dept/',views.Departments,name="dept"),
    path('dptlist/',views.stdeptlist,name="dptlist"),


]