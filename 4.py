class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False


    def add_reply(self, reply_comment):
        if not isinstance(reply_comment, Comment):
            raise TypeError("Відповідь має бути об'єктом класу Comment.")
        
        self.replies.append(reply_comment)


    def remove_reply(self):
        self.text = "Цей коментар було видалено."
        self.author = ""
        self.is_deleted = True


    def display(self, level = 0):
        indent = "    " * level

        if self.is_deleted:
            print(f"{indent}{self.text}")
        else:
            print(f"{indent}{self.author}: {self.text}")


        for reply in self.replies:
            reply.display(level + 1)


# if __name__ == "__main__":

#     root_comment = Comment("Яка чудова книга!", "Бодя")

#     reply1 = Comment("Книга повне розчарування :(", "Андрій")
#     reply2 = Comment("Що в ній чудового?", "Марина")

    
#     root_comment.add_reply(reply1)
#     root_comment.add_reply(reply2)

    
#     reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
#     reply1.add_reply(reply1_1)

    
#     reply2_1 = Comment("Повністю згоден, сюжет передбачуваний.", "Олег")
#     reply2_2 = Comment("Мені здається, ви просто не зрозуміли глибину твору.", "Ірина")
#     reply2.add_reply(reply2_1)
#     reply2.add_reply(reply2_2)

#     reply1_1_1 = Comment("Це занадто суб'єктивна оцінка. Я в захваті!", "Галина")
#     reply1_1.add_reply(reply1_1_1)

#     reply1.remove_reply()

#     print("--- Виведення коментарів ---")
#     root_comment.display()

    

        