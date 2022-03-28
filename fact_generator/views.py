from django.shortcuts import render

def homepage(request):
    """Homepage needs to be refactored to be a more generic landing page.
    Existing homepage should become a 'recipe nutrition' page"""
    return render(request, 'home.html')

def weight_loss_math(request):
    """Plan is for this page to hold a BMI calculator, a TDEE calculator, and graph that will allow users to plot
    approximately how long it will take to achieve their goal weight with a specified calorie deficit"""
    return render(request, 'bmi.html')
