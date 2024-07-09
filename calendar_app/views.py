# tasks/views.py

from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required
def calendar_view(request):
    # Query all tasks from your database
    tasks = Task.objects.all()

    # Initialize a dictionary to hold tasks grouped by day of the week
    tasks_by_day = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
        'Saturday': [],
        'Sunday': [],
    }

    # Group tasks by day of the week
    for task in tasks:
        day_of_week = task.task_date.strftime('%A')  # Get day name (e.g., Monday)
        tasks_by_day[day_of_week].append(task)

    # Pass the grouped data to the template
    return render(request, 'calendar/calendar.html', {'tasks_by_day': tasks_by_day})

@login_required
def add_task_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('calendar')
    else:
        form = TaskForm()
    return render(request, 'calendar/add_task.html', {'form': form})
