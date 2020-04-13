from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from deeplearn.cnn import deeper_model
from account.models import UserInfo
from deeplearn.models import speciesRecognition


@login_required(login_url='/account/login/')
def pic_upload(request):
    """上传图片"""
    user = User.objects.get(username=request.user.username)
    userinfo = UserInfo.objects.get(user=user)
    if request.method == 'POST':
        new_img = speciesRecognition(data_photo=request.FILES.get('img'))
        new_img.save()

        new_img = new_img.data_photo
        # print("图片地址:",new_img)

        cnn_model = deeper_model() #实例化
        result = cnn_model.startRecognize(new_img)  #调用模型，输出识别结果

        return render(request, 'deeplearn/pic_upload.html', {"userinfo_all": userinfo,
                                        "result":result,'new_img':new_img})
    if request.method == 'GET':
        return render(request, 'deeplearn/pic_upload.html', {"userinfo_all": userinfo})

    return render(request, 'deeplearn/pic_upload.html',{"userinfo_all": userinfo})

