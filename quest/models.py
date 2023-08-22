from django.db import models


class T102Fak(models.Model):
    fak_num = models.IntegerField(primary_key=True)
    fak_namp = models.CharField(max_length=255, blank=True)
    fak_nams = models.CharField(max_length=60, blank=True)
    mesto = models.IntegerField(null=True, blank=True)
    def __unicode__(self):
        return u'%s' % self.fak_namp
    class Meta:
        db_table = u't102_fak'
        verbose_name = u'факультет'
        verbose_name_plural = u'факультеты'

class T121Quest(models.Model):
    quest_num = models.AutoField(primary_key=True)
    QuestID = models.IntegerField(null=True, blank=True)	
    baza_num = models.IntegerField(null=True, blank=True)
    disc_num = models.IntegerField(null=True, blank=True)	
    quest_text = models.TextField(blank=True)
    quest_text_etalon = models.TextField(blank=True)	
    quest_lev = models.IntegerField(null=True, blank=True)
    quest_type = models.IntegerField(null=True, blank=True)
    answer_kol = models.IntegerField(null=True, blank=True)
    answer = models.TextField(blank=True)
    def __unicode__(self):
        return u'%s' % (self.quest_text)
    class Meta:
        db_table = u't121_quest'
        verbose_name = u'вопрос'
        verbose_name_plural = u'вопросы'		
		

class T122Answer(models.Model):
    answer_num = models.IntegerField(primary_key=True)
    quest_num = models.IntegerField(null=True, blank=True)
    answer_type = models.IntegerField(null=True, blank=True)	
    ok = models.IntegerField(null=True, blank=True)
    ans = models.IntegerField(null=True, blank=True)
    answer_text = models.TextField(blank=True)
    AnswerID = models.IntegerField(null=True, blank=True)		
    def __unicode__(self):
        return u'%s' % self.answer_text
    class Meta:
        db_table = u't122_answer'
        verbose_name = u'ответ'
        verbose_name_plural = u'ответы'

class T125Parol(models.Model):
    parol_num = models.AutoField(primary_key=True)
    plan_num = models.IntegerField(blank=False)
    fam = models.CharField(max_length=40, blank=True)
    imya = models.CharField(max_length=30, blank=True)
    otch = models.CharField(max_length=30, blank=True)	
    group_nam = models.CharField(max_length=20, blank=True)	
    pred_nam = models.CharField(max_length=30, blank=True)		
    baza_num = models.IntegerField(blank=False)		
    stud_num = models.IntegerField(blank=False)
    password = models.CharField(max_length=36, blank=False)
    trying = models.IntegerField(blank=False)			
    def __unicode__(self):
#        return u'%d %s %s %s %s' % (self.plan_num, self.stud_num, self.password, self.pred_nam )
        return u'%s %s %s %s %s' % (self.fam, self.imya, self.otch, self.group_nam, self.persona )
    class Meta:
        db_table = u't125_parol'
        verbose_name = u'пароль'
        verbose_name_plural = u'пароли'

class T125Plan(models.Model):
    plan_num = models.IntegerField(primary_key=True)
    baza_num = models.IntegerField(null=True, blank=True)
    group_nam = models.CharField(max_length=20, blank=False) 
    pred_nam = models.CharField(max_length=50, blank=False) 	
    group_num = models.IntegerField(null=True, blank=True) 
    fak_num = models.IntegerField(null=True, blank=True)
    processed = models.IntegerField(null=True, blank=True)
    executed = models.IntegerField(null=True, blank=True)
    teacher_num = models.IntegerField(null=True, blank=True) 
    tester_num = models.IntegerField(null=True, blank=True)	
    test_date = models.DateField(null=True, blank=True)
    test_time = models.TimeField(null=True, blank=True)
    def __unicode__(self):
        return u'%d %s %s %s %s %d %d' % (self.plan_num, self.group_nam, self.pred_nam, self.test_date, self.test_time)
    class Meta:
        db_table = u't125_plan'
        verbose_name = u'план тестирования'
        verbose_name_plural = u'планы тестования'

class T125Session(models.Model):
    session_num = models.AutoField(primary_key=True)
    parol = models.CharField(max_length=12, blank=True)		
    plan_num = models.IntegerField(null=True, blank=True)
    repeating = models.IntegerField(null=True, blank=True)
    processed = models.IntegerField(null=True, blank=True)
    trying = models.IntegerField(null=True, blank=True)
    attempt = models.IntegerField(null=True, blank=True)
    datetime_v = models.DateTimeField(null=True, blank=True)	
    ip_address = models.CharField(max_length=15, blank=True)		
    session_code = models.CharField(max_length=36, blank=True)	
    def __unicode__(self):
        return u'%d %s %d% d% d% d% d %s %s %s ' % (self.session_num, self.parol, self.plan_num,self.repeating, self.processed, self.trying, self.attempt, self.datetime_v, self.ip_address, self.session_code )
    class Meta:
        db_table = u't125_session'
        verbose_name = u'сеанс'
        verbose_name_plural = u'сеансы'
		
class T125Testing(models.Model):
    testing_num = models.AutoField(primary_key=True)
    parol = models.CharField(max_length=12, blank=True)		
    plan_num = models.IntegerField(null=True, blank=True)
    repeating = models.IntegerField(null=True, blank=True)
    processed = models.IntegerField(null=True, blank=True)
    trying = models.IntegerField(null=True, blank=True)
    attempt = models.IntegerField(null=True, blank=True)
    datetime_v = models.DateTimeField(null=True, blank=True)	
    ip_address = models.CharField(max_length=15, blank=True)		
    session_code = models.CharField(max_length=36, blank=True)	
    def __unicode__(self):
        return u'%d %s %d% d% d% d% d %s %s %s ' % (self.testing_num, self.parol, self.plan_num,self.repeating, self.processed, self.trying, self.attempt, self.datetime_v, self.ip_address, self.session_code )
    class Meta:
        db_table = u't125_testing'
        verbose_name = u'тестирование'
        verbose_name_plural = u'тестирования'			

class T126Test(models.Model):
    test_num = models.AutoField(primary_key=True)
    plan_num = models.IntegerField(null=True, blank=True)
    stud_num = models.IntegerField(null=True, blank=True)	
    baza_num = models.IntegerField(null=True, blank=True)
    mark = models.FloatField(null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    ipaddr = models.CharField(max_length=45, blank=True)
    def __unicode__(self):
        return u'%s %g %s %s' % (self.stud_num, self.mark, self.time, self.ipaddr)
    class Meta:
        db_table = u't126_test'
        verbose_name = u'тест'
        verbose_name_plural = u'тесты'

class T127ResTest(models.Model):
    res_test_num = models.AutoField(primary_key=True)
    test_num = models.IntegerField(null=True, blank=True)
    quest_num = models.IntegerField(null=True, blank=True)
    answer = models.CharField(max_length=500, blank=True)
    quest_typ = models.IntegerField(null=True, blank=True)
    ball = models.FloatField(null=True, blank=True)
    def __unicode__(self):
        return u'%d %s %g' % (self.test_num, self.answer, self.ball )
    class Meta:
        db_table = u't127_res_test'
        verbose_name = u'результаты тестирования'
        verbose_name_plural = u'результаты тестирования'

class T190Admin(models.Model):
    admin_num = models.AutoField(primary_key=True)
    fam = models.CharField(max_length=40, blank=False)	
    imya = models.CharField(max_length=30, blank=False)	
    otch = models.CharField(max_length=30, blank=False)		
    pass_md5 = models.CharField(max_length=40, blank=False)	
    priv_num = models.IntegerField(null=True, blank=True)	
    priv_nam = models.CharField(max_length=10, blank=False)		
    def __unicode__(self):
        return u'%d %s %s %s %s %d %s' % (self.admin_num, self.fam, self.imya, self.otch, self.pass_md5, self.priv_num, self.priv_nam)		
    class Meta:
        db_table = u't190_admin'
        verbose_name = u'администратор'
        verbose_name_plural = u'администраторы'		
	
class T190Prepod(models.Model):
    prepod_num = models.AutoField(primary_key=True)
    fam = models.CharField(max_length=40, blank=False)	
    imya = models.CharField(max_length=30, blank=False)	
    otch = models.CharField(max_length=30, blank=False)		
    pass_md5 = models.CharField(max_length=40, blank=False)	
    priv_num = models.IntegerField(null=True, blank=True)	
    priv_nam = models.CharField(max_length=10, blank=False)		
    def __unicode__(self):
        return u'%d %s %s %s %s %d %s' % (self.prepod_num, self.fam, self.imya, self.otch, self.pass_md5, self.priv_num, self.priv_nam)		
    class Meta:
        db_table = u't190_prepod'
        verbose_name = u'преподаватель'
        verbose_name_plural = u'преподаватели'				