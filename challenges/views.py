from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


monthly_challenges = {
    "january": 'Eat no meat for the entire month!',
    "february": "Walk at least 20m every day",
    "march": "Learn Django for at least 20m every day",
    "april": 'Eat no meat for the entire april month!',
    "may": "Walk at least 20m every day of MAY",
    "june": 'Eat no meat for the entire month of JUNE!',
    "july": 'Eat no meat for the entire month of JULY!',
    "august": "Walk at least 20m every day of AUGUST",
    "september": "Learn Django for at least 20m every day of september",
    "october": 'Eat no meat for the entire october month!',
    "november": "Walk at least 20m every day of november",
    "december": "Walk at least 20m every day of december"
}

months = list(monthly_challenges.keys())


def index(request):



    months_buttons = list(map(
        lambda month: f"""
            <li>
                <a href={reverse('month-challenge', args=[month])}>{month.capitalize()}</a>
            </li>
        """, months))

    html = f"""
        <nav>
            <ul>
               {''.join(months_buttons)} 
            </ul>
        </nav>
    """
    
    return HttpResponse(html)


def monthly_challenge_by_number(request, month):

    if month > len(months) or month < 0:
        return HttpResponseNotFound("This month is not suported")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])

    # return HttpResponseRedirect(redirect_month)
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):

    try:
        challenge_text = monthly_challenges[month]

        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month is not suported")
