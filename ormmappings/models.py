from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField('stud_name',max_length=100)
    age = models.IntegerField('stud_age')
    subjs = models.ManyToManyField('Subject',related_name='students')
    dept = models.ForeignKey('Dept',on_delete=models.CASCADE,related_name='students')


class Subject(models.Model):
    name = models.CharField('subj_name',max_length=100) #text
    code = models.CharField('subj_code', max_length=100)
    remarks = models.TextField('subj_overview',max_length=100) #TextArea -- row/coln


class Dept(models.Model):
    name = models.CharField('dept_name',max_length=100)
    code = models.CharField('dept_code', max_length=100)
    college = models.ForeignKey('College',on_delete=models.CASCADE,related_name='dept')


class College(models.Model):
    name = models.CharField('college_name',max_length=100)
    code = models.CharField('college_code', max_length=100)
    address = models.OneToOneField('Address',on_delete=models.CASCADE,related_name='college')

class Address(models.Model):
    city = models.CharField('city',max_length=100)
    state = models.CharField('state', max_length=100)
    pincode = models.IntegerField('pincode')

#Address(id=101,city='Pune',state='MH',pincode=171233)
'''
    FRK KEY
    
   AT THE TIME WRITTING 
    RELSHIP     -- BACKREF
    
    
    CL
        ADR = RLTN (BACKREF=CL) 
    ADD
        CLID = COLUMN(fk)
        
FK CLID -- INFERRED FROM PK - INTEGER --NOT PRESENT
BCKREF - CL -- INSTANCE TYPE


ADR -- INSTANCE TYPE -- LIST OF INSTNACE TYPE [USELIST-tRUE]
    
'''