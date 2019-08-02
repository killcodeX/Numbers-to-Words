import tkinter as tk
HEIGHT= 700
WIDTH= 800
####################################################################
try:
	def convert(num):
		# num = int(input("Enter the number :"))
		number = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
		nty = ["","Ten","Twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninthy"]
		tens = ["","eveven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eigtheen","ninteen"]
		if num > 1100000000:
			print("Not More than 99999")
		else:
			d = [' ',' ', ' ', ' ', ' ' ,' ', ' ', ' ' ,' ', ' ', ' ' ,' ']
			i = 0
			while num>0:  # to get the individual element in d
				d[i] = num%10
				i+=1
				num = num // 10
			n = ""
# for billions-===============

			if (d[11] != ' '):  # here index 5 represent the first elemnt similarly 4= second elemet
				n+=number[d[11]]	+ " Hundred "
			if ((d[10] != ' ')) :
				if (d[10] != 1):   #for eleents like 21,31,21
					n+=nty[d[10]] + number[d[9]]
				elif ((d[10] ==1) and (d[9] == 0)):
					n+=nty[d[10]]
				else: #for elements like 12,13,14
					n+=	tens[d[9]]
			if ((d[9] != ' ') and (d[10] ==' ')):
				n+=number[d[9]]
			if ((d[11] != ' ') or (d[10] != ' ') or (d[9] != ' ')):
				n+=" Billion, "
			#for millions-===============
			if (d[8] != ' '):  # here index 5 represent the first elemnt similarly 4= second elemet
				n+=number[d[8]]	+ " Hundred, "
			if ((d[7] != ' ')) :
				if (d[7] != 1):   #for eleents like 21,31,21
					n+=nty[d[7]] + number[d[6]]
				elif ((d[7] ==1) and (d[6] == 0)):
					n+=nty[d[7]]
				else: 				#for elements like 12,13,14
					n+=	tens[d[6]]
			if ((d[6] != ' ') and (d[7] ==' ')):
				n+=number[d[6]]
			if ((d[8] != ' ') or (d[7] != ' ') or (d[6] != ' ')):
				n+=" Million "
			#==============for thousands-===============
			if (d[5] != ' '):  # here index 5 represent the first elemnt similarly 4= second elemet
				n+=number[d[5]]	+ " Hundred "
			if ((d[4] != ' ')) :
				if (d[4] != 1):   #for eleents like 21,31,21
					n+=nty[d[4]] + number[d[3]]
				elif ((d[4] ==1) and (d[3] == 0)):
					n+=nty[d[4]]
				else: #for elements like 12,13,14
					n+=	tens[d[3]]
			if ((d[3] != ' ') and (d[4] ==' ')):
				n+=number[d[3]]
			if ((d[5] != ' ') or (d[4] != ' ') or (d[3] != ' ')):
				n+=" Thousand, "
#for ones tens hundred=====
			if ((d[2] != ' ') and (d[2] != 0)):  #here index 4 represent the first elemnt similarly 3= second elemet
				n+=number[d[2]]	+ " Hundred "
			if ((d[1] != 0)) :
				if (d[1] != 1):   #for eleents like 21,31,21
					n+=nty[d[1]] + number[d[0]]
				else: #for elements like 12,13,14
					n+=	tens[d[0]]
			label['text']=n
except NameError:
	label['text']="Can letter be converted into word ?"
except TypeError:
	label['text']="Can letter be converted into word ?"

####################################################################
root=tk.Tk(className='Word2Num')

canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

frame=tk.Frame(root,bg='#80C1ff',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry=tk.Entry(frame,font=('Courier',18))
entry.place(relwidth=0.65,relheight=1)

button=tk.Button(frame,text="Enter",font=40,command=lambda:convert(int(entry.get())))
button.place(relx=0.7,relheight=1,relwidth=0.3)

lower_frame=tk.Frame(root,bg='#80C1ff',bd=10)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

label=tk.Label(lower_frame, font=('Courier',18), anchor='nw',bg='white')
label.place(relwidth=1,relheight=1)

root.mainloop()
