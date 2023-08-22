# -*- coding: UTF-8 -*-[32;64;19M

from .forms import *
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse
# from md5 import md5
from django.http import HttpResponse
import random
# import base64,md5
from datetime import datetime
from time import sleep
import calendar
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import hashlib
import random as random_number
from django.db.models import Q
from django.contrib.sessions.models import Session
import json
import xlrd
from django.forms.models import model_to_dict
from django.contrib import messages
import pymorphy3

morph = pymorphy3.MorphAnalyzer()


def unigramma(text):
    text = text.lower()
    podgotovka = text.split(' ')
    text1 = ''
    for i in range(len(podgotovka)):
        s1 = "".join(c for c in podgotovka[i] if c.isalpha())
        podgotovka[i] = morph.parse(s1)[0].normal_form
        text1 += podgotovka[i]
        if i != len(podgotovka) - 1:
            text1 += ' '
        s1 = ""
    return text1


def proba(request):
    reslog1 = None
    if request.method == 'POST':  # If the form has been submitted...
        #        return HttpResponse("CheckPoint_A1")

        if 'quest' in request.POST and request.POST['quest']:
            kod = request.POST['quest']
            if len(kod) > 15:  # Нажата кнопка "Ответить на вопрос"
                q_list = request.session['q_list']
                page1 = request.session['start']
                res_test_num = request.session['res_test_num']
                reslog1 = request.session['reslog1']
                reslog1.res_test_num = res_test_num[page1 - 1]
                (q, q_a, q_b) = q_list[page1 - 1]
                reslog1.quest_typ = q['quest_type']
                reslog1.quest_num = int(q['quest_num'])
                is_ans = request.session['is_ans']
                is_ans[page1 - 1] = 1
                request.session['is_ans'] = is_ans
                #                html = "<html><body>Now: %s. </body></html>" % q['answer']
                #                return HttpResponse(html)

                if q['quest_type'] == 1:
                    quest_answ = []
                    quest_answ_ok = []
                    if 'Radio' in request.POST.keys():
                        ans_f = request.POST.get('Radio', 123)
                    ii = 0
                    for a in q_a:
                        ii = ii + 1
                        quest_answ_ok.append(int(a['ok']))
                        if int(ans_f) == int(a['answer_num']):
                            quest_answ.append(1)
                            a['ans'] = 1
                        else:
                            quest_answ.append(0)
                            a['ans'] = 0
                    if quest_answ == quest_answ_ok:
                        reslog1.ball = 1
                    else:
                        reslog1.ball = 0
                    reslog1.answer = "".join([str(i) for i in quest_answ])
                    if reslog1.ball == 1:
                        messages.info(request, "Правильно!")
                    else:
                        messages.info(request, "Неправильно!")

                if q['quest_type'] == 2:
                    quest_answ = ""
                    quest_answ_ok = []
                    ans_f = []
                    if 'Radio' in request.POST.keys():
                        ans_f = request.POST.getlist('Radio')
                    ii = 1
                    for a in q_a:
                        a['ans'] = 0
                        if int(a['ok']) == 1:
                            iii = 0
                            for b in ans_f:
                                if int(b) == int(a['answer_num']):
                                    a['ans'] = 1
                                    iii = 1
                            if iii == 0:
                                ii = 0
                        if int(a['ok']) == 0:
                            iii = 1
                            for b in ans_f:
                                if int(b) == int(a['answer_num']):
                                    a['ans'] = 1
                                    iii = 0
                            if iii == 0:
                                ii = 0
                        quest_answ = quest_answ + str(a['ans'])
                    if int(ii) == 1:
                        reslog1.ball = 1
                    else:
                        reslog1.ball = -1
                    reslog1.answer = quest_answ
                    if reslog1.ball == 1:
                        messages.info(request, "Правильно!")
                    else:
                        messages.info(request, "Неправильно!")

                if q['quest_type'] == 3:
                    quest_answ = []
                    quest_answ_ok = []
                    ans_f = []
                    if 'Radio' in request.POST.keys():
                        ans_f = request.POST.get('Radio', 123)
                    reslog1.ball = -1
                    try:
                        tmp = int(ans_f)
                    except:
                        return HttpResponse(
                            "<html><body><H1>Ваш ответ не является целым числом. Вернитесь на предыдущую страницу и введите ответ в виде целого числа!</H1></body></html>")
                    for i in q['answer']:
                        if i == ans_f:
                            reslog1.ball = 1
                    quest_answ = ans_f
                    reslog1.answer = quest_answ
                    q['quest_answer'] = quest_answ
                    if reslog1.ball == 1:
                        messages.info(request, "Правильно!")
                    else:
                        messages.info(request, "Неправильно!")

                if q['quest_type'] == 4:
                    quest_answ = []
                    quest_answ_ok = []
                    ans_f = []
                    if 'Radio' in request.POST.keys():
                        ans_f = request.POST.get('Radio', 123)
                    reslog1.ball = -1
                    for i in q['answer']:
                        if unigramma(ans_f).find(unigramma(i)) >= 0:
                            reslog1.ball = 1
                    quest_answ = ans_f
                    reslog1.answer = quest_answ
                    q['quest_answer'] = quest_answ
                    if reslog1.ball == 1:
                        messages.info(request, "Правильно!")
                    else:
                        messages.info(request, "Неправильно!")

                if q['quest_type'] == 5:
                    quest_answ = []
                    quest_answ_ok = []
                    ans_f = []
                    if 'Radio' in request.POST.keys():
                        ans_f = request.POST.get('Radio', 123)
                    reslog1.ball = -1
                    Kol_All = 0
                    Kol_I = 0
                    for i in q['answer']:
                        Kol_All = Kol_All + 1
                        if unigramma(ans_f).find(unigramma(i)) >= 0:
                            Kol_I = Kol_I + 1

                    html = "<html><body>Now %s. </body></html>" % Kol_All, Kol_I
                    return HttpResponse(html)

                    if (Kol_I / Kol_All) > 0.49:
                        reslog1.ball = 1
                    quest_answ = ans_f
                    reslog1.answer = quest_answ
                    q['quest_answer'] = quest_answ
                    if reslog1.ball == 1:
                        messages.info(request, "Правильно!")
                    else:
                        messages.info(request, "Неправильно!")

                #                reslog1.save()
                request.session['page'] = page1
            else:
                if 'q_list' in request.session:
                    del request.session['q_list']
                return HttpResponseRedirect('student')

    if 'q_list' not in request.session:  # Формирование набора заданий теста из БТЗ
        quest_1 = []
        quest = []
        quest_list = []
        q_list = []
        proba = []
        quest_1 = T121Quest.objects.using('exam').filter(baza_num=1).values('quest_num', 'quest_type', 'quest_text',
                                                              'quest_text_etalon', 'answer', 'answer_kol', 'quest_type')

        for i in quest_1:
            quest_2 = []
            ans_l = T122Answer.objects.using('exam').filter(quest_num=i['quest_num']).exclude(answer_type=15).order_by('?').values(
                'answer_num', 'answer_type', 'answer_text', 'ok', 'AnswerID', 'ans')
            ans_l_2 = []

            if (i['quest_type'] == 1) or (i['quest_type'] == 2):
                quest_answ = ""
                for a in ans_l:
                    quest_answ = quest_answ + str(a['ok'])
                i['answer'] = str(quest_answ)

            if i['quest_type'] == 3:
                answer_1 = []
                answer_2 = ""
                answer_3 = []
                for a in ans_l:
                    answer_1.append(a['answer_text'])
                i['answer'] = answer_1
                i['quest_answer'] = str('')

            if i['quest_type'] == 4:
                answer_1 = []
                answer_2 = ""
                answer_3 = []
                for a in ans_l:
                    answer_1.append(a['answer_text'])
                i['answer'] = answer_1
                i['quest_answer'] = str('')

            if i['quest_type'] == 5:
                answer_1 = []
                answer_2 = ""
                answer_3 = []
                for a in ans_l:
                    answer_1.append(a['answer_text'])
                i['answer'] = answer_1
                i['quest_answer'] = str('')

            a_l = []
            quest_2.append(i)
            for a in ans_l:
                a_l.append(a)
            quest_2.append(a_l)
            #######            quest_2.append(ans_l)
            quest_2.append(ans_l_2)
            q_list.append(quest_2)

        #        return HttpResponse("CheckPoint")
        #        html = "<html><body>Now: %s. </body></html>" % q_list
        #        return HttpResponse(html)

        test1 = T126Test(stud_num=1, plan_num=1, baza_num=1, mark=-1, time=datetime.now(),
                         ipaddr=request.META['REMOTE_ADDR'])
        #        test1.save()
        res_test_num = []
        is_ans = []
        for q, q_a, q_b in q_list:
            quest_answ = []
            if (q['quest_type'] == 2) or (q['quest_type'] == 3):
                #                quest_answ = []
                i = 0
                for a in q_a:
                    i = i + 1
                    quest_answ.append(0)
            #                q['answer'] = quest_answ

            #            if q['quest_type']>3:
            #                quest_answ = q['answer']

            reslog1 = T127ResTest(test_num=1, ball=-2, quest_num=q['quest_num'],
                                  answer="".join([str(i) for i in quest_answ]), quest_typ=q['quest_type'])
            #            reslog1.save()
            res_test_num.append(1)
            is_ans.append(0)

        if 'quest' in request.session:
            del request.session['quest']
        request.session['q_list'] = q_list
        request.session['test1'] = test1
        request.session['reslog1'] = reslog1
        request.session['res_test_num'] = res_test_num
        request.session['is_ans'] = is_ans
        request.session['page'] = 1
    else:
        q_list = request.session['q_list']

    #    return HttpResponseRedirect('result_proba') # Redirect after POST

    if 'is_ans' in request.session:
        is_ans = request.session['is_ans']
    else:
        is_ans = []
    objects = q_list
    paginator = Paginator(objects, 1)
    if 'page' in request.GET:
        page = int(request.GET.get('page', 1))
    else:
        page = request.session['page']
    request.session['start'] = page
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'test.html', {'quest_list': contacts, 'page': page, 'is_ans': is_ans})


def result_kag(request):
    #    return HttpResponse('result Кагалым')
    if 'stud' in request.session:
        stud = request.session['stud']
    else:
        return HttpResponseRedirect('student')
    if 'plan' in request.session:
        plan = request.session['plan']
    #        html = "<html><body>Now %s. </body></html>" % plan[0].fam
    #        return HttpResponse(html)
    else:
        return HttpResponseRedirect('student')
    if 'q_list' in request.session:
        q_list = request.session['q_list']
    else:
        return HttpResponseRedirect('student')
    if 'parol' in request.session:
        kod = request.session['parol']
    if 'baza' in request.session:
        baza_num = request.session['baza']
    else:
        return HttpResponseRedirect('student')
    res_list = T126Test.objects.using('exam').filter(stud_num=stud, baza_num=baza_num).order_by('-time')[0:1]
    result_list = T127ResTest.objects.using('exam').filter(
        test_num=res_list[0].test_num)  # .order_by('test_date','test_time')
    d = 0
    for det in result_list:
        d_q = T121Quest.objects.using('exam').filter(quest_num=det.quest_num)
        d_qq = d_q[0]
        if det.ball > 0:
            d = d + 1
    del request.session['stud']
    del request.session['q_list']
    p = T125Parol.objects.using('exam').filter(password=kod).update(trying=1)
    kod_3 = 123321
    if request.method == 'POST':  # If the form has been submitted...
        if 'output' in request.POST and request.POST['output']:
            return HttpResponseRedirect('student')
    return render(request, 'result_kag.html', {'plan': plan[0], 'd': d, 'res_list': res_list, 'fam': plan[0].fam})


def kagalym(request):
    if 'parol' in request.session:
        parol = request.session['parol']
    else:
        return HttpResponseRedirect('student')
    if 'stud' in request.session:
        stud = request.session['stud']
    else:
        return HttpResponseRedirect('student')
    if 'plan' in request.session:
        plan = request.session['plan']
    else:
        return HttpResponseRedirect('student')
    proc = get_object_or_404(T125Plan, plan_num=plan[0].plan_num)
    if proc.processed != 1:
        return HttpResponseRedirect('result_kag')
    if request.method == 'POST':  # If the form has been submitted...
        if 'quest' in request.POST and request.POST['quest']:
            kod = request.POST['quest']
            if len(kod) > 15:  # Нажата кнопка "Ответить на вопрос"
                q_list = request.session['q_list']
                page1 = request.session['start']
                test1 = request.session['test1']
                res_test_num = request.session['res_test_num']
                reslog1 = request.session['reslog1']
                reslog1.res_test_num = res_test_num[page1 - 1]

                #                html = "<html><body>Now %s. </body></html>" % reslog1.res_test_num
                #                return HttpResponse(html)

                (q, q_a, q_b) = q_list[page1 - 1]
                reslog1.quest_typ = q['quest_type']
                reslog1.quest_num = int(q['quest_num'])
                is_ans = request.session['is_ans']
                is_ans[page1 - 1] = 1
                request.session['is_ans'] = is_ans

                if q['quest_type'] == 1:
                    quest_answ = []
                    quest_answ_ok = []
                    if 'Radio' in request.POST.keys():
                        ans_f = request.POST.get('Radio', 123)
                    ii = 0
                    for a in q_a:
                        ii = ii + 1
                        quest_answ_ok.append(int(a['ok']))
                        if int(ans_f) == int(a['answer_num']):
                            quest_answ.append(1)
                            a['ans'] = 1
                        else:
                            quest_answ.append(0)
                            a['ans'] = 0
                    if quest_answ == quest_answ_ok:
                        reslog1.ball = 1
                    else:
                        reslog1.ball = 0
                    reslog1.answer = "".join([str(i) for i in quest_answ])
                    if reslog1.ball == 1:
                        messages.info(request, "Правильно!")
                    else:
                        messages.info(request, "Неправильно!")

                if q['quest_type'] == 2:
                    quest_answ = ""
                    quest_answ_ok = []
                    ans_f = []
                    if 'Radio' in request.POST.keys():
                        ans_f = request.POST.getlist('Radio')
                    ii = 1
                    for a in q_a:
                        a['ans'] = 0
                        if int(a['ok']) == 1:
                            iii = 0
                            for b in ans_f:
                                if int(b) == int(a['answer_num']):
                                    a['ans'] = 1
                                    iii = 1
                            if iii == 0:
                                ii = 0
                        if int(a['ok']) == 0:
                            iii = 1
                            for b in ans_f:
                                if int(b) == int(a['answer_num']):
                                    a['ans'] = 1
                                    iii = 0
                            if iii == 0:
                                ii = 0
                        quest_answ = quest_answ + str(a['ans'])
                    if int(ii) == 1:
                        reslog1.ball = 1
                    else:
                        reslog1.ball = -1
                    reslog1.answer = quest_answ
                    if reslog1.ball == 1:
                        messages.info(request, "Правильно!")
                    else:
                        messages.info(request, "Неправильно!")

                if q['quest_type'] == 3:
                    quest_answ = []
                    quest_answ_ok = []
                    ans_f = []
                    if 'Radio' in request.POST.keys():
                        ans_f = request.POST.get('Radio', 123)
                    reslog1.ball = -1
                    try:
                        tmp = int(ans_f)
                    except:
                        return HttpResponse(
                            "<html><body><H1>Ваш ответ не является целым числом. Вернитесь на предыдущую страницу и введите ответ в виде целого числа!</H1></body></html>")
                    for i in q['answer']:
                        if i == ans_f:
                            reslog1.ball = 1
                    quest_answ = ans_f
                    reslog1.answer = quest_answ
                    q['quest_answer'] = quest_answ
                    if reslog1.ball == 1:
                        messages.info(request, "Правильно!")
                    else:
                        messages.info(request, "Неправильно!")

                if q['quest_type'] == 4:
                    quest_answ = []
                    quest_answ_ok = []
                    ans_f = []
                    if 'Radio' in request.POST.keys():
                        ans_f = request.POST.get('Radio', 123)
                    reslog1.ball = -1
                    for i in q['answer']:
                        if unigramma(ans_f).find(unigramma(i)) >= 0:
                            reslog1.ball = 1
                    quest_answ = ans_f
                    reslog1.answer = quest_answ
                    q['quest_answer'] = quest_answ
                    if reslog1.ball == 1:
                        messages.info(request, "Правильно!")
                    else:
                        messages.info(request, "Неправильно!")

                if q['quest_type'] == 5:
                    quest_answ = []
                    quest_answ_ok = []
                    ans_f = []
                    if 'Radio' in request.POST.keys():
                        ans_f = request.POST.get('Radio', 123)
                    reslog1.ball = -1
                    Kol_All = 0
                    Kol_I = 0
                    for i in q['answer']:
                        Kol_All = Kol_All + 1
                        if unigramma(ans_f).find(unigramma(i)) >= 0:
                            Kol_I = Kol_I + 1
                    #                    html = "<html><body>Now %s. </body></html>" % Kol_All, Kol_I
                    #                    return HttpResponse(html)
                    if (Kol_I / Kol_All) > 0.49:
                        reslog1.ball = 1
                    quest_answ = ans_f
                    reslog1.answer = quest_answ
                    q['quest_answer'] = quest_answ
                    if reslog1.ball == 1:
                        messages.info(request, "Правильно!")
                    else:
                        messages.info(request, "Неправильно!")

                #                html = "<html><body>Now %s. </body></html>" % reslog1.ball
                #                return HttpResponse(html)

                reslog1.save()
                mark = 0
                for re in T127ResTest.objects.using('exam').filter(test_num=test1.test_num):
                    mark = mark + re.ball
                test1.mark = mark
                test1.save()
                request.session['page'] = page1
            else:
                return HttpResponseRedirect('result_kag')  # Redirect after POST

    #                            html = "<html><body>Now %s. </body></html>" % ans_f
    #                            return HttpResponse(html)

    if 'q_list' not in request.session:  # Формирование набора заданий теста из БТЗ
        session_key = request.session.session_key
        baza_num = request.session['baza']
        stud = request.session['stud']
        testing = T125Testing.objects.using('exam').filter(session_code=session_key, parol=parol)
        if not testing.exists():
            html = "<html><body>Now: %s. </body></html>" % session_key
            return HttpResponse(html)
        quest = []
        quest_list = []
        q_list = []
        proba = []
        formula_1 = T120Formula.objects.using('exam').filter(baza_num=baza_num).values('quest_type', 'quest_col', 'quest_time')
        for j in formula_1:
            quest_1 = T121Quest.objects.using('exam').filter(baza_num=baza_num, quest_type=j['quest_type']).order_by('?').values(
                'quest_num', 'quest_type', 'quest_text', 'quest_text_etalon', 'answer', 'answer_kol', 'quest_type')[
                      0:j['quest_col']]
            for i in quest_1:
                quest_2 = []
                ans_l = T122Answer.objects.using('exam').filter(quest_num=i['quest_num']).exclude(answer_type=15).order_by(
                    '?').values('answer_num', 'answer_type', 'answer_text', 'ok', 'AnswerID', 'ans')

                #                html = "<html><body>Now: %s. </body></html>" % ans_l[0]
                #                return HttpResponse(html)

                ans_l_2 = []

                if (i['quest_type'] == 1) or (i['quest_type'] == 2):
                    quest_answ = ""
                    for a in ans_l:
                        quest_answ = quest_answ + str(a['ok'])
                    i['answer'] = str(quest_answ)

                if i['quest_type'] == 3:
                    answer_1 = []
                    answer_2 = ""
                    answer_3 = []
                    for a in ans_l:
                        answer_1.append(a['answer_text'])
                    i['answer'] = answer_1
                    i['quest_answer'] = str('')

                if i['quest_type'] == 4:
                    answer_1 = []
                    answer_2 = ""
                    answer_3 = []
                    for a in ans_l:
                        answer_1.append(a['answer_text'])
                    i['answer'] = answer_1
                    i['quest_answer'] = str('')

                if i['quest_type'] == 5:
                    answer_1 = []
                    answer_2 = ""
                    answer_3 = []
                    for a in ans_l:
                        answer_1.append(a['answer_text'])
                    i['answer'] = answer_1
                    i['quest_answer'] = str('')

                a_l = []
                quest_2.append(i)
                for a in ans_l:
                    a_l.append(a)
                quest_2.append(a_l)
                #######                quest_2.append(ans_l)
                quest_2.append(ans_l_2)
                q_list.append(quest_2)

        #        return HttpResponse("CheckPoint")
        #        html = "<html><body>Now: %s. </body></html>" % q_list
        #        return HttpResponse(html)

        #        test1 = T126Test(stud_num=1, plan_num=1, baza_num=1, mark=-1, time=datetime.now(), ipaddr=request.META['REMOTE_ADDR'])
        test1 = T126Test(stud_num=stud, plan_num=plan[0].plan_num, baza_num=baza_num, mark=-1, time=datetime.now(),
                         ipaddr=request.META['REMOTE_ADDR'])
        test1.save()
        res_test_num = []
        is_ans = []
        for q, q_a, q_b in q_list:
            quest_answ = []
            if (q['quest_type'] == 1) or (q['quest_type'] == 2):
                quest_answ = []
                i = 0
                for a in q_a:
                    i = i + 1
                    quest_answ.append(0)
            #                q['answer'] = quest_answ

            #            if q['quest_type']>2:
            #                quest_answ = q['answer']

            #            reslog1 = T127ResTest(test_num=1, ball=-2, quest_num=q['quest_num'], answer="".join([str(i) for i in quest_answ]), quest_typ=q['quest_type'])
            reslog1 = T127ResTest(test_num=test1.test_num, ball=0, quest_num=q['quest_num'],
                                  answer="".join([str(i) for i in quest_answ]), quest_typ=q['quest_type'])
            reslog1.save()
            res_test_num.append(int(reslog1.res_test_num))
            is_ans.append(0)

        if 'quest' in request.session:
            del request.session['quest']
        request.session['q_list'] = q_list
        request.session['test1'] = test1
        request.session['reslog1'] = reslog1
        request.session['res_test_num'] = res_test_num
        request.session['is_ans'] = is_ans
        request.session['page'] = 1
    else:
        q_list = request.session['q_list']

    #    return HttpResponseRedirect('/result_proba/') # Redirect after POST

    if 'is_ans' in request.session:
        is_ans = request.session['is_ans']
    else:
        is_ans = []
    objects = q_list
    paginator = Paginator(objects, 1)
    if 'page' in request.GET:
        page = int(request.GET.get('page', 1))
    else:
        page = request.session['page']
    request.session['start'] = page
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'test.html', {'quest_list': contacts, 'page': page, 'is_ans': is_ans})


def student(request):
    if request.method == 'POST':
        form = code_form(request.POST)
        if form.is_valid():
            if 'code' in request.POST and request.POST['code']:
                kod = str(request.POST['code'])
                if str(kod) == str(123456789):
                    if 'q_list' in request.session:
                        del request.session['q_list']
                    return HttpResponseRedirect('proba')  # Redirect after POST

            request.session['fiction'] = "fiction"

            plan = T125Parol.objects.using('exam').filter(password=kod)
            if plan.exists():
                if plan[0].trying == 1:
                    html = "<html><body><H1>Вы уже прошли тестирование!  </H1></body></html>"
                    return HttpResponse(html)
                process = T125Plan.objects.using('exam').filter(plan_num=plan[0].plan_num)
                session_key = request.session.session_key
                session = T125Session.objects.using('exam').filter(parol=kod).order_by('-session_num')
                if not session.exists():
                    add = 0
                else:
                    session = T125Session.objects.using('exam').all().order_by('-session_num')
                    if session[0].parol != kod:
                        add = 1
                    else:
                        add = 2
                session1 = T125Session(parol=kod, plan_num=process[0].plan_num, processed=process[0].processed,
                                       trying=plan[0].trying, attempt=add, datetime_v=datetime.now(),
                                       ip_address=request.META['REMOTE_ADDR'], session_code=session_key)
                session1.save()
                sleep(1)
                session = T125Session.objects.using('exam').filter(session_code=session_key, parol=kod).order_by('-session_num')
                if add < 2:
                    if 'q_list' in request.session:
                        del request.session['q_list']
                    stud = plan[0].stud_num
                    request.session['stud'] = stud
                    request.session['plan'] = plan
                    request.session['parol'] = kod
                    request.session['baza'] = process[0].baza_num

            else:
                html = "<html><body><H1>Введен недействительный пароль! Вернитесь на предыдущую страницу и введите правильный пароль!  </H1></body></html>"
                return HttpResponse(html)

            if process[0].processed != 1:
                html = "<html><body><H1>Тестирование не разрешено! Вернитесь на предыдущую страницу и дождитесь указания тестолога!  </H1></body></html>"
                return HttpResponse(html)
            #                return HttpResponseRedirect('student')

            saving = 1
            try:
                testing1 = T125Testing(parol=kod, plan_num=process[0].plan_num, repeating=0,
                                       processed=process[0].processed, trying=plan[0].trying, attempt=add,
                                       datetime_v=datetime.now(), ip_address=request.META['REMOTE_ADDR'],
                                       session_code=session_key)
                testing1.save()
                sleep(1)
            except:
                saving = 0

            if process[0].baza_num == 1:
                return HttpResponseRedirect('kagalym')

            return HttpResponseRedirect('student')
    else:
        form = code_form()
    return render(request, 'code.html', {'form': form, })


def begin(request):
    if request.method == 'POST':
        form = question_form(request.POST)
        if form.is_valid():
            if 'key_1' in request.POST and request.POST['key_1']:
                key_1 = request.POST['key_1']
            if 'key_2' in request.POST and request.POST['key_2']:
                key_2 = request.POST['key_2']
            if 'key_3' in request.POST and request.POST['key_3']:
                key_3 = request.POST['key_3']
            if 'answer' in request.POST and request.POST['answer']:
                answer = request.POST['answer']
            request.session['key_1'] = key_1
            html = "<html><body>Now %s </body></html>" % key_1, key_2, key_3, answer
            return HttpResponse(html)
    else:
        form = question_form()
    return render(request, 'question.html', {'form': form, })


def admin_code(request):
    if request.method == 'POST':
        form = code_form(request.POST)
        if form.is_valid():
            if 'code' in request.POST and request.POST['code']:
                kod = request.POST['code']
            prepods = []
            request.session['prepods'] = prepods
            str_h = str(kod.encode("UTF-8"))
            p = hashlib.sha1(str_h.encode("UTF-8")).hexdigest()
            p_md = p + 'q1w2e3r4t5y6'
            p_md_md = hashlib.sha1(p_md.encode("UTF-8")).hexdigest()
            admin = T190Admin.objects.using('exam').filter(pass_md5=p_md_md)
            if not admin.exists():
                return HttpResponseRedirect('admin_code')
            if admin[0].priv_num == 0:
                request.session['fam'] = admin[0].fam
                request.session['imya'] = admin[0].imya
                request.session['otch'] = admin[0].otch
                request.session['adm'] = 123
                return HttpResponseRedirect('superadmin')
            if admin[0].priv_num == 1:
                request.session['fam'] = admin[0].fam
                request.session['imya'] = admin[0].imya
                request.session['otch'] = admin[0].otch
                request.session['adm'] = 123
                return HttpResponseRedirect('admin')
            html = "<html><body>Now %s </body></html>" % admin.fam
            return HttpResponse(html)
    else:
        form = code_form()
    return render(request, 'admin_code.html', {'form': form, })


def superadmin(request):
    #    return HttpResponse("CheckPoint SUPER")
    if 'adm' in request.session:
        adm = request.session['adm']
    else:
        if 'fam' in request.session:
            del request.session['fam']
        if 'imya' in request.session:
            del request.session['imya']
        if 'otch' in request.session:
            del request.session['otch']
        return HttpResponseRedirect('admin_code')
    if 'fam' in request.session:
        fam = request.session['fam']
    else:
        return HttpResponseRedirect('admin_code')
    if 'imya' in request.session:
        imya = request.session['imya']
    else:
        return HttpResponseRedirect('admin_code')
    if 'otch' in request.session:
        otch = request.session['otch']
    else:
        return HttpResponseRedirect('admin_code')
    sadmin = T190Admin.objects.using('exam').filter(priv_num=0)
    admin = T190Admin.objects.using('exam').filter(priv_num=1)
    if request.method == 'POST':  # If the form has been submitted...
        if 'insert' in request.POST and request.POST['insert']:
            return HttpResponseRedirect('admin_insert')
    if request.method == 'POST':  # If the form has been submitted...
        if 'edit_admin' in request.POST and request.POST['edit_admin']:
            a_num = request.POST['edit_admin']
            request.session['a_num'] = a_num
            return HttpResponseRedirect('admin_edit')
    if request.method == 'POST':  # If the form has been submitted...
        if 'edit_sadmin' in request.POST and request.POST['edit_sadmin']:
            return HttpResponseRedirect('sadmin_edit')
    if request.method == 'POST':  # If the form has been submitted...
        if 'del_admin' in request.POST and request.POST['del_admin']:
            a_num = request.POST['del_admin']
            p = T190Admin.objects.using('exam').filter(admin_num=a_num).delete()
            return HttpResponseRedirect('superadmin')
    if request.method == 'POST':  # If the form has been submitted...
        if 'output' in request.POST and request.POST['output']:
            if 'fam' in request.session:
                del request.session['fam']
            if 'imya' in request.session:
                del request.session['imya']
            if 'otch' in request.session:
                del request.session['otch']
            if 'adm' in request.session:
                del request.session['adm']
            return HttpResponseRedirect('admin_code')
    return render(request, 'superadmin.html',
                  {'sadmin': sadmin, 'admin': admin, 'fam': fam, 'imya': imya, 'otch': otch})


def admin(request):
    if 'adm' in request.session:
        adm = request.session['adm']
    else:
        if 'fam' in request.session:
            del request.session['fam']
        if 'imya' in request.session:
            del request.session['imya']
        if 'otch' in request.session:
            del request.session['otch']
        return HttpResponseRedirect('admin_code')
    if 'fam' in request.session:
        fam = request.session['fam']
    else:
        return HttpResponseRedirect('admin_code')
    if 'imya' in request.session:
        imya = request.session['imya']
    else:
        return HttpResponseRedirect('admin_code')
    if 'otch' in request.session:
        otch = request.session['otch']
    else:
        return HttpResponseRedirect('admin_code')
    prepod = T190Prepod.objects.using('exam').all()
    if request.method == 'POST':  # If the form has been submitted...
        if 'insert' in request.POST and request.POST['insert']:
            return HttpResponseRedirect('prepod_insert')
    if request.method == 'POST':  # If the form has been submitted...
        if 'edit_prepod' in request.POST and request.POST['edit_prepod']:
            p_num = request.POST['edit_prepod']
            request.session['p_num'] = p_num
            return HttpResponseRedirect('prepod_edit')
    if request.method == 'POST':  # If the form has been submitted...
        if 'del_prepod' in request.POST and request.POST['del_prepod']:
            p_num = request.POST['del_prepod']
            p = T190Prepod.objects.using('exam').filter(prepod_num=p_num).delete()
            return HttpResponseRedirect('admin')
    if request.method == 'POST':  # If the form has been submitted...
        if 'output' in request.POST and request.POST['output']:
            if 'fam' in request.session:
                del request.session['fam']
            if 'imya' in request.session:
                del request.session['imya']
            if 'otch' in request.session:
                del request.session['otch']
            if 'adm' in request.session:
                del request.session['adm']
            return HttpResponseRedirect('admin_code')
    if request.method == 'POST':  # If the form has been submitted...
        if 'fak' in request.POST and request.POST['fak']:
            return HttpResponseRedirect('admin_fak')
        if 'kaf' in request.POST and request.POST['kaf']:
            return HttpResponseRedirect('admin_kaf')
        if 'plantest' in request.POST and request.POST['plantest']:
            return HttpResponseRedirect('admin_plan')
        if 'password' in request.POST and request.POST['password']:
            return HttpResponseRedirect('admin_parol')
        if 'formula' in request.POST and request.POST['formula']:
            return HttpResponseRedirect('admin_formula')
    return render(request, 'admin.html', {'prepod': prepod, 'admin': admin, 'fam': fam, 'imya': imya, 'otch': otch})


def admin_parol(request):
    if 'fam' in request.session:
        fam = request.session['fam']
    else:
        return HttpResponseRedirect('admin_code')
    if 'imya' in request.session:
        imya = request.session['imya']
    else:
        return HttpResponseRedirect('admin_code')
    if 'otch' in request.session:
        otch = request.session['otch']
    else:
        return HttpResponseRedirect('admin_code')
    parol = T125Parol.objects.using('exam').all()
    if request.method == 'POST':  # If the form has been submitted...
        if 'output' in request.POST and request.POST['output']:
            return HttpResponseRedirect('admin')
    if request.method == 'POST':  # If the form has been submitted...
        if 'insert_parol' in request.POST and request.POST['insert_parol']:
            #            return HttpResponse("CheckPoint INSERT")
            return HttpResponseRedirect('parol_insert')
    if request.method == 'POST':  # If the form has been submitted...
        if 'edit_parol' in request.POST and request.POST['edit_parol']:
            parol_num = request.POST['edit_parol']
            request.session['parol_num'] = parol_num
            return HttpResponseRedirect('parol_edit')
    if request.method == 'POST':  # If the form has been submitted...
        if 'del_parol' in request.POST and request.POST['del_parol']:
            parol_num = request.POST['del_parol']
            p = T125Parol.objects.using('exam').filter(parol_num=parol_num).delete()
            return HttpResponseRedirect('admin_parol')
    return render(request, 'admin_parol.html', {'parol': parol, 'fam': fam, 'imya': imya, 'otch': otch})


def parol_insert(request):
    if request.method == 'POST':  # If the form has been submitted...
        if 'insert' in request.POST and request.POST['insert']:
            plan_num = request.POST.get('plan_num', 123)
            fam = request.POST.get('fam', 123)
            imya = request.POST.get('imya', 123)
            otch = request.POST.get('otch', 123)
            group_nam = request.POST.get('group_nam', 123)
            pred_nam = request.POST.get('pred_nam', 123)
            baza_num = request.POST.get('baza_num', 123)
            stud_num = request.POST.get('stud_num', 123)
            password = request.POST.get('parol', 123)
            trying = request.POST.get('trying', 123)
            paroll = T125Parol(plan_num=plan_num, fam=fam, imya=imya, otch=otch, group_nam=group_nam, pred_nam=pred_nam,
                               baza_num=baza_num, stud_num=stud_num, password=password, trying=trying)
            paroll.save()
            return HttpResponseRedirect('admin_parol')
    if request.method == 'POST':  # If the form has been submitted...
        if 'output' in request.POST and request.POST['output']:
            return HttpResponseRedirect('admin_parol')
    return render(request, 'parol_insert.html', {})


def parol_edit(request):
    parol_num = request.session['parol_num']
    paroll = T125Parol.objects.using('exam').filter(parol_num=parol_num)
    #    html = "<html><body>Now %s. </body></html>" % fakk[0].fak_namp
    #    return HttpResponse(html)
    if request.method == 'POST':  # If the form has been submitted...
        if 'edit_parol' in request.POST and request.POST['edit_parol']:
            plan_num = request.POST.get('plan_num', 123)
            fam = request.POST.get('fam', 123)
            imya = request.POST.get('imya', 123)
            otch = request.POST.get('otch', 123)
            group_nam = request.POST.get('group_nam', 123)
            pred_nam = request.POST.get('pred_nam', 123)
            baza_num = request.POST.get('baza_num', 123)
            stud_num = request.POST.get('stud_num', 123)
            password = request.POST.get('password', 123)
            trying = request.POST.get('trying', 123)
            p = T125Parol.objects.using('exam').filter(parol_num=parol_num).update(plan_num=plan_num, fam=fam, imya=imya, otch=otch,
                                                                     group_nam=group_nam, pred_nam=pred_nam,
                                                                     baza_num=baza_num, stud_num=stud_num,
                                                                     password=password, trying=trying)
            return HttpResponseRedirect('admin_parol')
    if request.method == 'POST':  # If the form has been submitted...
        if 'output' in request.POST and request.POST['output']:
            return HttpResponseRedirect('admin_parol')
    return render(request, 'parol_edit.html',
                  {'plan_num': paroll[0].plan_num, 'fam': paroll[0].fam, 'imya': paroll[0].imya, 'otch': paroll[0].otch,
                   'group_nam': paroll[0].group_nam, 'pred_nam': paroll[0].pred_nam, 'baza_num': paroll[0].baza_num,
                   'stud_num': paroll[0].stud_num, 'password': paroll[0].password, 'trying': paroll[0].trying})


def admin_plan(request):
    if 'fam' in request.session:
        fam = request.session['fam']
    else:
        return HttpResponseRedirect('admin_code')
    if 'imya' in request.session:
        imya = request.session['imya']
    else:
        return HttpResponseRedirect('admin_code')
    if 'otch' in request.session:
        otch = request.session['otch']
    else:
        return HttpResponseRedirect('admin_code')
    plan = T125Plan.objects.using('exam').all()
    if request.method == 'POST':  # If the form has been submitted...
        if 'output' in request.POST and request.POST['output']:
            return HttpResponseRedirect('admin')
    if request.method == 'POST':  # If the form has been submitted...
        if 'insert_plan' in request.POST and request.POST['insert_plan']:
            #            return HttpResponse("CheckPoint INSERT")
            return HttpResponseRedirect('plan_insert')
    if request.method == 'POST':  # If the form has been submitted...
        if 'edit_plan' in request.POST and request.POST['edit_plan']:
            plan_num = request.POST['edit_plan']
            request.session['plan_num'] = plan_num
            return HttpResponseRedirect('plan_edit')
    if request.method == 'POST':  # If the form has been submitted...
        if 'del_plan' in request.POST and request.POST['del_plan']:
            plan_num = request.POST['del_plan']
            #            html = "<html><body>Now %s. </body></html>" % plan_num
            #            return HttpResponse(html)
            p = T125Plan.objects.using('exam').filter(plan_num=plan_num).delete()
            return HttpResponseRedirect('admin_plan')
    return render(request, 'admin_plan.html', {'plan': plan, 'fam': fam, 'imya': imya, 'otch': otch})


def plan_insert(request):
    if request.method == 'POST':  # If the form has been submitted...
        if 'insert' in request.POST and request.POST['insert']:
            baza_num = request.POST.get('baza_num', 123)
            group_num = request.POST.get('group_num', 123)
            plann = T125Plan(baza_num=baza_num, group_num=group_num)
            plann.save()
            return HttpResponseRedirect('admin_plan')
    if request.method == 'POST':  # If the form has been submitted...
        if 'output' in request.POST and request.POST['output']:
            return HttpResponseRedirect('admin_plan')
    return render(request, 'plan_insert.html', {})


def plan_edit(request):
    plan_num = request.session['plan_num']
    planl = T125Plan.objects.using('exam').filter(plan_num=plan_num)
    #    html = "<html><body>Now %s. </body></html>" % fakk[0].fak_namp
    #    return HttpResponse(html)
    if request.method == 'POST':  # If the form has been submitted...
        if 'edit_plan' in request.POST and request.POST['edit_plan']:
            num = request.POST.get('num', 123)
            group_nam = request.POST.get('group_nam', 123)
            disc_nam = request.POST.get('disc_nam', 123)
            group_num = request.POST.get('group_num', 123)
            fak_num = request.POST.get('fak_num', 123)
            proc = request.POST.get('proc', 123)
            exec = request.POST.get('exec', 123)
            prepod = request.POST.get('prepod', 123)
            testolog = request.POST.get('testolog', 123)
            date = request.POST.get('date', 123)
            time = request.POST.get('time', 123)
            p = T125Plan.objects.using('exam').filter(plan_num=plan_num).update(baza_num=num, group_nam=group_nam, pred_nam=disc_nam,
                                                                  group_num=group_num, fak_num=fak_num, processed=proc,
                                                                  executed=exec, teacher_num=prepod,
                                                                  tester_num=testolog, test_date=date, test_time=time)
            return HttpResponseRedirect('admin_plan')
    if request.method == 'POST':  # If the form has been submitted...
        if 'output' in request.POST and request.POST['output']:
            return HttpResponseRedirect('admin_plan')
    return render(request, 'plan_edit.html',
                  {'num': planl[0].baza_num, 'group_nam': planl[0].group_nam, 'disc_nam': planl[0].pred_nam,
                   'group_num': planl[0].group_num, 'fak': planl[0].fak_num, 'proc': planl[0].processed,
                   'exec': planl[0].executed, 'prepod': planl[0].teacher_num, 'testolog': planl[0].tester_num,
                   'date': planl[0].test_date, 'time': planl[0].test_time})


def session(request):
    session = T125Session.objects.using('exam').all()
    #    html = "<html><body>Now %s. </body></html>" % session[0]
    #    return HttpResponse(html)
    return render(request, 'session.html',
                  {'session_num': session[0].session_num, 'parol': session[0].parol, 'plan_num': session[0].plan_num,
                   'repeating': session[0].repeating, 'processed': session[0].processed, 'trying': session[0].trying,
                   'attempt': session[0].attempt, 'datetime_v': session[0].datetime_v,
                   'ip_address': session[0].ip_address, 'session_code': session[0].session_code})


def admin_formula(request):
    if 'fam' in request.session:
        fam = request.session['fam']
    else:
        return HttpResponseRedirect('admin_code')
    if 'imya' in request.session:
        imya = request.session['imya']
    else:
        return HttpResponseRedirect('admin_code')
    if 'otch' in request.session:
        otch = request.session['otch']
    else:
        return HttpResponseRedirect('admin_code')
    formula = T120Formula.objects.using('exam').all()
    if request.method == 'POST':  # If the form has been submitted...
        if 'output' in request.POST and request.POST['output']:
            return HttpResponseRedirect('admin')
    if request.method == 'POST':  # If the form has been submitted...
        if 'insert_formula' in request.POST and request.POST['insert_formula']:
            #            return HttpResponse("CheckPoint INSERT")
            return HttpResponseRedirect('formula_insert')
    if request.method == 'POST':  # If the form has been submitted...
        if 'edit_formula' in request.POST and request.POST['edit_formula']:
            formula_num = request.POST['edit_formula']
            request.session['formula_num'] = formula_num
            return HttpResponseRedirect('formula_edit')
    if request.method == 'POST':  # If the form has been submitted...
        if 'del_formula' in request.POST and request.POST['del_formula']:
            formula_num = request.POST['del_formula']
            p = T120Formula.objects.using('exam').filter(formula_num=formula_num).delete()
            return HttpResponseRedirect('admin_formula')
    return render(request, 'admin_formula.html', {'formula': formula, 'fam': fam, 'imya': imya, 'otch': otch})


def formula_insert(request):
    if request.method == 'POST':  # If the form has been submitted...
        if 'insert' in request.POST and request.POST['insert']:
            baza_num = request.POST.get('baza_num', 123)
            quest_type = request.POST.get('quest_type', 123)
            quest_col = request.POST.get('quest_col', 123)
            quest_time = request.POST.get('quest_time', 123)
            formulal = T120Formula(baza_num=baza_num, quest_type=quest_type, quest_col=quest_col, quest_time=quest_time)
            formulal.save()
            return HttpResponseRedirect('admin_formula')
    if request.method == 'POST':  # If the form has been submitted...
        if 'output' in request.POST and request.POST['output']:
            return HttpResponseRedirect('admin_formula')
    return render(request, 'formula_insert.html', {})


def formula_edit(request):
    formula_num = request.session['formula_num']
    formulal = T120Formula.objects.using('exam').filter(formula_num=formula_num)
    #    html = "<html><body>Now %s. </body></html>" % fakk[0].fak_namp
    #    return HttpResponse(html)
    if request.method == 'POST':  # If the form has been submitted...
        if 'edit_formula' in request.POST and request.POST['edit_formula']:
            baza_num = request.POST.get('baza_num', 123)
            quest_type = request.POST.get('quest_type', 123)
            quest_col = request.POST.get('quest_col', 123)
            quest_time = request.POST.get('quest_time', 123)
            p = T120Formula.objects.using('exam').filter(formula_num=formula_num).update(baza_num=baza_num, quest_type=quest_type,
                                                                           quest_col=quest_col, quest_time=quest_time)
            return HttpResponseRedirect('admin_formula')
    if request.method == 'POST':  # If the form has been submitted...
        if 'output' in request.POST and request.POST['output']:
            return HttpResponseRedirect('admin_formula')
    return render(request, 'formula_edit.html', {'baza_num': formulal[0].baza_num, 'quest_type': formulal[0].quest_type,
                                                 'quest_col': formulal[0].quest_col,
                                                 'quest_time': formulal[0].quest_time})
