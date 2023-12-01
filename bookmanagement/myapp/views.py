from myapp.imports import *

def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'data': token})

@csrf_exempt 
def user_register(request):
    if request.method == "POST":
        try:
            request_data = request.body.decode('utf-8')
            data = json.loads(request_data)

            user_email = data.get('user_email',None)
            user_password = data.get('user_password',None)
            user_name = data.get('user_name',"user")
           
            if user_email is None or user_password is None:
                return JsonResponse({"message": "Email or Password is empty !", "success": "false","status":400})

            try:
                user_exits = user_table.objects.get(user_email=user_email)
                if user_exits:
                    return JsonResponse({"message": "Email Already Registered, Try to login !", "success": "true","status":200})
            except:
                hashed_password = bcrypt.hashpw(user_password.encode('utf-8'), bcrypt.gensalt()).hex()

                instance = user_table(user_email=user_email, user_password=hashed_password, user_name= user_name)
                instance.save()
                return JsonResponse({"message":"Email registered successfully, please Login!","success":"True","status":200})
       
        except Exception as e:
            print("<--------- Exception in API : user_register -----------> ", str(e))
            return JsonResponse({"error":str(e),"success":"false","status":400}) 

@csrf_exempt 
def user_login(request):
    if request.method == "POST":
        try:
            request_data = request.body.decode('utf-8')
            data = json.loads(request_data)

            user_email = data.get('user_email',None)
            user_password = data.get('user_password',None)
           
            if user_email is None or user_password is None:
                return JsonResponse({"message": "Email or Password is empty !", "success": "false","status":400})
            try:
                user_exits = user_table.objects.get(user_email=user_email)
            except:
                return JsonResponse({"message": "Please Register first ,Then Try Again to login !", "success": "false","status":400})

            if user_exits and bcrypt.checkpw(user_password.encode('utf-8'), bytes.fromhex(user_exits.user_password)):
                return JsonResponse({"message": "User Logged in Successfully !", "success": "true","status":200})
            elif user_exits and not bcrypt.checkpw(user_password.encode('utf-8'), bytes.fromhex(user_exits.user_password)):
                return JsonResponse({"message": "Password is Wrong , Try Again!", "success": "false","status":400})
       
        except Exception as e:
            print("<--------- Exception in API : user_register -----------> ", str(e))
            return JsonResponse({"error":str(e),"success":"false"}) 


@csrf_exempt 
def add_books(request):
    if request.method == "POST":
        try:
            request_data = request.body.decode('utf-8')
            data = json.loads(request_data)

            book_name = data.get('book_name',None)
            author_id = data.get('author_id',None)
            stock = data.get('stock',0)
           
            if book_name is None or author_id is None:
                return JsonResponse({"message": "Enter valid Book name and Author !!", "success": "false","status":400})
            try:
                user_exits = book_table.objects.get(book_name=book_name,author_id=author_id)
                if user_exits:
                    book_table.objects.filter(book_name=book_name,author_id=author_id).update(stock= user_exits.stock+ stock)
                    
                    return JsonResponse({"message": "This Specific Book is already present, Updating Stock !", "success": "true","status":200})
            except:
                instance = book_table(book_name=book_name,author_id=author_id,stock=stock)
                instance.save()
                return JsonResponse({"message": "New Book Added to Collection ...", "success": "true","status":200})
       
        except Exception as e:
            print("<--------- Exception in API : user_register -----------> ", str(e))
            return JsonResponse({"error":str(e),"success":"false", "status":400}) 

@csrf_exempt 
def show_Dbcollection(request):
    if request.method == "POST":
        try:
            request_data = request.body.decode('utf-8')
            data = json.loads(request_data)

            book_name = data.get('book_name',None)
            author_id = data.get('author_id',None)
           
            if book_name is None and author_id is None:
                return JsonResponse({"message": "Enter valid Book name and Author to Search for ...", "success": "false","status":400})
            elif book_name and author_id:
                db_collection = book_table.objects.filter(book_name=book_name,author_id=author_id)
            elif book_name and author_id is None:
                db_collection = book_table.objects.filter(book_name=book_name)
            elif author_id and book_name is None:
                db_collection = book_table.objects.filter(author_id=author_id)
            

            selected_fields = db_collection.values('book_name', 'author_id')
            json_data = json.dumps(list(selected_fields))
        
            print(json_data)
            return JsonResponse({"Data Collection":json.loads(json_data), "success": "true","status":200})
            
       
        except Exception as e:
            print("<--------- Exception in API : user_register -----------> ", str(e))
            return JsonResponse({"error":str(e),"success":"false", "status":400}) 