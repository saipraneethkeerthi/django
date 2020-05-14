from django.shortcuts import render
from django.http import HttpResponse
from .models import projects
from .models import education

# Create your views here.

def index(request):

    p1=projects()
    p1.name='Smart Automatic Petrol Pump using RFID'
    p1.dec='The main aim of the project is to design a system which is capable of automatically deducting the amount of petrol dispensed from user card based on RFID technology.'
    p1.date='2019'
    p1.image='5.png'

    p2=projects()
    p2.name='Smart Vehicle Monitoring System'
    p2.dec='The aim of the project is to implement smart vehicle monitoring system using GSM. If any crash occur, then SMS will be sent to the owner or to saved contacts. Most of the road accidents are happened due to alcohol drinking and because of not obeying the traffic rules. If toxic gas present in any AC cars,then toxic gas sensor will sense the gas and the indication is displayed by using light then the window door will be automatically opened'
    p2.date='2019'
    p2.image='1.jpeg'

    p3=projects()
    p3.name='Automatic Railway Gate System'
    p3.dec='Automatic Railway Gate Control System is useful project, which helps in automatically opening and closing the railway gate upon detecting arrival or departure of the train.'
    p3.date='2018'
    p3.image='4.jpg'

    p4=projects()
    p4.name='Automatic Street Lights Using IR Sensor'
    p4.dec='The main aim of the project is to save electricity.During the day time many street lights are been glowing, so reduce that we have used LDR. In night time if there is no person roaming on the road,then there will be unnessary of glowing of light, to reduce that we have used IR Sensor'
    p4.date='2017'
    p4.image='6.png'

  #  p5=projects()
  #  p5.name='xyz'
  #  p5.dec='asdfghjklwertyuiop[zxcvbnm,'
   # p5.date='2022'
  #  p5.image='2.jpg'



    proj=[p1,p2,p3,p4]



    e1=education()
    e1.year='2015'
    e1.study='CLASS X'
    e1.college='Ekashila Public School, Jangaon'
    e1.branchIs=False
    e1.branch='love'
    e1.cgpa='8.8'

    e2=education()
    e2.year='2015-2018'
    e2.study='Diploma'
    e2.college='Government Polytechnic college, Warangal'
    e2.branchIs=True
    e2.branch='Electronics And Communication Engineering'
    e2.cgpa='8.5'

    e3=education()
    e3.year='2018-2021'
    e3.study='Bachelor of Technology'
    e3.college='Vallurupalli Nageswara Rao Vignana Jyothi Institute of Engineering and Technology (VNRVJIET)'
    e3.branchIs=True
    e3.branch='Electronics And Communication Engineering'
    e3.cgpa='8.3'

  #  e4=education()
 #   e4.year='2000'
  #  e4.study='life lesson'
  #  e4.college='home'
  #  e4.branch='love'
  #  e4.cgpa='100'

    

    edu=[e3,e2,e1]


    return render(request,'index.html',{'proj':proj,'edu':edu})
