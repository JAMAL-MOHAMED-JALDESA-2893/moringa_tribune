from django.shortcuts import render
from django.http  import HttpResponse,Http404
import datetime as dt
from django.shortcuts import render,redirect


# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

# Create your views here.

def news_of_day(request):
    date = dt.date.today()
    html = f'''
        <html>
            <body>
                <p>todays date</p>
                <h1>{date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)





def news_of_day(request):
    date = dt.date.today()
    return render(request, 'all-news/today-news.html', {"date": date,})



# View Function to present news from past days
def past_days_news(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_of_day)

    return render(request, 'all-news/past-news.html', {"date": date})