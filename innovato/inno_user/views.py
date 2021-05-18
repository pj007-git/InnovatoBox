from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Video_up,Comment,like,profile,Skill,Portfo,follower
import operator
# Create your views here.
def index(request):
    # registration page
    # signup logic
    u =  User.objects.all()
    user_list = []
    for k in u:
        user_list.append(k.username)
    if request.method == "POST":    
        uname = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass']
        pass2 = request.POST['rpass']
        mail1 = request.POST['email']
        #### profile details
        pcontact = request.POST['contact']
        pabout = request.POST['about']
        

        html = request.POST['HTML']
        css = request.POST['CSS']
        js = request.POST['JS']
        py = request.POST['Python']
        db = request.POST['db']
        wordp = request.POST['Wordpress']
        mongo = request.POST['Mongo']

        
        if pass1 != pass2:
            messages.error(request, "PASSWORD DOES NOT MATCH ")
            return redirect('/inno_user/')

        #Username Logic
        z = ['_','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
                'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        def check(x2):
            y = ['#',"$","%",'!','@']
            for i in y:
                if i in x2:
                    return i
            else:
                return False
        if uname in user_list:
            messages.warning(request,"username is already exist")
            return redirect('/inno_user/')
        if len(uname)<=3:
            messages.warning(request,"your username must have 4 or more character ")
            return redirect('/inno_user/')
        if uname[0] not in z:
            messages.warning(request,"first char must be lowercase or '_' ") 
            return redirect('/inno_user/')
        for a in uname:
            if a.isspace() == True:
                messages.warning(request," your username is having space")
                return redirect('/inno_user/')
        else:
            result = check(uname)
            if type(result) == str:
                if result in uname:
                    #print("yes")
                    x1 = uname.replace(result, '')
                    if x1.isalpha():
                        messages.warning(request,"required 0-9 in Username")
                        return redirect('/inno_user/')
                    elif x1.isdigit():
                        messages.warning(request,"required a-z in username")
                        return redirect('/inno_user/')
                    elif x1.isalnum():
                        pass
                    else:
                        messages.warning(request,"required also 0-9 and a-z with one speciel character")
                        return redirect('/inno_user/')
            else:
                messages.warning(request,"No speciel charcter found")
                return redirect('/inno_user/')


        user = User.objects.create_user(uname,mail1,pass1)
        user.first_name = fname
        user.last_name = lname
        user.save()
        prof = profile(p_name=uname,p_contact=pcontact,p_about=pabout)
        prof.save()
        sk = Skill(sk_user=uname,Html=html,Css=css,Js=js,Python=py,Database=db,Wordpress=wordp,Mongodb=mongo)
        sk.save()
        # port = Portfo(port_user=uname, port_url=port_url)
        # port.save()
        messages.success(request,"user is registerd successfully")
        return redirect("/inno_user/login/")
    
        messages.warning(request,"username is already exist")
        return redirect("/inno_user/")
    else:
        return render(request, "inno_user/index.html") 

def signin(request):
    #login page logic
    u =  User.objects.all()
    user_list = []
    for i in u:
        user_list.append(i.username)
    
    if request.method == 'POST':
        uname = request.POST.get('uname','')
        password = request.POST.get("password",'')
        
        luser = authenticate(username=uname, password=password)
        if luser is not None:
            login(request,luser)
            messages.success(request, f" {uname} is successfully loged in")
            return redirect('/inno_user/welcomepage/')
        else:
            if uname not in user_list:     
                messages.warning(request,"invalid username")
                return redirect('/inno_user/login/')
            else:
                messages.warning(request,"invalid password")
                return redirect('/inno_user/login/')

    else:
        return render(request,"inno_user/login.html")


def dashbord(request, vid):
    v = Video_up.objects.filter(v_id=vid)
    c1 = Comment.objects.all()
    l = like.objects.all()
    lis1 = []
    lis2 = []
    for x in l:
        if v[0] == x.l_postid:
            lis1.append(x)
        if x.l_user == request.user:
            lis2.append(x.l_postid)
    return render(request,"inno_user/dashbord.html", { 
        'video' : v[0], 
        'cmt' : c1, 
        'like' : l,
        'l_like' : len(lis1),
        'like_user' : lis2, 
        })

def signout(request):
    logout(request)
    messages.success(request,"you are loged out")
    return redirect('/inno_user/')

def up_video(request):
    pr = profile.objects.all()
    if request.method == "POST":
        v_title = request.POST.get('title', '')
        v_video = request.FILES['video']
        v_desc = request.POST.get('desc', '')
        v_image = request.FILES['image']
        v_gif = request.FILES['gif']
    

        v_post = Video_up(v_title=v_title, v_file=v_video, v_desc=v_desc,v_user=request.user,v_image=v_image,v_gif = v_gif)
        v_post.save()
        messages.success(request, "'s Post uploaded successfully...")
        return redirect('/inno_user/up_video/')
    else:
        return render(request, "inno_user/up_video.html",{'p' : pr })

def cmt_upld(request, vid):
    post1 = Video_up.objects.filter(v_id=vid)
    if request.method == "POST":
        
        cmt = request.POST.get('comment', '')

        com = Comment(cmt_user=request.user, cmt_vid=post1[0], cmt_msg=cmt)
        if cmt.isspace():
            messages.warning(request,"please no null comment")
            return redirect(f'/inno_user/dashbord/{vid}/')
        com.save()
        return redirect(f'/inno_user/dashbord/{vid}/')





def like_l(request, vid):
    post2 = Video_up.objects.filter(v_id=vid)
    li = like(l_user=request.user, l_postid=post2[0])        
    li.save()
    return redirect(f'/inno_user/dashbord/{vid}')
    

# llid = ''
def unlike(request, lid, vid):
    ll = like.objects.filter(l_id=lid)
    ll.delete()
    return redirect(f"/inno_user/dashbord/{vid}/")

def delete_post(request,idd):
    v = Video_up.objects.filter(v_id=idd)
    v.delete()
    messages.error(request,"your post is deleted successfully")
    return redirect("/inno_user/homepage/")


def homepage(request):
    v = Video_up.objects.all()
    l = like.objects.all()
    pr = profile.objects.all()
    
    # total likes logic
    dic1 = dict()
    for i in l:
        dic1[i.l_postid] = dic1.get(i.l_postid, 0) + 1

    lr = v[::-1]
    
    return render(request,"inno_user/homepage.html", { 'video' : lr,'dic1' : dic1, 'p' : pr, })
    
def searchpage(request):
    pr = profile.objects.all()
    v = Video_up.objects.all()
    list1 = []
    if request.method == "POST":
        Search_msg = request.POST.get('smsg','')
        for i in v:
            if i.v_title.lower().strip().replace(" ","") == Search_msg.lower().strip().replace(" ",""):
                list1.append(i)
        print(v)            
        if len(list1) == 0:
            yes= "yes"
        else:
            yes ="No"
        return render(request,"inno_user/searchpage.html",{'li' : list1,
        'msg' : "NO SEARCH FOUND!!your String must be the title of the post", 'y' : yes,'p' : pr  })

    else:
        return HttpResponse("<h2>No bro soorry!!</h2>")
    # return render(request,"inno_user/searchpage.html",{'li' : list1 })


def profilepage(request, pid,):
    l = []
    pr = profile.objects.filter(p_id=pid)
    s = Skill.objects.filter(sk_user=pr[0].p_name)
    port = Portfo.objects.all()
    f = follower.objects.filter(f_user=pr[0].p_name)
    for j in f:
        l.append(j.sub_user.username)
    fo = len(f)
    
     
    # port = Portfo.objects.filter(port_user=pr[0].p_name)
    # print(S[0])
    return render(request,"inno_user/profilepage.html", {'p':pr[0], 's' : s[0],'port' : port,'f' : fo,'fo':l })

def up_profile(request, pid):
    pr = profile.objects.all()
    pro = profile.objects.filter(p_id=pid)
    if request.method == "POST":
        p = profile(p_id = pid)
        p.p_name = request.POST.get('pname', '')
        p.p_contact = request.POST.get('pnumber', '')
        p.p_about = request.POST.get('pabout', '')
        p.p_image = request.FILES['pimage']
        p.p_email = request.POST.get('pemail','')
        print(p.p_contact)
        if p.p_contact == "0":
            messages.warning(request,"no means no")
            return render(request,"inno_user/up_profile.html",{ 'pro': pro[0] })
        p.save()
        messages.success(request, "'s Profile updated successfully...")
        pro = profile.objects.filter(p_id=pid)
        return render(request,'inno_user/up_profile.html',{ 'pro': pro[0] })
        
    else:
        pro = profile.objects.filter(p_id=pid)
        return render(request, "inno_user/up_profile.html",{ 'pro': pro[0] })

def up_skill(request,pid,sid):
    print(sid,pid)
    pr = profile.objects.filter(p_id=pid) 
    sk = Skill(sk_id=sid)
    if request.method == "POST":  
        sk.sk_user = request.POST.get('sname','')   
        sk.Html = request.POST.get('HTML','')
        sk.Css = request.POST.get('CSS','')
        sk.Js =request.POST.get('JS', '')
        sk.Python = request.POST.get('Python', '')
        sk.Database = request.POST.get('db', '')
        sk.Wordpress = request.POST.get('Wordpress', '')
        sk.Mongodb = request.POST.get('Mongo', '')

        sk.save()
        messages.success(request,"your skill are added successfully!!")
        s = Skill.objects.filter(sk_id=sid)
        return render(request,"inno_user/up_skills.html",{'s' : s[0], 'p' : pr[0]})

    else:
        s = Skill.objects.filter(sk_id=sid)
        return render(request,"inno_user/up_skills.html",{'s' : s[0], 'p' : pr[0]})

def portfo(request,pid):
    # po = Portfo.objects.all()
    p = profile.objects.filter(p_id = pid)
    if request.method == "POST":
        port_user = request.POST.get('name','')
        port_img = request.FILES['project_image']
        port_url = request.POST.get('project')
        port = Portfo(port_user=port_user,port_url=port_url,port_img=port_img)
        port.save()
        messages.success(request,"your project is saved !!")
        
        return render(request,"inno_user/portfo.html", {'p' : p[0], })
    else:
        
        return render(request,"inno_user/portfo.html", {'p' : p[0], })
def del_project(request):
    port = Portfo.objects.all()
    p = profile.objects.all()
    return render(request,"inno_user/deleteproject.html",{'port' : port,'p':p})

def del_this_project(request,delid):
    port = Portfo.objects.filter(port_id=delid)
    port.delete()
    return redirect("/inno_user/delete_project/")

def likedvideo(request):
    pr = profile.objects.all()
    l = like.objects.all()
    v = Video_up.objects.all()
    try:
        for i in v:
            print(i.v_id)
            print(type(i.v_id))
        print(type(l[0].l_postid)   )
        return render(request,"inno_user/likedvideo.html",{'l' : l,'video' : v,'p' : pr })
    except:
        return render(request,"inno_user/likedvideo.html",{'msg' : "You haven't liked any video yet!",'l' : l,'video' : v,'p' : pr  })

def Trend(request):
    pr = profile.objects.all()
    l = like.objects.all()
    v = Video_up.objects.all()
    dic1 = dict()
    for i in l:
        dic1[i.l_postid.v_id] = dic1.get(i.l_postid.v_id, 0) + 1
    
    sorted_dict = sorted(dic1.items(),key=operator.itemgetter(1),reverse=True)
    print(sorted_dict)
    sorted_dic = dict(sorted_dict)
    x = sorted_dic.keys()
    print(x)
    
    for j in v:
        print(j.v_id)
    return render(request,"inno_user/trendingpage.html",{'l' : l,'v' : v ,'di' : sorted_dic,'p' : pr })

def welcome(request):
    
    return render(request,"inno_user/welcomepage.html")
def guest(request):
    if request.method == "POST":
        usname = request.POST['usname']
        #mail = request.POST['emaill']
        passs = request.POST['passs']
        guest_user = authenticate(username=usname, password=passs)
        login(request,guest_user)
        messages.success(request, f" {usname} is successfully loged in")
        return render(request,"inno_user/welcomepage.html")
    else:
        return render(request,"inno_user/welcomepage.html")

def follow(request):
    f = follower.objects.all()
    p = profile.objects.all()
    try:
        return render(request,"inno_user/subscription.html",{'f': f,'p' : p})
    except:
        return render(request,"inno_user/subscription.html",{'f': f,'msg' : "You Are not Following Any of the Members Yet!!"})

def following(request,pid):
    p = profile.objects.filter(p_id = pid)
    # u = User.objects.filter(username = uid)
    # print(type(pid))
    # print(type(uid))
    # print(p[0])
    fo = follower(f_user=p[0].p_name, sub_user=request.user)
    fo.save()
    messages.success(request,f"you are Now Following {p[0].p_name}")
    return redirect(f"/inno_user/profilepage/{pid}")

def unfollowing(request,pid):
    p = profile.objects.filter(p_id = pid)
    unfo = follower.objects.filter(f_user = p[0].p_name)
    for i in unfo:
        if i.sub_user == request.user:
            un = follower.objects.filter(f_id = i.f_id)
            un.delete()
    messages.success(request,f"you are Unfollowing {p[0].p_name}")
    return redirect(f"/inno_user/profilepage/{pid}")