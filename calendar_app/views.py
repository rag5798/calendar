# tasks/views.py

from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta

@login_required
def calendar_view(request):
    # Get today's date
    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())  # Monday
    end_of_week = start_of_week + timedelta(days=6)  # Sunday

    # Query tasks within the current week and order by task_date and task_time
    tasks = Task.objects.filter(task_date__range=[start_of_week, end_of_week]).order_by('task_date', 'task_time')

    # Initialize a dictionary to hold tasks grouped by day of the week
    tasks_by_day = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
        'Saturday': [],
        'Sunday': []
    }

    # Group tasks by day of the week
    for task in tasks:
        day_of_week = task.task_date.strftime('%A')  # Get day name (e.g., Monday)
        tasks_by_day[day_of_week].append(task)

    # Pass the grouped data to the template
    context = {
        'tasks_by_day': tasks_by_day,
        'current_month': today.strftime('%B'),
        'current_year': today.year,
        'day_dates': {  # This will show the dates for the current week
            'Monday': (start_of_week + timedelta(days=0)).strftime('%Y-%m-%d'),
            'Tuesday': (start_of_week + timedelta(days=1)).strftime('%Y-%m-%d'),
            'Wednesday': (start_of_week + timedelta(days=2)).strftime('%Y-%m-%d'),
            'Thursday': (start_of_week + timedelta(days=3)).strftime('%Y-%m-%d'),
            'Friday': (start_of_week + timedelta(days=4)).strftime('%Y-%m-%d'),
            'Saturday': (start_of_week + timedelta(days=5)).strftime('%Y-%m-%d'),
            'Sunday': (start_of_week + timedelta(days=6)).strftime('%Y-%m-%d'),
        }
    }

    return render(request, 'calendar/calendar.html', context)

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
