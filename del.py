# if (db.query(models.User).count() == 0):
# if (request.password == "Pass@1234"):

#     admin_user = models.User(username=request.username, created_by=request.username,
#                              password=hashing.Hash.bcrypt(request.password), is_admin=True)
#     db.add(admin_user)
#     db.commit()
#     db.refresh(admin_user)
#     access_token = tokens.create_access_token(data={"user": {
#         "username": request.username,"isAdmin": True}})

#     return {"access_token": access_token, "token_type": "bearer"}

# else:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                         detail="Incorrect Passwords")

# else:


# delete html code goes below
# <section class="footer">
#       <div class="col footer-about">
#         <a href="" class="brand-lg"> brands<span>U</span>rl </a>
#         <p>
#           BrandURL is a short URL service that offers custom domain branding,
#           password protection, link expiration, and tracking features. BrandURL
#           provides detailed analytics to track clicks, location, and device
#           type.
#         </p>
#       </div>

#       <div class="col footer-company">
#         <h4>Company</h4>
#         <ul>
#           <li>
#             <a href="http://" target="_blank" rel="noopener noreferrer">
#               Teams
#             </a>
#           </li>
#           <li>
#             <a href="http://" target="_blank" rel="noopener noreferrer">
#               Supports</a
#             >
#           </li>
#           <li>
#             <a href="http://" target="_blank" rel="noopener noreferrer"> FAQ</a>
#           </li>
#           <li>
#             <a href="http://" target="_blank" rel="noopener noreferrer"
#               >Customer Testimonial</a
#             >
#           </li>
#         </ul>
#       </div>
#       <div class="col footer-resources">
#         <h4>Usefull Links</h4>
#         <ul>
#           <li>
#             <a href="http://" target="_blank" rel="noopener noreferrer">
#               Privacy Policy</a
#             >
#           </li>
#           <li>
#             <a href="http://" target="_blank" rel="noopener noreferrer">
#               Terms & Conditions</a
#             >
#           </li>
#           <li>
#             <a href="http://" target="_blank" rel="noopener noreferrer">
#               Refunds</a
#             >
#           </li>
#         </ul>
#       </div>
#     </section>

# if not len(request.username) >= 8:
#     raise HTTPException(status_code=status.HTTP_302_FOUND,
#                         detail=f"{request.username} length must be gretter than 8 character.")
# else:
# else:
#     raise HTTPException(status_code=status.HTTP_302_FOUND,
#                         detail=f"{request.username} already exists.")
# if val_user.count() == 0:
#     new_user = models.User(fullname="Shreeganesh", email_address=request.email_address, created_by=request.email_address,
#                             password=hashing.Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     access_token = tokens.create_access_token(data={"user": {
#         "username": request.username, "email_address": request.email_address, "isAdmin": True}})

#     return {"access_token": access_token, "token_type": "bearer"}

# else:


# @router.get('/verifyemail/{verification_code}')
# def VerifyEmail(verification_code: str, db: Session = Depends(get_db)):
#     result = db.query(models.User).filter(
#         models.User.verification_code == verification_code)

#     if not result:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN, detail='Invalid verification code')
#     else:
#         result.update({"is_active": True, "verification_code": None})
#         db.commit()

#     return {"Account verified successfully!"}


######################################JS################################################################################
# const form = document.getElementById('contact-form');

# form.addEventListener('submit', (event) => {
#   event.preventDefault();
#   const name = document.getElementById('name-input').value;
#   const mobile = document.getElementById('mobile-input').value;
#   const email = document.getElementById('email-input').value;
#   const messages = document.getElementById('messages-input').value;
#   // const data = {name:name, mobile_number:mobile, email:email, messages:messages};

#   fetch('http://127.0.0.1:8000/api/contact-us', {
#     method: 'POST',
#     body: JSON.stringify({name:name, email:email, mobile_number:mobile, messages:messages}),
#     headers: {
#       'Content-Type': 'application/json'
#     }
#   })
#   .then(response => response.json())
#   .then((response) => {
#     if (response.status === 200) {
#     var successMessage = document.getElementById('success-message');
#     successMessage.classList.add("show-message");
#     successMessage.style.display = "block";
#     successMessage.innerHTML = "Thank You for contact us. Our team will reach you as soon as possible.";
#     console.log(successMessage)
#   }else {
#     var errorMessage = document.getElementById('error-message');
#     errorMessage.classList.add("show-message");
#     errorMessage.style.display = "block";
#     errorMessage.innerHTML = response.detail;
#     console.log(errorMessage)
#   }
#   setTimeout(() => {
#     var successMessage = document.getElementById('success-message');
#     var errorMessage = document.getElementById('error-message');
#     successMessage.style.display = "none";
#     errorMessage.style.display = "none";
#   }, 5000);})

#   .then(data => {
#     console.log(data);
#   })

#   .catch(error => {
#     var errorMessage = document.getElementById('error-message');
#     console.error('Error:', error);
#     errorMessage.style.display = "block";
#     errorMessage.innerHTML =error.messages;
#   });

# });


# async function shortItClick() {
#     const response = await fetch("/api/home/app", {
#       method: "post",
#       headers: {
#         'Content-Type': 'application/json'
#       },
#     //   body: JSON.stringify(data)
#     });
#     if (!response.ok) {
#       throw new Error(`HTTP error! Status: ${response.status}`);
#     }
#     const responseData = await response.json();
#     console.log(responseData)
#     return responseData;
#   }

#  document.addEventListener('DOMContentLoaded', (event) => {
#     document.getElementById("myForm").addEventListener("submit", function (e) {
#        e.preventDefault() // Cancel the default action
#        var catName = document.getElementById('catName').value;
#        fetch('/disable/' + catName, {
#              method: 'POST',
#           })
#           .then(resp => resp.text()) // or, resp.json(), etc.
#           .then(data => {
#              document.getElementById("response").innerHTML = data;
#           })
#           .catch(error => {
#              console.error(error);
#           });
#     });
#  });


# const form = document.getElementById('contact-form');
# const successMessage = document.getElementById('success-message');
# const errorMessage = document.getElementById('error-message');

# form.addEventListener('submit', (event) => {
#   event.preventDefault();

#   const name = document.getElementById('name-input').value;
#   const mobile = document.getElementById('mobile-input').value;
#   const email = document.getElementById('email-input').value;
#   const messages = document.getElementById('messages-input').value;
#   // const data = {name:name, mobile_number:mobile, email:email, messages:messages};

#   fetch('http://127.0.0.1:8000/api/contact-us', {
#     method: 'POST',
#     body: JSON.stringify({name:name, email:email, mobile_number:mobile, messages:messages}),
#     headers: {
#       'Content-Type': 'application/json'
#     }
#   })
#   .then(response => response.json())
#   .then(data => {
#     console.log(data);
#     if (data.success) {
#       successMessage.style.display = "block";
#       console.log(successMessage)
#     } else {
#       errorMessage.style.display = "block";
#       console.log(errorMessage)
#     }
#     setTimeout(() => {
#       successMessage.style.display = "none";
#       errorMessage.style.display = "none";
#     }, 10000);
#   })

#   .catch(error => {
#     console.error('Error:', error);
#   });

# });


# const form = document.getElementById('contact-form');

# form.addEventListener('submit', (event) => {
#   event.preventDefault();

#   const name = document.getElementById('name-input').value;
#   const mobile = document.getElementById('mobile-input').value;
#   const email = document.getElementById('email-input').value;
#   const messages = document.getElementById('messages-input').value;
#   const data = {name:name, email:email, mobile_number:mobile, messages:messages};

#   fetch('http://127.0.0.1:8000/api/contact-us', {
#     method: 'POST',
#     body: JSON.stringify(data),
#     headers: {
#       'Content-Type': 'application/json'
#     }
#   })
#   // .then(response => response.json())
#   .then((response) => {
#     if (response.status === 200) {
#     var successMessage = document.getElementById('success-message');
#     successMessage.classList.add("show-message");
#     successMessage.style.display = "block";
#     successMessage.innerHTML = response.detail;
#     console.log(successMessage)
#   }else {
#     var errorMessage = document.getElementById('error-message');
#     errorMessage.classList.add("show-message");
#     errorMessage.style.display = "block";
#     errorMessage.innerHTML = response.detail;
#     console.log(errorMessage)
#   }
#   setTimeout(() => {
#     var successMessage = document.getElementById('success-message');
#     var errorMessage = document.getElementById('error-message');
#     successMessage.style.display = "none";
#     errorMessage.style.display = "none";
#   }, 5000);})
#   .then(data => {
#     console.log(data);
#   })

#   .catch(error => {
#     var errorMessage = document.getElementById('error-message');
#     console.error('Error:', error);
#     errorMessage.style.display = "block";
#     errorMessage.innerHTML =error.messages;
#   });

# });

# perfect code
# const form = document.getElementById('contact-form');

# form.addEventListener('submit', (event) => {
#   event.preventDefault();

#   const name = document.getElementById('name-input').value;
#   const mobile = document.getElementById('mobile-input').value;
#   const email = document.getElementById('email-input').value;
#   const messages = document.getElementById('messages-input').value;
#   const data = {name:name, email:email, mobile_number:mobile, messages:messages};
#   console.log(data)

#   const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
#   const mobilePattern = /^[0-9]{10}$/;

#   if (!emailPattern.test(email)) {
#     var errorMessage = document.getElementById('error-message');
#     errorMessage.classList.add("show-message");
#     errorMessage.style.display = "block";
#     document.getElementById('email-input').focus();
#     errorMessage.innerHTML = "Please enter a valid email address.";
#     return;
#   }
#   if (!mobilePattern.test(mobile)){
#     var errorMessage = document.getElementById('error-message');
#     errorMessage.classList.add("show-message");
#     errorMessage.style.display = "block";
#     document.getElementById('mobile-input').focus();
#     errorMessage.innerHTML = "Please enter a valid 10-digit mobile number.";
#     return;
#   }


#   fetch('http://127.0.0.1:8000/api/contact-us', {
#     method: 'POST',
#     body: JSON.stringify(data),
#     headers: {
#       'Content-Type': 'application/json'
#     }
#   })
#   .then(response => response.json())
#   .then((response) => {
#     if (response.status === 200) {
#     var successMessage = document.getElementById('success-message');
#     successMessage.classList.add("show-message");
#     successMessage.style.display = "block";
#     successMessage.innerHTML = response.detail;

#     //clear the text fields after successfully submited the form
#     document.getElementById('name-input').value = '';
#     document.getElementById('mobile-input').value = '';
#     document.getElementById('email-input').value = '';
#     document.getElementById('messages-input').value = '';
#   }else {
#     var errorMessage = document.getElementById('error-message');
#     errorMessage.classList.add("show-message");
#     errorMessage.style.display = "block";
#     errorMessage.innerHTML = response.detail;

#      //clear the text fields after successfully submited the form
#      document.getElementById('name-input').value = '';
#      document.getElementById('mobile-input').value = '';
#      document.getElementById('email-input').value = '';
#      document.getElementById('messages-input').value = '';
#   }
#   setTimeout(() => {
#     var successMessage = document.getElementById('success-message');
#     var errorMessage = document.getElementById('error-message');
#     successMessage.style.display = "none";
#     errorMessage.style.display = "none";
#   }, 5000);
#   console.log(response);
# })
#   .catch(error => {
#     var errorMessage = document.getElementById('error-message');
#     // console.error('Error:', error);
#     errorMessage.style.display = "block";
#     errorMessage.innerHTML =error.messages;
#   });

# });


#   const name = document.getElementById('name-fields').value;
#   const mobile = document.getElementById('mobile-fields').value;
#   const email = document.getElementById('email-fields').value;
#   const messages = document.getElementById('messages-fields').value;
#   const data = {name:name, email:email, mobile_number:mobile, messages:messages};
#   console.log(data)

#   fetch('http://127.0.0.1:8000/api/contact-us', {
#     method: 'POST',
#     body: JSON.stringify(data),
#     headers: {
#       'Content-Type': 'application/json'
#     }
#   })

#   .then(response => response.json())

#   .then((response) => {
#     if (response.status === 200) {
#     var successMessage = document.getElementById('success-message');
#     successMessage.classList.add("show-message");
#     successMessage.style.display = "block";
#     successMessage.innerHTML = response.detail;

#     //clear the text fields after successfully submited the form
#     document.getElementById('name-fields').value = '';
#     document.getElementById('mobile-fields').value = '';
#     document.getElementById('email-fields').value = '';
#     document.getElementById('messages-fields').value = '';
#   }else {
#     var errorMessage = document.getElementById('error-message');
#     errorMessage.classList.add("show-message");
#     errorMessage.style.display = "block";
#     errorMessage.innerHTML = response.detail

#     //clear the text fields after successfully submited the form
#     document.getElementById('name-fields').value = '';
#     document.getElementById('mobile-fields').value = '';
#     document.getElementById('email-fields').value = '';
#     document.getElementById('messages-fields').value = '';
#   }

#   setTimeout(() => {
#     var successMessage = document.getElementById('success-message');
#     var errorMessage = document.getElementById('error-message');
#     successMessage.style.display = "none";
#     errorMessage.style.display = "none";
#   }, 5000);
#   console.log(response);
#   })

#   .catch(error => {
#     var errorMessage = document.getElementById('error-message');
#     errorMessage.style.display = "block";
#     errorMessage.innerHTML =error.messages;
#   });

# ###########
# const form = document.getElementById('contact-form');
# var successMessage = document.getElementById('success-message');
# var errorMessage = document.getElementById('error-message');

# const name_field = document.getElementById('name-fields');
# const mobile_field = document.getElementById('mobile-fields');
# const email_field = document.getElementById('email-fields');
# const messages_field = document.getElementById('messages-fields');

# form.addEventListener('submit', (event) => {
#   event.preventDefault();
#   if( !validateName()||!validateMobile()||!validateEmail()||!validateMobile()||!validateMassage()){
#     return;
#   }else{
#     const name = document.getElementById('name-fields').value;
#     const mobile = document.getElementById('mobile-fields').value;
#     const email = document.getElementById('email-fields').value;
#     const messages = document.getElementById('messages-fields').value;

#     const data = {name:name, email:email, mobile_number:mobile, messages:messages};
#     console.log(data)

#     fetch('http://127.0.0.1:8000/api/contact-us', {
#       method: 'POST',
#       body: JSON.stringify(data),
#       headers: {
#         'Content-Type': 'application/json'
#       }
#     })
#     .then(response => response.json())
#     .then((response) => {
#       if (response.status === 200){
#       var successMessage = document.getElementById('success-message');
#       successMessage.classList.add("show-message");
#       successMessage.style.display = "block";
#       successMessage.innerHTML = response.detail;

#       //clear the text fields after successfully submited the form
#       document.getElementById('name-fields').value = '';
#       document.getElementById('mobile-fields').value = '';
#       document.getElementById('email-fields').value = '';
#       document.getElementById('messages-fields').value = '';
#     }else {
#       var errorMessage = document.getElementById('error-message');
#       errorMessage.classList.add("show-message");
#       errorMessage.style.display = "block";
#       errorMessage.innerHTML = response.detail;

#        //clear the text fields after successfully submited the form
#       document.getElementById('name-fields').value = '';
#       document.getElementById('mobile-fields').value = '';
#       document.getElementById('email-fields').value = '';
#       document.getElementById('messages-fields').value = '';
#     }
#     setTimeout(() => {
#       var successMessage = document.getElementById('success-message');
#       var errorMessage = document.getElementById('error-message');
#       successMessage.style.display = "none";
#       errorMessage.style.display = "none";
#     }, 5000);
#     console.log(response);
#   })
#     // .catch(error => {
#     //   var errorMessage = document.getElementById('error-message');
#     //   // console.error('Error:', error);
#     //   errorMessage.style.display = "block";
#     //   errorMessage.innerHTML = error.messages;
#     // });
#   }
# });


# function validateName(){
#   const nameValue = name_field.value.trim();
#   if(nameValue === '') {
#       setError('Name field is required');
#       return false;
#     }
#     setError();
#     return true;
# }

# function validateMobile(){
#   const mobileValue = mobile_field.value.trim();
#   if(mobileValue === '') {
#       setError('Mobile number field is required');
#       return false;
#     }else if(!isValidMobileRe(mobileValue)){
#       setError('Mobile number must have 10 didgits');
#       return false;
#     }
#     setError();
#     return true;
# }

# function isValidMobileRe(mobileValue){
#   // const mobileValue = mobile_field.value.trim();
#   const mobilePattern = /^[0-9]{10}$/;
#   return mobilePattern.test(mobileValue);
# }

# function validateEmail(){
#   const emailValue = email_field.value.trim();
#   if(emailValue==='') {
#     setError('Email fields is required');
#     return false;
#     } else if (!isValidEmailPattern(emailValue)) {
#       setError('Provide a valid email address');
#       return false;
#      }
#   setError();
#   return true;
# }

# function isValidEmailPattern(emailValue){
#   // const emailValue = email_field.value.trim();
#   const emailPattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
#   return emailPattern.test(String(emailValue).toLowerCase());
# }

# function validateMassage(){
#  const messageValue = messages_field.value.trim();
#  if(messageValue===''){
#   setError('Messages fields is required');
#   return false;
#  }
#  setError()
#  return true;
# }

# const setError = (message) => {
#   errorMessage.classList.add("show-message");
#   errorMessage.style.display = "block";
#   errorMessage.innerText = message;
# }
# const setSuccess = () => {
#   successMessage.classList.add("show-message");
#   successMessage.style.display = "block";
#   successMessage.innerText = "form submitted succesfully";
#   errorMessage.classList.remove('show-message');
# }


# @router.post("/login", status_code=status.HTTP_200_OK)
# def login(request: Request, request_pass: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     # def login(request: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
#     val_user = db.query(models.User).filter(
#         models.User.username == request_pass.username)
#     print(request_pass.username)
#     print(request_pass.password)

#     errors = []
#     if not val_user.first():
#         # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#         # detail="User does not exists")
#         errors.append("User does not exists")
#         return templates.TemplateResponse("signin.html", {"request": request, "errors": errors})
#     else:
#         # verify password between requesting by a user & database password
#         if not hashing.Hash.verify(val_user.first().password, request_pass.password):
#             # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#             #                     detail="Incorrect Passwords")

#             errors.append("Incorrect Passwords")
#             return templates.TemplateResponse("signin.html", {"request": request, "errors": errors})
#         else:
#             access_token = tokens.create_access_token(data={"user": {
#                 "username": val_user.first().username, "isAdmin": val_user.first().is_admin}})

#             # return {"access_token": access_token, "token_type": "bearer"}
#             return templates.TemplateResponse("sigin.html", {"request": request, "access_token": access_token, "token_type": "bearer"})
#             # return RedirectResponse("/", status_code=303)

 # return {"access_token": access_token, "token_type": "bearer", "status": 200}

            # response = templates.TemplateResponse(
            #     "/dashboard.html", {"request": request, "status": 200})
            # response = RedirectResponse(url="/dashboard.html")
            # print(response)
            # response.set_cookie(key="access_token",
            #                     value=f"Bearer {jwt_token}", httponly=True)
            # # return {"access_token": access_token, "token_type": "bearer", "status": 200}
            # return response
# from fastapi import APIRouter, Depends, status, HTTPException, Response, Request
# from fastapi.responses import JSONResponse
# from botbuilder.core import BotFrameworkAdapter, TurnContext, MessageFactory,BotFrameworkAdapterSettings
# from botbuilder.schema import Activity, ActivityTypes
# import os
# from dotenv import dotenv_values, load_dotenv

# config = dotenv_values(".env")
# connect = load_dotenv()

# router = APIRouter(tags=["ChatBot"])

# # adapter = BotFrameworkAdapter({
# #     "app_id":  os.getenv('AZURE_APP_ID'),
# #     "app_password":  os.getenv('AZURE_APP_PASSWORD'),
# # })

# app_settings = BotFrameworkAdapterSettings(
#     app_id=os.getenv('AZURE_APP_ID'),
#     app_password= os.getenv('AZURE_APP_PASSWORD')
# )

# adapter = BotFrameworkAdapter(app_settings)
# # Your Bot logic
# class MyBot:
#     async def on_turn(self, turn_context: TurnContext):
#         if turn_context.activity.type == ActivityTypes.message:
#             await turn_context.send_activity(MessageFactory.text(f"You said: {turn_context.activity.text}"))

# # Instantiate the Bot
# bot = MyBot()

# # Handle incoming messages
# async def handle_activity(request: Request, adapter: BotFrameworkAdapter):
#     body = await request.body()
#     try:
#         await adapter.process_activity(body, request.headers["Authorization"], bot.on_turn)
#         return JSONResponse(content={}, status_code=200)
#     except Exception as e:
#         return JSONResponse(content={"error": str(e)}, status_code=500)

# # Define the endpoint for receiving messages
# @router.post("/api/messages")
# async def messages_endpoint(request: Request, adapter: BotFrameworkAdapter = Depends()):
#     return await handle_activity(request, adapter)

#  <script>
#       document.addEventListener('DOMContentLoaded', function () {
#           const chatButton = document.getElementById('chatButton');
#           const webchatContainer = document.getElementById('webchatContainer');
#           const closeButton = document.getElementById('closeButton');
  
#           chatButton.addEventListener('click', async function () {
              
#               const res = await fetch('https://directline.botframework.com/v3/directline/tokens/generate', {
#                   method: 'POST',
#                   headers: { 'Authorization': 'Bearer JS8B8oqLjfw.GY2L8zoJTmwammep5oPep9D9OOiIaRlMY35IhSlG1pI' }
#               });
#               const { token } = await res.json();
  
#               const styleSet = window.WebChat.createStyleSet({
                 
#               });
  
#               window.WebChat.renderWebChat(
#                   {
#                       directLine: window.WebChat.createDirectLine({ token }),
#                       userID: 'WebChat_UserId',  
#                       username: 'Web Chat User',  
#                       locale: 'en-US',
#                       styleSet
#                   },
#                   document.getElementById('webchatContainer')
#               );
  
              
#               webchatContainer.style.display = 'block';
#               closeButton.style.display = 'block';
#               chatButton.style.display = 'none';
#           });

#           closeButton.addEventListener('click', function () {
#             webchatContainer.style.display = 'none';
#             closeButton.style.display = 'none';
#             chatButton.style.display = 'block';
#         });
#       });


#   </script> 

# aiohttp==3.8.5
# aiosignal==1.3.1
# anyio==3.6.2
# arrow==1.3.0
# async-timeout==4.0.3
# asyncio==3.4.3
# attrs==23.1.0
# bcrypt==4.0.1
# binaryornot==0.4.4
# botbuilder-core==4.14.6
# botbuilder-integration-aiohttp==4.14.6
# botbuilder-schema==4.14.6
# botframework-connector==4.14.6
# botframework-streaming==4.14.6
# certifi==2023.11.17
# cffi==1.16.0
# chardet==5.2.0
# charset-normalizer==3.3.2
# click==8.1.3
# colorama==0.4.6
# cookiecutter==1.7.0
# cryptography==41.0.7
# decorator==5.1.1
# dnspython==2.3.0
# ecdsa==0.18.0
# email-validator==2.0.0.post2
# fastapi==0.89.1
# frozenlist==1.4.0
# future==0.18.3
# greenlet==2.0.2
# h11==0.14.0
# idna==3.4
# isodate==0.6.1
# Jinja2==3.1.2
# jinja2-time==0.2.0
# jsonpickle==1.4.2
# MarkupSafe==2.1.3
# msal==1.26.0
# msrest==0.6.21
# multidict==6.0.4
# oauthlib==3.2.2
# passlib==1.7.4
# poyo==0.5.0
# psycopg2==2.9.5
# psycopg2-binary==2.9.9
# pyasn1==0.4.8
# pycparser==2.21
# pydantic==1.10.4
# PyJWT==2.8.0
# python-dateutil==2.8.2
# python-dotenv==0.21.1
# python-jose==3.3.0
# python-multipart==0.0.5
# requests==2.31.0
# requests-oauthlib==1.3.1
# rsa==4.9
# six==1.16.0
# sniffio==1.3.0
# SQLAlchemy==2.0.23
# starlette==0.22.0
# types-python-dateutil==2.8.19.14
# typing_extensions==4.4.0
# urllib3==1.26.18
# uvicorn==0.20.0
# validators==0.20.0
# whichcraft==0.6.1
# yarl==1.9.4


# <button id="chatButton">Chat with us</button>
# <button id="closeButton">×</button>
# <div id="webchatContainer"></div>


# /*chat bot*/
# <script src="https://cdn.botframework.com/botframework-webchat/latest/webchat.js"></script>

# #chatButton {
#     position: fixed;
#     bottom: 40px;
#     right: 20px;
#     background-color: dodgerblue;
#     color: #ffffff;
#     padding: 12px;
#     border: none;
#     border-radius: 5px;
#     cursor: pointer;
#     /* z-index: 2; */
# }

# #webchatContainer {
#     display: none;
#     position: fixed;
#     bottom: 20px;
#     right: 20px;
#     width: 300px;
#     height: 400px;
#     border: 1px solid #ccc;
#     border-radius: 5px;
#     overflow: hidden;
#     /* z-index: 1; */
# }

# #closeButton {
#     display: none;
#     position: fixed;
#     bottom: 436px;
#     right: 40px;
#     background-color: transparent;
#     border: none;
#     padding: 5px;
#     cursor: pointer;
#     z-index: 1;
#     font-size: 30px;
# }


# // azure bot implement
# document.addEventListener('DOMContentLoaded', function () {
#   const chatButton = document.getElementById('chatButton');
#   const webchatContainer = document.getElementById('webchatContainer');
#   const closeButton = document.getElementById('closeButton');

#   chatButton.addEventListener('click', async function () {
      
#       const res = await fetch('https://directline.botframework.com/v3/directline/tokens/generate', {
#           method: 'POST',
#           headers: { 'Authorization': 'Bearer JS8B8oqLjfw.GY2L8zoJTmwammep5oPep9D9OOiIaRlMY35IhSlG1pI' }
#       });
#       const { token } = await res.json();

#       const styleSet = window.WebChat.createStyleSet({
         
#       });

#       window.WebChat.renderWebChat(
#           {
#               directLine: window.WebChat.createDirectLine({ token }),
#               userID: 'WebChat_UserId',  
#               username: 'Web Chat User',  
#               locale: 'en-US',
#               styleSet
#           },
#           document.getElementById('webchatContainer')
#       );

      
#       webchatContainer.style.display = 'block';
#       closeButton.style.display = 'block';
#       chatButton.style.display = 'none';
#   });

#   closeButton.addEventListener('click', function () {
#     webchatContainer.style.display = 'none';
#     closeButton.style.display = 'none';
#     chatButton.style.display = 'block';
# });
# });

# <section class="intro">
#   <div class="intro-row">
#     <h1>
#       <!-- Shorter url for your solution -->
#       Trim your lengthy URL instantly!
#       <!-- Shorter URL  <br>
#       for your solution -->
#     </h1>
#     <p>
#       Make custom short URLs,QR Codes for your solution & share it anywhere. Hassle free !
#     </p>
#     <div class="btn-items">
#       <input
#         type="url"
#         class="link-enter"
#         placeholder="Paste here long url"
#         id="lng-url-text"
#         required
#       />
#       <button class="btn" id="shrt-lnk-btn" type="submit">Short It</button>
#       <div id="error-message" class="hidden"></div>
#     </div>
#     <div class="btn-items" id="cpy-url-div">
#       <input
#         type="url"
#         class="link-enter"
#         id="shrt-url-text"
#         value=""
#         readonly
#       />
#       <button class="btn" id="shrt-cpy-btn">
#         <i class="bx bxs-copy-alt"></i>
#       </button>
#     </div>
#   </div>
#   <!-- <div class="img-intro">
#     <img
#       src="{{url_for('static',path='images/url_short.svg')}}"
#       alt=""
#       srcset=""
#     />
#   </div> -->
# </section>
# @import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

# * {
#     margin: 0;
#     padding: 0;
#     /* scroll-behavior: smooth; */
#     /* background-color: #fff; */

# }

# html {
#     scroll-behavior: smooth;
# }

# body {
#     font-family: "Open Sans", sans-serif;
# }

# :root {
#     --blue: #1e90ff;
#     --white: #ffffff;
#     --black: #000000;
#     --gray: #838E95;
#     --font-color: #869ab8;
#     --btn-color: #313232;
#     --border-btn: 0.0.1rem;
#     --btn-margin: 0.5rem;
#     --btn-padding: 0.5rem;
#     --h2: 1.5rem;
#     --button-click-blue: rgb(53, 147, 241);
#     --insta-color: #E1306C;
#     --twitter-color: #00ACEE;
#     --facebook-color: #3b5998;

# }

# /* utility */
# .sub-head {
#     color: var(--black);
#     font-size: 1.18rem;
#     margin: 0.7rem 0.5rem;
#     text-align: left;
# }

# .sub-para {
#     color: var(--font-color);
#     padding: 0.5rem 0.515rem;
#     font-size: 1.1rem;
#     font-family: sans-serif;
#     color: #0F4880;
# }

# .btn {
#     text-decoration: none;
#     border-radius: 0.3rem;
#     color: var(--btn-color);
#     padding: 0.5rem 1.19rem;
#     margin: 0.4rem 0.4rem;
#     outline: none;
# }

# h1 {
#     color: var(--black);
#     font-size: 2.3rem;
#     margin: 0.7rem 1.5rem;
# }

# /* navigation bar */
# #navbar {
#     display: flex;
#     justify-content: space-between;
#     align-items: center;
#     background-color: #0F4880;
#     padding: 0.5rem;
#     flex-wrap: wrap;
# }

# .left ul {
#     display: flex;
#     margin: 0;
# }

# .left ul li {
#     list-style: none;
# }

# .left ul li {
#     padding: 0.5rem;
#     text-decoration: none;
#     font-size: 1rem;
#     padding: .4rem 1rem;
#     color: white;
#     text-transform: uppercase;
#     text-align: center;
# }

# .left ul li .nav-link {
#     display: block;
#     padding: 0;
#     font-size: 1rem;
#     font-weight: 400;
#     color: white;
#     text-decoration: none;
#     background: none;
#     border: 0;
#     transition: none;
# }


# .left ul li:hover {
#     color: gray;

# }

# .left ul li.active {
#     background-color: dodgerblue;
#     border-radius: 2px;
#     color: white;
# }

# .right {
#     display: flex;
# }

# .right .btn:nth-child(1) {
#     padding: 0.5rem 1.19rem;
#     color: white;
#     border: 0.81px solid white;
# }

# .right .btn:nth-child(2) {
#     background-color: var(--blue);
#     color: white;
# }

# .right .btn:nth-child(1):hover {
#     background-color: #0A2F53;
#     ;
# }

# .right .btn:nth-child(2):hover {
#     background-color: #0A2F53;
#     border: 0.81px solid white;
# }

# .left .logo-name {
#     text-decoration: none;
#     color: white;
#     font-size: 1.2rem;
#     font-family: Arial, sans-serif;
#     margin-left: 0.5rem;
#     display: none;
# }

# .left .logo-name span {
#     color: dodgerblue;
# }

# .right {
#     margin-right: 0.8rem;
# }

# .right .menu-icon {
#     color: white;
#     font-size: 1.5rem;
#     cursor: pointer;
#     padding: 0.5rem;
#     margin: 0.4rem;
#     display: none;

# }
# .sidebar {
#     position: fixed;
#     top: 0;
#     right: -100%;
#     height: 100%;
#     width: 260px;
#     padding: 20px 0;
#     color: white;
#     background-color: #0F4880;
#     box-shadow: 0 5px 1px rgba(0, 0, 0, 0.1);
#     transition: all 0.4s ease;
#     z-index: 1;
# }

# .logo {
#     display: flex;
#     align-items: center;
#     margin: 0 24px;
# }

# .logo .menu-icon {
#     color:white;
#     font-size: 24px;
#     margin-right: 14px;
#     cursor: pointer;
# }

# .logo .logo-name {
#     color: white;
#     font-size: 22px;
#     font-family: Arial, sans-serif;
#     font-weight: 500;
#     text-decoration: none;
#     margin-bottom: 0px;
# }

# .logo .logo-name span {
#     color: dodgerblue;
# }

# nav.open .sidebar {
#     right: 0;
# }

# .sidebar .sidebar-content {
#     display: flex;
#     height: 100%;
#     flex-direction: column;
#     justify-content: space-between;
#     padding: 30px 16px;
# }

# .sidebar-content .lists {
#     padding-left: 01rem;
# }

# .sidebar-content .list {
#     list-style: none;

# }

# .list .nav-link {
#     display: flex;
#     align-items: center;
#     margin: 8px 0;
#     padding: 9px 12px;
#     /* border-radius: 8px; */
#     text-decoration: none;
# }

# .lists .nav-link:hover {
#     background-color: dodgerblue;
# }

# .nav-link .icon {
#     margin-right: 14px;
#     font-size: 20px;
#     color: #707070;
# }

# .nav-link .list {
#     font-size: 16px;
#     color: #707070;
#     font-weight: 400;
# }

# .lists .nav-link:hover .icon,
# .lists .nav-link:hover .link {
#     color: #333;
# }

# .list .btn {
#     border-radius: 0.3rem;
#     padding: 0.5rem 1.6rem;
#     background-color: var(--blue);
#     color: white;
#     width: 87%;
# }

# .lists .list.active {
#     border-radius: 1px;
#     color: white;
#     width: 92%;
#     background-color: #0A2F53;
# }

# /* main start  */
# .intro {
#     display: flex;
#     align-items: center;
#     justify-content: center;
#     background-color: #fff;
#     height: 87vh;
#     padding: 0rem 0.5rem;
#     background-image: linear-gradient(to right, #E7EDF2, #DBE4EC);
# }



# .intro div h1 {
#     color: #0F4880;
#     font-size: 2.9rem;
#     text-align: center;
#     text-transform: uppercase;
#     font-family: "Poppins", sans-serif;
#     font-weight: 500;
#     font-style: normal;
# }

# h1 strong {
#     color: #339933;
# }

# h1 span {
#     color: #339933;
# }

# .intro div p {
#     color: #0F4880;
#     padding: 0.5rem 10rem;
#     font-size: 1.18rem;
#     font-family: sans-serif;
#     line-height: 0.5;
#     text-align: center;

# }


# .intro .btn-items {
#     display: flex;
#     flex-direction: column;
#     justify-content: center;
#     align-items: center;
#     text-align: center;
#     margin: 0rem 4.7rem;
# }

# .btn-items .input-items {
#     width: 100%;
# }

# .intro div .btn-items .hidden {
#     display: none;
#     text-align: center;
# }

# .intro div .btn-items #error-message {
#     background-color: red;
#     color: white;
#     transition: opacity 5s ease-in-out;
#     padding: 0.5rem 1.5rem;
#     margin: 0.2rem 0rem;
#     border-radius: 0.3rem;
#     width: calc(100% - 78px);
#     max-width: 549px;
# }

# .intro div .btn-items .show-message {
#     opacity: 1;
# }

# .intro .btn-items input {
#     padding: 0.5rem 1.5rem;
#     color: black;
#     cursor: text;
#     font-size: 1rem;
#     margin: 0.5rem 0rem;
#     outline: none;
#     background-color: rgb(255, 255, 255);
#     max-width: 265px;
#     border: 1.5px solid rgb(238, 238, 238);
#     border-radius: 4px;
#     width: calc(100% - 134px);
#     max-width: 549px;
# }

# .intro .btn-items button {
#     background-color: #0F4880;
#     color: white;
#     margin: 0.6rem 0.5rem;
#     font-size: 1rem;
#     cursor: pointer;
#     outline: none;
#     padding: 0.56rem 1rem;
#     margin-left: 0.5rem;
#     margin-bottom: 0.8rem;
#     border-radius: 4px;
#     text-transform: uppercase;
#     width: calc(100% - 134px);
#     max-width: 549px;
# }



# .intro div .btn-items button:hover {
#     background-color: #0A2F53;
# }

# .intro div #cpy-url-div {
#     display: none;
# }

# .intro div .btn-items #shrt-cpy-btn {
#     padding: 0.5rem 2.5rem;
# }

# .intro div #cpy-url-div .green-copied {
#     background-color: green;
#     color: white;
#     transition: opacity 5s ease-in-out;
#     padding: 0.5rem 1.2rem;
# }

# .img-intro img {
#     width: 40vw;
#     height: 60vh;
# }

# /* features sections*/

# .features {
#     display: flex;
#     flex-direction: column;
#     justify-content: center;
#     align-items: center;
#     height: 100vh;
#     background-image: linear-gradient(to bottom right, #2996FF, #092B4D);
#     opacity: 0.9;
# }

# .features {
#     display: flex;
#     flex-direction: column;
#     justify-content: center;
#     align-items: center;
#     height: 100vh;
#     opacity: 0.9;
#     background-color: white;
# }

# .features .para-features {
#     color: #DDEEFF;
#     font-size: 14px;
# }

# .para-features span {
#     color: #FFB733;
#     font-size: 15px;
#     margin-left: 0.2rem;
#     display: inline-block;
#     animation: moveUpDown 4s ease-in-out infinite;
# }

# @keyframes moveUpDown {

#     0%,
#     100% {
#         transform: scale(1);
#         /* Starting and ending size */
#     }

#     50% {
#         transform: scale(1.1);
#         /* Expand */
#     }

#     60% {
#         transform: scale(0.9);
#         /* Contract */
#     }
# }


# .features h1 {
#     font-size: 1.5rem;
#     color: var(--black);
#     padding: 0.5rem 0.1rem;
#     text-align: center;
# }


# .fs-row {
#     display: grid;
#     grid-template-columns: auto auto auto auto;
#     gap: 0.5rem;
#     justify-content: space-evenly;
#     align-items: center;
#     padding: 0.5rem;

# }

# .features .fs-row .fs-items {
#     display: flex;
#     flex-direction: column;
#     justify-content: space-between;
#     align-items: center;
#     padding: 1rem 0.3rem;
#     margin: 1rem;
#     border: #f8f9fa;
#     text-align: center;
#     background-color: white;
#     border-radius: 5px;
#     box-shadow: 0 2px 3px -1px rgba(0, 0, 0, 0.1);

# }

# .features .fs-row .fs-items .fs-icons {
#     display: flex;
#     flex-direction: column;
#     justify-content: space-between;
#     align-items: start;
#     padding: 0.2rem 0.89rem;
#     margin: 1.219rem 1rem;
#     border: #f8f9fa;
#     border-radius: 1rem;
# }

# .fs-icons i {
#     font-size: 3.5rem;
#     color: white;
#     background-color: var(--blue);
#     width: 4.5rem;
#     height: 4.5rem;
#     text-align: center;
#     align-items: center;
#     padding: 0.5rem;
#     border-radius: 50%;
# }


# .services-list .service-block {
#     margin-bottom: 25px;
# }

# .services-list .service-block .ico {
#     font-size: 38px;
#     float: left;
# }

# .services-list .service-block .text-block {
#     margin-left: 58px;
# }

# .services-list .service-block .text-block .name {
#     font-size: 20px;
#     font-weight: 900;
#     margin-bottom: 5px;
# }

# .services-list .service-block .text-block .info {
#     font-size: 16px;
#     font-weight: 300;
#     margin-bottom: 10px;
# }

# .services-list .service-block .text-block .text {
#     font-size: 12px;
#     line-height: normal;
#     font-weight: 300;
# }

# .highlight {
#     color: dodgerblue;
#     ;
#     font-weight: bold;
# }



# /* faq */
# #faq-section {
#     padding: 2.5rem;
#     margin: 2rem 0rem;
# }

# .faqs-container {
#     font-family: "Roboto", sans-serif;
#     margin: 0 auto;
# }


# .faqs-container h2 {
#     padding: 4px 32px;
#     font-size: 28px;
#     text-align: center;
#     margin-bottom: 3.5rem;
#     align-items: center;
# }

# .content-container {
#     padding: 0.5rem 0.5rem;
#     border: 0.05rem solid #F0F1F8;
#     border-radius: 0.15rem;
#     margin: 1.2rem 0rem;
# }

# .content-container .faq-header {
#     display: flex;
#     align-items: center;
#     position: relative;
#     cursor: pointer;
# }

# .content-container .faq-header .open,
# .content-container .faq-header .close {
#     position: absolute;
#     right: 0;
#     padding: 0 32px;
#     font-size: 22px;
#     font-weight: bold;
#     transform: translateY(-8px);
#     opacity: 0;
#     transition: all 500ms;
# }

# .content-container .faq-header .open.active,
# .content-container .faq-header .close.active {
#     opacity: 1;
#     transform: translateY(0);
#     color: black;

# }

# .content-container .faq-header h3 {
#     font-size: 20px;
#     padding: 0 32px;
#     margin-top: 0.6rem;
# }

# .content-container .content {
#     padding: 0px 32px;
#     line-height: 2;
#     max-height: 0;
#     overflow: hidden;
#     transition: all 500ms;
#     margin-top: 0.5rem;
# }

# .content-container .content.active {
#     max-height: 800px;
# }


# /* footer section */
# .footer {
#     display: flex;
#     padding: 2rem;
#     background-color: #0F4880;
#     height: 43vh;
#     justify-content: center;
# }

# .footer .col {
#     width: 41%;
#     padding: 0.5rem 2rem;
#     margin: 0.5rem;
#     background-color: #E1306C;
# }

# .footer .footer-about a {
#     text-decoration: none;
#     color: white;
# }

# .footer .footer-about .brand-lg {
#     text-decoration: none;
#     text-align: center;
#     color: white;
#     font-size: 1.65rem;
#     font-family: Arial, sans-serif;
# }

# .footer .footer-about p {
#     font-size: 1rem;
#     font-family: Arial, sans-serif;
#     padding-top: 0.4rem;
#     color: var(--gray);
# }

# .footer .footer-about .brand-lg span {
#     font-family: 'Satisfy', cursive;
#     color: dodgerblue;
#     font-size: 1.59rem;
# }

# .footer .footer-company h4 {
#     color: white;
#     font-size: 1.3rem;
#     font-family: Georgia, 'Times New Roman', Times, serif;
#     text-align: left;
#     padding: 0.5rem 0rem;
# }

# .footer .footer-company ul li {
#     list-style: none;
#     font-family: sans-serif;
#     padding: 0.34rem 0rem;
# }

# .footer .footer-company ul li a {
#     color: gray;
#     text-decoration: none;
#     font-size: 1rem;
# }

# .footer .footer-resources h4 {
#     color: white;
#     font-size: 1.11rem;
#     font-family: Georgia, 'Times New Roman', Times, serif;
#     text-align: left;
#     padding: 0.5rem 0rem;
# }

# .footer .footer-resources ul li {
#     list-style: none;
#     font-family: sans-serif;
#     padding: 0.34rem 0rem;
# }

# .footer .footer-resources ul li a {
#     color: gray;
#     text-decoration: none;
#     font-size: 1rem;
# }


# /* sub-footer section*/
# .sub-footer {
#     display: flex;
#     background-color: #0F4880;
#     height: 10vh;
#     justify-content: space-between;
#     align-items: center;
#     flex-wrap: wrap;
#     padding: 0.5rem;
# }

# .sub-footer .copy-rights p {
#     font-size: 1em;
#     margin: 0.0912rem;
#     font-family: sans-serif;
#     color: white;
#     padding-left: 0.7rem;
# }

# .sub-footer .copy-rights p a {
#     color: white;
#     text-decoration: none;
#     font-size: 1rem;
#     font-family: Arial, sans-serif;
# }

# .sub-footer .copy-rights p a span {
#     font-family: 'Satisfy', cursive;
#     color: dodgerblue;
#     font-size: 1rem;
# }

# .sub-footer .social-icons a {
#     margin: 0.0912rem 0.45rem;
#     color: white;
# }

# .sub-footer .social-icons a i {
#     font-size: 1.21rem;
#     /* color: white; */
# }

# .sub-footer .social-icons a i:first-child:hover {
#     color: var(--insta-color);
# }

# .sub-footer .social-icons a i:nth-child(2):hover {
#     color: var(--twitter-color);
# }

# .sub-footer .social-icons a i:nth-child(3):hover {
#     color: var(--facebook-color);
#     ;
# }

# @media (min-width:945px) and (max-width:1021px) {
#     .intro {
#         height: 48vh;
#     }

#     .features {
#         height: 48vh;
#     }
# }

# @media only screen and (max-width: 945px) {

#     .left ul {
#         display: none;
#     }

#     .left .logo-name {
#         display: block;
#     }

#     .right .btn:nth-child(1) {
#         display: none;
#     }

#     .right .btn:nth-child(2) {
#         display: none;
#     }

#     .right .menu-icon {
#         display: block;
#     }

# }

# @media (min-width:768px) and (max-width:945px) {


#     .intro {
#         flex-wrap: wrap;
#         height: 60vh;
#     }

#     .intro .img-intro {
#         display: none;
#     }

#     /* .features {
#         height: 120vh;
#     } */
#     .features {
#         height: 105vh;
#     }

#     .features .fs-row {

#         display: block;

#     }


#     .features .fs-row .fs-items {
#         text-align: center;
#         align-items: center;
#         padding: 1rem 0rem;
#         margin-top: 2.8rem;
#     }

#     .fs-items .fs-icons {
#         margin-bottom: 0rem;
#     }

#     .sub-head {
#         margin: 0.6rem auto;
#     }

#     .sub-para {
#         text-align: center;
#         padding: 0.5rem 1rem 1rem 1rem;
#         margin: 0rem;
#     }

#     /* #services {
#         height: 95vh;
#     } */
# }

# @media only screen and (max-width: 768px) {

#     .intro {
#         flex-wrap: wrap;
#         height: 60vh;
#     }

#     .intro .img-intro {
#         display: none;
#     }
#     .intro div h1 {
#         font-size: 1.9rem;
#     }
#     .features .fs-row {
#         display: block;

#     }

#     .intro .btn-items input {
#         padding: 0.5rem 0.7rem;
#         width: calc(100% - 78px);
#         max-width: 517px;
#     }

#     .intro .btn-items button {
#         width: calc(100% - 78px);
#         max-width: 549px;
#     }


#     .features {
#         height: 115vh;
#     }
    
#     .features .fs-row .fs-items {
#         text-align: center;
#         align-items: center;
#         padding: 1rem 0rem;
#         margin-top: 1.8rem;
#     }

#     .fs-items .fs-icons {
#         margin-bottom: 0rem;
#     }

#     .sub-head {
#         margin: 0.6rem auto;
#     }

#     .sub-para {
#         text-align: center;
#         padding: 0.5rem 1rem 1rem 1rem;
#         margin: 0rem;
#     }

#     .content-container .faq-header h3 {
#         font-size: 18px;
#     }
# }

# @media (min-width:376px) and (max-width:580px) {
#     .intro div h1 {
#         font-size: 2rem;
#         padding-bottom: 1rem;
#     }

#     .features {
#         height: 110vh;
#     }

#     .intro .btn-items {
#         padding-top: 1rem;
#     }

#     .btn-items .input-items {
#         width: 80%;
#         margin: auto;
#     }


#     .intro div p {
#         font-size: 1rem;

#     }

#     .intro .btn-items {
#         text-align: start;
#         margin-left: 2rem;
#         text-align: center;
#         margin: auto;
#     }

#     .intro .btn-items input {
#         padding: 0.5rem 0.7rem;
#         width: calc(100% - 78px);
#         max-width: 517px;
#     }

#     .intro .btn-items button {
#         width: calc(100% - 78px);
#         max-width: 549px;
#     }


#     /* #feature{
#         height: 117vh;
#     } */
#     .features {
#         height: 141vh;
#     }

#     .sub-para {

#         font-size: 17px;
#     }

# }


# @media (min-width:290px) and (max-width:375px) {
#     .intro div h1 {
#         font-size: 1.5rem;
#         padding-bottom: 0.6rem;
#         margin: 0.3rem 0.4rem;
#     }

#     .intro div p {
#         padding: 0.5rem 1.8rem 0rem 0.4rem;

#     }

#     .btn-items .input-items {
#         width: 151%;
#     }

#     .intro .btn-items {
#         padding: 0rem;
#         margin-top: 1rem;
#     }

#     .intro .btn-items button {
#         padding: 0.56rem 5.5rem;
#         width: 75%;
#         margin: 0;

#     }

#     .intro .btn-items input {
#         padding: 0.5rem 0.7rem;
#         width: calc(100% - 78px);
#         max-width: 517px;
#     }

#     .intro .btn-items button {
#         width: calc(100% - 78px);
#         max-width: 549px;
#         font-size: 13px;
#     }


#     .intro .btn-items button {
#         width: calc(100% - 76px);
#         max-width: 549px;
#         font-size: 13px;
#     }

#     /* .features {
#         height: 120vh;
#     } */
#     .features {
#         height: 134vh;
#     }

#     #feature h2 {
#         text-align: center;
#     }

#     .para-features {
#         font-size: 13px;
#     }

#     .faqs-container h2 {
#         font-size: 23px;

#     }

#     .content-container .faq-header .open,
#     .content-container .faq-header .close {
#         padding: 0 10px;
#     }

#     .content.active p {
#         font-size: 0.8rem;
#     }

#     .sub-footer {
#         height: 17vh;
#         flex-direction: column-reverse;
#         justify-content: center;
#     }

#     .sub-footer .copy-rights {
#         margin-top: 1.2rem;

#     }

# }

# @media (min-width: 290px) and (max-width: 430px) {

#     .intro div p {
#         font-size: 10px;
#         text-align: center;
#         margin: 0;
#         padding: orem;
#         padding: 0rem 1.5rem;
#         margin-bottom: 0.5rem;
#     }

#     /* .btn-items .input-items {
#     width: 10%;
# } */
#     #feature {
#         height: 113vh;
#     }

#     #feature h2 {
#         font-size: 16px;
#     }

#     #featureservices .para-features {
#         font-size: 12px;
#     }

#     .sub-para {

#         padding: 0.5rem;
#         font-size: 13px;
#     }

#     .faqs-container h2 {
#         font-size: 18px;
#     }

#     .faqs-container h2 {
#         margin-bottom: 2.5rem;
#     }

#     .content-container .faq-header h3 {
#         font-size: 12px;
#     }

#     content.active p {

#         font-size: 9px;
#     }

#     .sub-footer {
#         height: 17vh;
#         flex-direction: column-reverse;
#         justify-content: center;
#     }

#     .sub-footer .copy-rights {
#         margin-top: 1.2rem;

#     }
# }

# @media (min-width: 280px) and (max-width:388px) {
#     .intro {
#         height: 75vh;
#     }
#     .intro .btn-items input {
#         padding: 0.5rem 0.7rem;
#         width: calc(100% - 4px);
#         max-width: 542px;
#     }

#     .intro .btn-items button {
#         padding: 0.5rem 0.7rem;
#         width: calc(100% - 4px);
#         max-width: 549px;
#         margin-left: 0rem;
#     }

#     /* .btn-items .input-items {
#         width: 150%;
#     } */
#     .btn-items .input-items {
#         width: 150%;
#         margin: auto;
#         margin-left: -3rem;
#     }

#     .features {
#         height: 148vh;
#     }

#     .features h2 {
#         font-size: 17px;
#     }

#     .features .para-features {
#         font-size: 11px;
#     }

#     .sub-footer {
#         height: 17vh;
#         flex-direction: column-reverse;
#         justify-content: center;
#     }

#     .sub-footer .copy-rights {
#         margin-top: 1.2rem;

#     }
# }

# @media (min-width:390px) and (max-width: 430px) {
#     .features {
#         height: 118vh;
#     }
# }

# @media only screen and (max-width: 375px) {
#     .features {
#         height: 149vh;
#     }
# }

# @media only screen and (max-width: 280px) {
#     .intro div h1 {
#         font-size: 1.5rem;
#         margin: 0rem;
#     }

#     .intro .btn-items {
#         margin: 0rem 3.5rem;
#         margin-left: 4.5rem;
#     }

#     .features {

#         height: 177vh;
#     }

#     #faq-section {
#         padding: 2.5rem 0rem;

#     }

#     .faqs-container h2 {
#         font-size: 17px;
#     }

#     .content-container .faq-header h3 {
#         font-size: 13px;
#     }

#     .sub-footer {
#         height: 17vh;
#         flex-direction: column-reverse;
#         justify-content: center;
#     }

#     .sub-footer .copy-rights {
#         margin-top: 1.2rem;

#     }

# }