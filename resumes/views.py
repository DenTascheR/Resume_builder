from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Resume
from .forms import ResumeForm

@login_required
def resume_list(request):
    resumes = Resume.objects.filter(user=request.user)
    return render(request, 'resume/resume_list.html', {'resumes': resumes})

@login_required
def resume_create(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            return redirect('resume_list')
    else:
        form = ResumeForm()
    return render(request, 'resume/resume_form.html', {'form': form})

@login_required
def resume_edit(request, pk):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            return redirect('resume_list')
    else:
        form = ResumeForm(instance=resume)
    return render(request, 'resume/resume_form.html', {'form': form})

@login_required
def resume_delete(request, pk):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    if request.method == 'POST':
        resume.delete()
        return redirect('resume_list')
    return render(request, 'resume/resume_confirm_delete.html', {'resume': resume})
