from django.shortcuts import render

from Cow_app.models import CowText
from Cow_app.forms import CowTextForm
import subprocess


# Create your views here.
def index(request):
    if request.method == "POST":
        form = CowTextForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form = CowTextForm()
            CowText.objects.create(
                text=data['text'],
            )
            cowsay_input = subprocess.run(
                ['cowsay'] + data['text'].split(), capture_output=True
            ).stdout.decode()

        return render(request, 'index.html', {'cowsay_input': cowsay_input,
                                              "form": form})
    form = CowTextForm()
    return render(request, 'index.html', {'form': form})


def History(request):
    cowsay_history = list(CowText.objects.all())
    History = cowsay_history[-10:][::-1]

    return render(request, 'history.html', {'History': History})
