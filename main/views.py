from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView
from django.conf import settings
from .models import *
from django.views.decorators.csrf import csrf_exempt


def home(request):
    partners = Partner.objects.all()
    category = PartnerCategory.objects.all()
    category_1 = PartnerCategory.objects.get(id=1)
    category_2 = PartnerCategory.objects.get(id=2)
    category_3 = PartnerCategory.objects.get(id=3)
    tagline = MainTagline.objects.all()[0]
    firstline = MainTagline.objects.all()[1]
    secondline = MainTagline.objects.all()[2]
    thirdline = MainTagline.objects.all()[3]
    employees = Employees.objects.all()
    content = Content.objects.all()
    social_media = SocialMedia.objects.all()

    context = {"partners":partners, 'category_1': category_1, 'category_2': category_2, 'category_3': category_3,
               'category':category, "content":content, "tagline":tagline, "firstline":firstline,
               "secondline":secondline, "thirdline":thirdline, "employees":employees, 'social_media': social_media,
               }
    return render(request, "home.html", context)


def appeal(request):
    if request.method == 'POST':
        data = request.POST
        msg = f'Файл {data["file"]} \n Имя {data["name"]}\n' \
              f' Текст {data["message"]} \n Почта {data["email"]} \n Телефон {data["phone"]}'
        send_mail('Образец', msg, settings.EMAIL_HOST_USER, ['zhanbolot19971997@gmail.com'])
    return HttpResponseRedirect(redirect_to=reverse('home'))


def about_journal(request):
    statistic_1 = Statistic.objects.get(id=4)
    statistic_2 = Statistic.objects.get(id=2)
    statistic_3 = Statistic.objects.get(id=3)
    fourthline = MainTagline.objects.all()[4]
    fifthline = MainTagline.objects.all()[5]
    sixthline = MainTagline.objects.all()[6]
    seventhline = MainTagline.objects.all()[7]
    eightline = MainTagline.objects.all()[8]
    nineteenthline = MainTagline.objects.all()[9]
    twentythline = MainTagline.objects.all()[10]
    twentyonethline = MainTagline.objects.all()[11]

    context = {"statistic_1": statistic_1, "statistic_2": statistic_2, "statistic_3": statistic_3,
               "fourthline": fourthline, "fifthline": fifthline, "sixthline":sixthline,
               "seventhline":seventhline, "eightline":eightline, "nineteenthline":nineteenthline,
               "twentythline":twentythline, "twentyonethline":twentyonethline }

    return render(request, "about_journal.html", context)


def contacts(request):
    return render(request, "contacts.html", )


def news(request):
    news = News.objects.all()
    context = {"news":news}
    return render(request, "news.html", context)

class NewsDetail(DetailView):
    model = Articles
    template_name = "news-detail.html"
    context_object_name = 'news'
    pk_url_kwarg = 'news_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['social_media'] = SocialMedia.objects.all()
        return context


def article_releases(request):
    articles = Articles.objects.all()
    articles_archived = ArticlesArchive.objects.all()
    ninethline = MainTagline.objects.all()[12]
    tenthline = MainTagline.objects.all()[13]
    eleventhline = MainTagline.objects.all()[14]
    twelvethine = MainTagline.objects.all()[15]
    thirteenthline = MainTagline.objects.all()[16]
    fourteenthline = MainTagline.objects.all()[17]
    fifthteenthline = MainTagline.objects.all()[18]
    sixthteenthline = MainTagline.objects.all()[19]
    seventeenthline = MainTagline.objects.all()[20]
    eighteenthline = MainTagline.objects.all()[21]
    number1 = MainTagline.objects.all()[22]
    number2 = MainTagline.objects.all()[23]
    number3 = MainTagline.objects.all()[24]
    number4 = MainTagline.objects.all()[25]
    text1 = MainTagline.objects.all()[26]
    text2 = MainTagline.objects.all()[27]
    gallery = ImagesContent.objects.all()
    context = {"articles":articles, "articles_archived":articles_archived, "ninethline":ninethline,
               "tenthline":tenthline, "eleventhline":eleventhline, "twelvethine":twelvethine,
               "thirteenthline":thirteenthline, "fourteenthline":fourteenthline,
               "fifthteenthline":fifthteenthline, "sixthteenthline":sixthteenthline,
               "seventeenthline":seventeenthline, "eighteenthline":eighteenthline,
                "number1":number1, "number2":number2, "number3":number3, "number4":number4,
               "text1":text1, "text2":text2, "gallery":gallery,}
    return render(request, "article_releases.html", context )


class ArticleDetail(DetailView):
    model = Articles
    template_name = "article-releases-detail.html"
    context_object_name = 'articles'
    pk_url_kwarg = 'article_id'


class ArticleArchivedDetail(DetailView):
    model = ArticlesArchive
    template_name = "article-archived.html"
    context_object_name = 'articles_archived'
    pk_url_kwarg = 'article_archived_id'


def for_authors(request):
    category = AuthorCategory.objects.all()
    authors = Authors.objects.all()
    context = {"authors": authors, 'category': category}
    return render(request, "for_authors.html", context)


def article_article_releases(request):
    return render(request, "article-releases-detail.html", )

