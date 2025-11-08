from django.shortcuts import render,redirect,HttpResponse
from.models import *
# Create your views here.

def employe_view(requset):
    employe_data = EmployeeTable.objects.all()
    if requset.method == 'POST':
        name = requset.POST.get('name')
        age = requset.POST.get('age')
        email = requset.POST.get('mail')
        doj = requset.POST.get('dofj')
        EmployeeTable.objects.create( Employee_Name=name, Age=age,Email_Address=email,Date_of_Joining=doj)
        return redirect('vemp')
    return render(requset,'EmployeeTable.html')    

def view_emp(requset):
    employe_data = EmployeeTable.objects.all()
    return render(requset,'EmployeeView.html',{'emp_data':employe_data})

#-------------------------------------------------------------------------

def store_view(requset):
    store_data = Product_Table.objects.all()
    if requset.method == 'POST':
        p_name = requset.POST.get('pro_name')
        b_name= requset.POST.get('brand')
        price = requset.POST.get('price')
        man_fac= requset.POST.get('md')
        Product_Table.objects.create( Product_Name=p_name, Brand_Name=b_name, price=price, Manufacturing_Date=man_fac)
    return render(requset,'product_tab.html',{'pro_vew':store_data})

#------------------------------------------------------------------------------------------------

def book_view(requset):
    book_data =  Book_Table.objects.all()
    if requset.method == 'POST':
         bt = requset.POST.get('bok_tit')
         an= requset.POST.get('auth_name')
         gen= requset.POST.get('grnre')
         pub_y= requset.POST.get('pub_year')
         Book_Table.objects.create(  Book_Title= bt,  Author_Name=an,  Genre= gen,   Published_Year= pub_y)
    return render(requset,'book.html',{'book_vew':book_data})
    
#__________________________________________________________________
def movie_view(requset):
    movie_data = Movie_Table.objects.all()
    if requset.method == 'POST':
         mt = requset.POST.get('mov_name')
         dn= requset.POST.get('drac_name')
         date= requset.POST.get('dat')
         lang= requset.POST.get('langu')
         Movie_Table.objects.create(   Movie_Title= mt,Director_Name=dn, Date=date,Language=lang)
    return render(requset,'movie.html',{'mov_viw':movie_data})

def movie_delete(requset,mov_id):
    mt =  Movie_Table.objects.get(id=mov_id)
    print(mt)
    mt.delete()
    return redirect("movie")  

def movie_edit(request, mov_id):
    movie = Movie_Table.objects.get(id=mov_id)  # fixed here
    if request.method == 'POST':
        movie.Movie_Title = request.POST.get('mov_name')
        movie.Director_Name = request.POST.get('drac_name')
        movie.Date = request.POST.get('dat')
        movie.Language = request.POST.get('langu')
        movie.save()
        return redirect('movie')  
    return render(request,'movie.html',{'movie': movie})
 

#_____________________________________________________________________________

def student_view(requset):
    student_data =Student_Table.objects.all()
    if requset.method == 'POST':
         sn=requset.POST.get('stu_name')
         age= requset.POST.get('age_stu')
         ed=requset.POST.get('emial')
         dob=requset.POST.get('dob_stu')
         Student_Table.objects.create(Student_Name=sn,Age=age,Email_Address=ed,Date_of_Birth=dob)
    return render(requset,'student.html',{'stu_viw':student_data}) 


    
      
        

