from django.urls import path
from .views import student_marks_ins_fn,get_marks,student_marks_view_fn,student_marks_upd_fn

urlpatterns = [
    path('marks-entry/', student_marks_ins_fn, name='marks_entry'),
    path('get-marks/', get_marks, name='get_marks'),
    path('submitted-marks/', student_marks_view_fn, name='submitted_marks'), 
    path('update-all-marks/', student_marks_upd_fn, name='update-all-marks'),




    



]
