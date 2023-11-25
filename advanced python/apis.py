# import requests
# response = requests.get("https://api.open-notify.org/iss-pass.json")

# print(response.json())




# from tkinter import *
# #import webbrowser
# import requests
# def fun():
#     # webbrowser.open("https://api.kanye.rest/")
#     link_url = "https://api.kanye.rest/"
#     response = requests.get(link_url)
#     link_label = Label(window ,text = response.json())
#     quote = link_label["quote"]
#     mybutton.config(text = quote)

# window = Tk()
# window.title(" Quote Desktop App ")
# window.geometry("600x400")

# newlabel = Label(window,text = " CLICK ON THE BUTTON ")
# newlabel.pack()

# # background_color = '#001f3f'
# # window.configure(bg=background_color)
# mybutton = Button(window,text = "GET", command= fun)
# mybutton.pack()

# window.mainloop()
def fuc(num): 
    for i in num:
       yield (i*i)
num = fuc([1,2,3,4,5,6,7])
#print(num)
for nums in num:
    print(nums)