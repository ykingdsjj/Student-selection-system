from django.shortcuts import render
from .models import TeacherUser
from course import models as courseModels
from django.shortcuts import redirect
from .forms import TeacherApplyCourseForm
# Create your views here.
def teacherIndex(request):
    pass
    return render(request, 'teacher/teacherIndex.html')

def teacherInformation(request):
    teacher = TeacherUser.objects.get(teacherID=request.session['user_id'])
    context = {'teacher':teacher}
    return render(request, 'teacher/teacherInformation.html', context)

def teacherManagement(request):
    courses = courseModels.SelectCourse.objects.filter(selectCourseTeacher=request.session['user_id'])
    context = {'courses':courses}
    return render(request, 'teacher/teacherManagement.html', context)

def teacherCourse(request):
    
    if request.method == 'POST':
        form = TeacherApplyCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacherCourse')

    else:
        form = TeacherApplyCourseForm() 
        applyCourse = courseModels.TeacherApplyCourse.objects.filter(teacher=request.session['user_id'])
        courses = courseModels.Course.objects.all()

    context = {'form':form, 'applyCourse':applyCourse, 'courses':courses}
    return render(request, 'teacher/teacherCourse.html', context)

def teacherManagementClass(request, classID):
    students = courseModels.StudentSelectCourse.objects.filter(studentSelectCourse_course=classID)
    if request.method == 'POST':
        for student in students:
            score = request.POST.get(student.studentSelectCourse_stduent.studentID.userID)
            student.studentSelectCourse_score = score
            student.save()
        return redirect('teacherManagementClass', classID)

    else:
        context = {'students':students,'classID':classID}
        return render(request, 'teacher/teacherManagementClass.html', context)