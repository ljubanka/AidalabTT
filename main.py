from Tkinter import *
import time
import random
r = 25 #ball radius

class App:
	def __init__(self, master):
		self.master = master
		self.frame = Frame(self.master)
		self.frame.pack(fill=BOTH, expand=1)		
		
		self.canvas = Canvas(self.frame, bg="orange", highlightthickness=0)
		self.canvas.configure(width = 600, height = 400)
		self.canvas.pack(fill="both", expand="yes")		
		self.canvas.bind('<Configure>', self.resize)		
		
		self.draw_objects()		
		self.delta = self.set_direction()
		while 0 in self.delta:
			self.delta = self.set_direction()

	# add the ball and the button to the screen	
	def draw_objects(self):
		self.width = int(self.canvas["width"])		
		self.height = int(self.canvas["height"])
		self.center = (self.width/2, self.height/2)
		
		self.b = Button(self.frame, text="Start the movement!", borderwidth = 1, anchor ="center", command=self.callback, height=3)
		self.b_window = self.canvas.create_window(self.center[0], self.height, anchor = S,  window = self.b)
		
		self.top = self.canvas.create_line(0, 0, self.width, 0)		
		self.left = self.canvas.create_line(0, 0, 0, self.height)
		self.right = self.canvas.create_line(self.width, 0, self.width, self.height)
		self.bottom_before_b = self.canvas.create_line(0, self.height, self.center[0]-(self.b.winfo_reqwidth()/2), self.height)
		self.left_b = self.canvas.create_line(self.center[0]-(self.b.winfo_reqwidth()/2), self.height, self.center[0]-(self.b.winfo_reqwidth()/2), self.height-self.b.winfo_reqheight())
		self.top_b = self.canvas.create_line(self.center[0]-(self.b.winfo_reqwidth()/2), self.height-self.b.winfo_reqheight(), self.center[0]+(self.b.winfo_reqwidth()/2), self.height-self.b.winfo_reqheight())
		self.right_b = self.canvas.create_line(self.center[0]+(self.b.winfo_reqwidth()/2), self.height-self.b.winfo_reqheight(), self.center[0]+(self.b.winfo_reqwidth()/2), self.height)
		self.bottom_after_b = self.canvas.create_line(self.center[0]+(self.b.winfo_reqwidth()/2), self.height, self.width, self.height)
		
		self.ball = self.canvas.create_oval(self.center[0]-r, self.center[1]-r, self.center[0]+r, self.center[1]+r, fill="navy", outline = "navy")		

	
	# actions when app window is resized
	def resize(self, event):
		self.canvas.delete("all")
		self.canvas.configure(width = event.width, height = event.height)
		self.draw_objects()
	
	#setting direction for the ball to move (randomly)
	def set_direction(self):
		self.delta = (random.randint(-10, 10), random.randint(-10, 10))
		while self.delta[0]== 0 and self.delta[1]==0:
			self.delta = (random.randint(-10, 10), random.randint(-10, 10))

		return self.delta
	
	#Moving the ball continuously
	def callback(self):

		self.move()		
		self.canvas.after(10, self.callback)
	
	#The ball moving algorithm
	def move(self):
		current_coords = self.canvas.coords(self.ball)
		objects = self.canvas.find_overlapping(current_coords[0], current_coords[1], current_coords[2], current_coords[3])
		for obj in objects:
			if obj == self.top or obj == self.bottom_before_b or obj == self.bottom_after_b or obj == self.top_b:
				self.delta = (self.delta[0], -self.delta[1])
			elif obj == self.left or obj == self.right or obj == self.left_b or obj == self.right_b:
				self.delta = (-self.delta[0], self.delta[1])

		new_coords = (current_coords[0]+self.delta[0], current_coords[1]+self.delta[1], 
					current_coords[2]+self.delta[0], current_coords[3]+self.delta[1])
		self.canvas.coords(self.ball, new_coords)	

root = Tk()
app = App(root)
app.master.title("LPO GUI")
root.mainloop()
		
		
