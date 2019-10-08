from django.shortcuts import render

from fib_calculator.utils import cal_fib_num
from .form import FibInputForm


# Create your views here.
def fib_input_view(request):
    form = FibInputForm()
    return render(request, 'fib_calculator/form.html', {'form': form})


def output(request):
    if request.method == 'POST':
        form = FibInputForm(request.POST)
        if form.is_valid():
            num = form.cleaned_data['num_field']
            fib_num = cal_fib_num(num)
            return render(request, 'fib_calculator/output.html', {'fib_num': fib_num})
        else:
            return render(request, 'fib_calculator/form.html', {'form': form})
