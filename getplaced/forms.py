from django import forms
from .models import Studtb
from .models import Student
from .models import Admintb
from .models import Suggestions
from .models import Placement_History
from .models import Interview_details
from .models import Sprofile

class StudtbForm(forms.ModelForm):
    class Meta:
        model=Studtb
        fields=['Username','pwd']
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['roll_no','studname','phoneno','email_id','branch','sec','syear','psd','username']

class AdmintbForm(forms.ModelForm):
    class Meta:
        model=Admintb
        fields=['username','email_id','password']

class SuggestionsForm(forms.ModelForm):
    class Meta:
        model=Suggestions
        fields=['title','mock_tests','tips','video_links','added_on','added_by']

class Placement_HistoryForm(forms.ModelForm):
    class Meta:
        model=Placement_History
        fields=['pyear','company_name','package','ptype','students_applied','students_placed']

class Interview_detailsForm(forms.ModelForm):
    class Meta:
        model=Interview_details
        fields=['company_name','job_title','job_description','requisites','selection_process','link','time','date','added_by','added_on']

class SprofileForm(forms.ModelForm):
    class Meta:
        model=Sprofile
        fields=['abt','skl','prjdesc','prjlink','reslink','usern']
