from tkinter import *
import time


window = Tk()
window.title("Type_writer.exe")
window.minsize(height=500, width=650)
window.config(padx=20, pady=20, background="grey")

# text = '''generating random paragraphs can be an excellent way for writers to get their creative flow going at the
# beginning of the day the writer has no idea what topic the random paragraph will be about when it appears this forces
# the writer to use creativity to complete one of three common writing challenges the writer can use the paragraph as the
# first one of a short story and build upon it a second option is to use the random paragraph somewhere in a short story
# they create the third option is to have the random paragraph be the ending paragraph in a short story no matter which
# of these challenges is undertaken the writer is forced to use creativity to incorporate the paragraph into their writing
# '''

text = '''
years ago when i was younger i kinda liked a girl i knew she was mine and we were sweethearts that was then
 but then its true im in love with a fairytale even though it hurts cause i dont care if i lose my mind im already
 cursed every day we started fighting every night we fell in love no one else could make me sadder but no one else
 could lift me high above i dont know what i was doin when suddenly we fell apart nowadays i cannot find her but
 when i do well get a brand new start im in love with a fairytale even though it hurts cause i dont care if i lose
 my mind im already cursed shes a fairytale yeah even though it hurts cause i dont care if i lose my mind
 im already cursed
 '''
text_list = text.replace("\n", "").split(" ")

label = []
char = 0
x = 20
y = 20
time_end = time.time() + 10

for txt in text_list:
    char += len(txt)
    if char >= 50:
        x = 20
        y += 30
        char = len(txt)
    label_item = Label(text=txt, font=("", 15,), background="grey")
    label_item.place(x=x, y=y)

    label.append(label_item)
    x += (label_item.winfo_reqwidth())


input_entry = Entry(width=40, font=("arial", 20, ))
input_entry.place(y=y+50)
input_entry.focus()

n = 0
word = ""
type_list = []
time_end = None

num_1 = 0
ON = True
def key_press(event):
    global n, word, type_list, time_end, num_1, num_2, ON
    if ON:

        if time_end == None:
            time_end = time.time() + 60

        if time.time() < time_end:

            key = event.char

            if key == " ":

                if text_list[num_1] != word:
                    print(text_list[num_1], word)
                    label[n].config(foreground="red")

                type_list.append(word)
                word = ""
                label[n].config(background="grey")
                n += 1
                input_entry.delete(0, END)
                num_1 += 1
            elif key == "\x08":
                word = word[:-1]
                print(word)
            else:
                label[n].config(background="cyan")
                word += key
                red = False
                for char in word:
                    num_2 = word.index(char)
                    try:
                        if text_list[num_1][num_2] == char:
                            label[n].config(foreground="green")
                        else:
                            print(text_list[num_1][num_2], key)
                            red = True
                    except IndexError:
                        red = True
                if red:
                    label[n].config(foreground="red")

        else:
            input_entry.destroy()
            for item in label:
                item.destroy()

            words_per_min = 0
            print(type_list)

            for wrds in type_list:
                indx = type_list.index(wrds)

                if text_list[indx] == wrds:
                    words_per_min += 1

            wpm_label = Label(text=f"Your WPM is: {words_per_min}.", font=("Impact", 25), background="grey")
            wpm_label.pack()

            msg1_label = Label(text="The average WPM is 40", font=("arial", 15), background="grey")
            msg2_label = Label(text="But with practice people can go above 100.", font=("arial", 15), background="grey")

            msg1_label.pack()
            msg2_label.pack()

            ON = False


window.bind('<Key>', key_press)
window.mainloop()

