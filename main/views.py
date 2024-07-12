from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from goods.models import Categories


class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'ТОВ "ТЕНДЕР-ПАК" - Головна'
        context["content"] = "Виробництво гофрокартону та виробів з нього"
        return context


# def index(request):


#     context = {
#         'title': 'Home - Главная',
#         'content': "Магазин мебели HOME",
#     }

#     return render(request, 'main/index.html', context)


class AboutView(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'ТОВ "ТЕНДЕР-ПАК" - Про нас'
        context["content"] = "Про нас"
        context["text_on_page"] = (
            "ТОВ ТЕНДЕР-ПАК засновано у липні 2008 року, саме в цей час було придбано та введено в експлуатацію лінію з виробництва гофрованого картону ЛГК-140. Наша компанія розпочала свою роботу з невеликого цеху в Подільському районі міста Києва./"
            "Для перероблення гофрокартонна використовували рольові преси РП-1790, на той момент, на підприємстві їх було лише два. Саме цього року було випущено перший метр гофрованого картону та висічено першу партію пакування./"
            "З початку роботи, компанія обрала стратегію постійного розвитку шляхом придбання і запуску нового устаткування, постійного поліпшення якості своєї продукції, оскільки якість продукції залежить від якості устаткування, на якому вона випускається. Саме цей вибір стратегічного розвитку підприємства не змусив довго чекати на певні успіхи компанії. Вже наступного року було придбано та введено в експлуатацію верстат ротаційного висікання РС - 4М – призначений для висікання виробів складної конфігурації. Верстат МФ-5 призначений для нанесення флексографічного друку на гофрокартон. Було запущено та введено в експлуатацію сучасне обладнання для пакування готової продукції. У 2013 році, з початком кризи, компанія переносить свої виробничі потужності за межі Києва, значно збільшивши площу виробничих і складських приміщень, що в результаті для підприємства стало черговим етапом розвитку./"
        ).replace("/", "<br><br>")
        return context


class ContactView(TemplateView):
    template_name = "main/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'ТОВ "ТЕНДЕР ПАК" - Контактна інформація '
        context["content"] = "Контактна інформація"
        return context


# def about(request):
#     context = {
#         "title": "Home - О нас",
#         "content": "О нас",
#         "text_on_page": "Текст о том почему этот магазин такой классный, и какой хороший товар.",
#     }

#     return render(request, "main/about.html", context)
