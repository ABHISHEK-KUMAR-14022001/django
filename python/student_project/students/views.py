from django.shortcuts import render, redirect
from .forms import StudentForm

def student_form(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to success page
    else:
        form = StudentForm()

    return render(request, 'students/student_form.html', {'form': form})

def success_page(request):
    return render(request, 'students/success.html')
