 
from django import forms

from .models import  Student, Course
# Тук отново имаме ModelForm този път за изпит

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'faculty_number', 'year_of_study', 'study_type', 'course']

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Първо име'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['faculty_number'].label = 'Факултетен номер'
        self.fields['year_of_study'].label = 'Година на обучение'
        self.fields['study_type'].label = 'Начин на обучение'
        self.fields['course'].label = 'Kурс'

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'p-1 w-full block border border-gray-400 rounded-md'})


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'faculty', 'education_level']
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Име'
        self.fields['faculty'].label = 'Факултет'
        self.fields['education_level'].label = 'Ниво на образование'

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'p-1 w-full block border border-gray-400 rounded-md'})