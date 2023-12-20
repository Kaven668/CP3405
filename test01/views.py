from django.shortcuts import render, redirect, HttpResponse
from test01 import models

db_id = 2
question_type = "short answer"
question_category = "category"
option_correct = True
question_title = "How's the weather?"


# Create your views here.
def test_fun(request):
    name = "zm"
    student = ["pw", "ch", "ak", "ll", "ls"]
    return render(request, "learn.html", {"a": name, "b": student})


def info_list(request):
    # 获取数据库所有数据
    date_list = models.UserInfo.objects.all()
    return render(request, "info_list.html", {"data_list": date_list})


def login(request):
    if request.method == "GET":
        return render(request, 'info_add.html')
    user = request.POST.get("user")  # 获取数据
    password = request.POST.get("pwd")
    age = request.POST.get("age")
    models.UserInfo.objects.create(name=user, password=password, age=age)

    return redirect("/info")


def login_01(request):
    if request.method == "GET":
        return render(request, "login.html")
    input_name = request.POST.get("username")
    input_password = request.POST.get("password")
    user_info = models.UserInfo.objects.all()
    for i in user_info:
        print(i.name, i.password)
        if i.name == input_name and i.password == input_password:
            return redirect("/products.html")
    return redirect("/failed.html")


def delete(request):
    uid = request.GET.get("id")
    models.UserInfo.objects.filter(id=uid).delete()  # 删除数据
    return redirect("/info/")


def test_db(request):
    # Input the data
    models.Survey.objects.create(survey_id=db_id)
    models.QuestionType.objects.create(question_type_id=db_id, question_type=question_type)
    models.QuestionCategory.objects.create(question_category_id=db_id, question_category=question_category)
    models.MediaType.objects.create(media_type_id=db_id)
    models.Question.objects.create(question_id=db_id, question_title=question_title, question_type_id=db_id)
    models.Option.objects.create(option_id=db_id, option_correct=option_correct)
    models.QuestionHasSurvey.objects.create(question_id=db_id, survey_id=db_id)
    models.QuestionHasQuestionCategory.objects.create(question_id=db_id, question_category_id=db_id)
    return HttpResponse("Added Successfully")
    # return redirect()


def test_db_01(request):
    # Query the data
    obj = models.QuestionHasQuestionCategory.objects.filter(question_id=2)
    for i in obj:
        print(i.question_category_id, i.question_id)
    question = models.Question.objects.filter(question_id=db_id)
    for i in question:
        print(i.question_title)
    return HttpResponse("Done")


def test_db_02(request):
    # Get data from POST query
    if request.method == "GET":
        return render(request, 'info_add.html')
    user = request.POST.get("user")
    password = request.POST.get("pwd")
    age = request.POST.get("age")
    print(user, password, age)
    return HttpResponse("Welcome " + user)


def test_db_03(request):
    # Get data from GET query
    test_01 = request.GET.get("id")
    test_02 = request.GET.get("name")
    test_03 = request.GET.get("type")
    print(test_01, test_02, test_03)
    return HttpResponse("500")


def test_dlt(request):
    # Clear all the data
    models.Survey.objects.all().delete()
    models.QuestionType.objects.all().delete()
    models.QuestionCategory.objects.all().delete()
    models.MediaType.objects.all().delete()
    models.Question.objects.all().delete()
    models.Option.objects.all().delete()
    models.QuestionHasSurvey.objects.all().delete()
    models.QuestionHasQuestionCategory.objects.all().delete()
    return HttpResponse("Deleted Successfully")
