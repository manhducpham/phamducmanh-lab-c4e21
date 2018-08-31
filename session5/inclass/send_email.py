from gmail import GMail, Message

mail = GMail("c4e21.pdm.test", "Manpro12babon")
msg = Message("Test gmail library", to = 'manhadhvnh@gmail.com', text = "Thu test gui mail.")
mail.send(msg)
print("Done")