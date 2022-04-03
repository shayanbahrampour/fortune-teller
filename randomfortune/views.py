from django.shortcuts import render
import random
from django.http import HttpResponse

# Create your views here.
fortunelist=[
  "You Are Great",
  "You Are Gonna Make It",
  "You Are The Best",
  "The World is waiting for you",
  "All will go well with your new project.",
   "If you continually give, you will continually have.",
   "Self-knowledge is a life long process.",
   "You are busy, but you are happy.",
   "Your abilities are unparalleled.",
   "Those who care will make the effort.",
   "Now is the time to try something new.",
   "Miles are covered one step at a time.",
   "Don’t just think, act!"
]


def fortune(request):
    context = {
        "fortune": random.choice(fortunelist)
    }
    return render(request,r"F:\projects\fortune-teller\randomfortune\templates\fortune.html",context)
