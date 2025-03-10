from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import *
from . import services
from .models import *


def login_required_decorator(func):
    return login_required(func, login_url='login_page')


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


def login_page(request):
    if request.POST:
        username = request.POST.get('username')
        password =  request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect("home_page")

    return render(request, 'login.html')


@login_required_decorator
def home_page(request):
    faculties = services.get_faculties()
    kafedras = services.get_kafedra()
    subjects = services.get_subject()
    teachers = services.get_teacher()
    groups = services.get_group()
    students = services.get_student()
    ctx = {
        'counts' : {
            'faculties': len(faculties),
            'kafedras': len(kafedras),
            'subjects': len(subjects),
            'teachers': len(teachers),
            'groups': len(groups),
            'students': len(students),
        }
    }
    return render(request, 'index.html', ctx)

# Faculty
@login_required_decorator
def faculty_create(request):
    model = Faculty()
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f'You created faculty: {request.POST.get("name")}']
        request.session['actions'] = actions

        action_count = request.session.get('action_count', 0)
        action_count += 1
        request.session["action_count"] = action_count

        return redirect('faculty_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'faculty/form.html', ctx)


@login_required_decorator
def faculty_edit(request, pk):
    model = Faculty.objects.get(pk=pk)
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f'You edited faculty: {request.POST.get("name")}']
        request.session['actions'] = actions

        action_count = request.session.get('action_count', 0)
        action_count += 1
        request.session["action_count"] = action_count

        return redirect('faculty_list')

    ctx ={
        'model': model,
        'form': form
    }
    return render(request, 'faculty/form.html', ctx)

@login_required_decorator
def faculty_delete(request, pk):
    model = Faculty.objects.get(pk=pk)
    model.delete()

    actions = request.session.get('actions', [])
    actions += [f'You deleted faculty: {request.POST.get("name")}']
    request.session['actions'] = actions

    action_count = request.session.get('action_count', 0)
    action_count += 1
    request.session["action_count"] = action_count

    return redirect('faculty_list')

@login_required_decorator
def faculty_list(request):
    faculties = services.get_faculties()
    print(faculties)
    ctx = {
        'faculties':faculties
    }
    return render(request, 'faculty/list.html', ctx)


# Kafedra
@login_required_decorator
def kafedra_create(request):
    model = Kafedra()
    form = KafedraForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f'You created kafedra: {request.POST.get("name")}']
        request.session['actions']=actions

        action_count = request.session.get('action_count', 0)
        action_count += 1
        request.session["action_count"] = action_count


        return redirect('kafedra_list')

    ctx = {
        'model':model,
        'form': form
    }
    return render(request, 'kafedra/form.html', ctx)


@login_required_decorator
def kafedra_edit(request, pk):
    model = Kafedra.objects.get(pk=pk)
    form = KafedraForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f'You edited kafedra: {request.POST.get("name")}']
        request.session['actions'] = actions

        action_count = request.session.get('action_count', 0)
        action_count += 1
        request.session["action_count"] = action_count

        return redirect('kafedra_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'kafedra/form.html', ctx)


@login_required_decorator
def kafedra_delete(request, pk):
    model = Kafedra.objects.get(pk=pk)
    model.delete()

    actions = request.session.get('actions', [])
    actions += [f'You deleted kafedra: {request.POST.get("name")}']
    request.session['actions'] = actions

    action_count = request.session.get('action_count', 0)
    action_count += 1
    request.session["action_count"] = action_count

    return redirect('kafedra_list')


@login_required_decorator
def kafedra_list(request):
    kafedras = services.get_kafedra()
    print(kafedras)
    ctx = {
        'kafedras': kafedras
    }
    return render(request, 'kafedra/list.html', ctx)


# Subject
@login_required_decorator
def subject_create(request):
    model = Subject()
    form = SubjectForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f'You created a subject: {request.POST.get("name")}']
        request.session['actions'] = actions

        action_count = request.session.get('action_count', 0)
        action_count += 1
        request.session["action_count"] = action_count

        return redirect('subject_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'subject/form.html', ctx)


@login_required_decorator
def subject_edit(request, pk):
    model = Subject.objects.get(pk=pk)
    form = SubjectForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f'You edited the subject: {request.POST.get("name")}']
        request.session['actions'] = actions

        action_count = request.session.get('action_count', 0)
        action_count += 1
        request.session["action_count"] = action_count

        return redirect('subject_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'subject/form.html', ctx)


@login_required_decorator
def subject_delete(request, pk):
    model = Subject.objects.get(pk=pk)
    model.delete()

    actions = request.session.get('actions', [])
    actions += [f'You deleted the subject: {request.POST.get("name")}']
    request.session['actions'] = actions

    action_count = request.session.get('action_count', 0)
    action_count += 1
    request.session["action_count"] = action_count

    return redirect('subject_list')


@login_required_decorator
def subject_list(request):
    subjects = services.get_subject()
    print(subjects)
    ctx = {
        'subjects': subjects
    }
    return render(request, 'subject/list.html', ctx)


# Teacher
@login_required_decorator
def teacher_create(request):
    model = Teacher()
    form = TeacherForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f'You added a teacher: {request.POST.get("first_name")}']
        request.session['actions'] = actions

        action_count = request.session.get('action_count', 0)
        action_count += 1
        request.session["action_count"] = action_count

        return redirect('teacher_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'teacher/form.html', ctx)


@login_required_decorator
def teacher_edit(request, pk):
    model = Teacher.objects.get(pk=pk)
    form = TeacherForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f'You edited the teacher: {request.POST.get("first_name")}']
        request.session['actions'] = actions

        action_count = request.session.get('action_count', 0)
        action_count += 1
        request.session["action_count"] = action_count

        return redirect('teacher_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'teacher/form.html', ctx)


@login_required_decorator
def teacher_delete(request, pk):
    model = Teacher.objects.get(pk=pk)
    model.delete()

    actions = request.session.get('actions', [])
    actions += [f'You deleted the teacher: {request.POST.get("first_name")}']
    request.session['actions'] = actions

    action_count = request.session.get('action_count', 0)
    action_count += 1
    request.session["action_count"] = action_count

    return redirect('teacher_list')


@login_required_decorator
def teacher_list(request):
    teachers = services.get_teacher()
    print(teachers)
    ctx = {
        'teachers': teachers
    }
    return render(request, 'teacher/list.html', ctx)


# Group
@login_required_decorator
def group_create(request):
    model = Group()
    form = GroupForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f'You created a group: {request.POST.get("name")}']
        request.session['actions'] = actions

        action_count = request.session.get('action_count', 0)
        action_count += 1
        request.session["action_count"] = action_count

        return redirect('group_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'group/form.html', ctx)


@login_required_decorator
def group_edit(request, pk):
    model = Group.objects.get(pk=pk)
    form = GroupForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f'You edited the group: {request.POST.get("name")}']
        request.session['actions'] = actions

        action_count = request.session.get('action_count', 0)
        action_count += 1
        request.session["action_count"] = action_count

        return redirect('group_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'group/form.html', ctx)


@login_required_decorator
def group_delete(request, pk):
    model = Group.objects.get(pk=pk)
    model.delete()

    actions = request.session.get('actions', [])
    actions += [f'You deleted the group: {request.POST.get("name")}']
    request.session['actions'] = actions

    action_count = request.session.get('action_count', 0)
    action_count += 1
    request.session["action_count"] = action_count

    return redirect('group_list')


@login_required_decorator
def group_list(request):
    groups = services.get_group()
    print(groups)
    ctx = {
        'groups': groups
    }
    return render(request, 'group/list.html', ctx)

# Student
@login_required_decorator
def student_create(request):
    model = Student()
    form = StudentForm(request.POST or None, request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f'You added a student: {request.POST.get("first_name")}']
        request.session['actions'] = actions

        action_count = request.session.get('action_count', 0)
        action_count += 1
        request.session["action_count"] = action_count

        return redirect('student_list')

    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'student/form.html', ctx)


@login_required_decorator
def student_edit(request, pk):
    model =Student.objects.get(pk=pk)
    form = StudentForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f'You edited the student: {request.POST.get("first_name")}']
        request.session['actions'] = actions

        action_count = request.session.get('action_count', 0)
        action_count += 1
        request.session["action_count"] = action_count

        return redirect('student_list')

    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'student/form.html', ctx)


@login_required_decorator
def student_delete(request, pk):
    model = Student.objects.get(pk=pk)
    model.delete()

    actions = request.session.get('actions', [])
    actions += [f'You deleted the student: {request.POST.get("first_name")}']
    request.session['actions'] = actions

    action_count = request.session.get('action_count', 0)
    action_count += 1
    request.session["action_count"] = action_count

    return redirect('student_list')


@login_required_decorator
def student_list(request):
    students = services.get_student()
    print(students)
    ctx = {
        'students': students
    }
    return render(request, 'student/list.html', ctx)


@login_required_decorator
def profile(request):
    return render(request, 'profile.html')


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login_page")
    template_name = "signup.html"
