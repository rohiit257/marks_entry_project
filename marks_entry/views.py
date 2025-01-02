from django.shortcuts import render, redirect
from .models import Student, Question, Marks

def student_marks_ins_fn(request):
    if request.method == 'POST':
        data = request.POST
        students = Student.objects.all()
        questions = Question.objects.all()

        for student in students:
            for question in questions:
                marks_field_name = f'marks_{student.id}_{question.id}'
                marks_value = data.get(marks_field_name)

                if marks_value is not None and marks_value.strip() != "":
                    print(f"Saving marks for Student ID: {student.id}, Question ID: {question.id}, Marks: {marks_value}")
                    marks, created = Marks.objects.get_or_create(student=student, question=question)
                    marks.marks = marks_value
                    marks.save()

        return redirect('submitted_marks')  

    students = Student.objects.all()
    questions = Question.objects.all()
    context = {
        'students': students,
        'questions': questions,
    }
    return render(request, 'marks_entry.html', context)

def student_marks_view_fn(request):
    students = Student.objects.all() 
    questions = Question.objects.all()
    submitted_marks = Marks.objects.all()
    marks_dict = {}
    
    for student in students:
        marks_dict[student.name] = {}
        total_marks = 0
        for question in questions:
            mark_obj = submitted_marks.filter(student=student, question=question).first()
            if mark_obj:
                marks_dict[student.name][question.question_id] = mark_obj.marks
                total_marks += mark_obj.marks
            else:
                marks_dict[student.name][question.question_id] = None
        
        marks_dict[student.name]['total_marks'] = total_marks
    
    context = {
        'marks_dict': marks_dict,
        'questions': questions,
    }
    return render(request, 'submitted_marks.html', context)

def student_marks_upd_fn(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('marks_'):
                student_id, question_id = key.split('_')[1:]
                student = Student.objects.get(pk=student_id)
                question = Question.objects.get(pk=question_id)
                mark = Marks.objects.get_or_create(student=student, question=question)[0]
                mark.marks = value
                mark.save()
        return redirect('submitted_marks')
    else:
        students = Student.objects.all()
        questions = Question.objects.all()
        marks_dict = {}

        for student in students:
            marks_dict[student] = {}
            for question in questions:
                mark = Marks.objects.filter(student=student, question=question).first()
                marks_dict[student][question] = mark.marks if mark else ''

        return render(request, 'update_all_marks.html', {'students': students, 'questions': questions, 'marks_dict': marks_dict})


def get_marks(request):
    students = Student.objects.all()
    questions = Question.objects.all()
    marks = None

    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        question_id = request.POST.get('question_id')
        
        if student_id and question_id:
            marks = Marks.objects.filter(student_id=student_id, question_id=question_id).first()
            print(marks)

    return render(request, 'marks_detail.html', {'students': students, 'questions': questions, 'marks': marks})
