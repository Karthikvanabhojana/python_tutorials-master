# score = input("Enter Score: ")
# score1=float(score)
# if(score1>=0.9):
#     print("A")
# elif(score1>=0.8):
#     print("B")
# elif(score1>=0.7):
#     print("C")
# elif(score1>=0.6):
#     print("D")
# else:
#     print("F")
# x = 'banana'
# y = max(x)
# print(y)
# def stuff():
#     print('Hello')
#     return
#     print('World')
# stuff()
# largest = -1
# smallest = 100000
# while True:
#     num = input("Enter a number: ")
#     if num == "done":
#         break
#     try:
#         inum=int(num)
#         if largest < inum:
#             largest = inum
#         if smallest > inum:
#             smallest = inum
#     except:
#         print("Invalid Input")
#
# print("Maximum", largest)
# print("Minimum ", smallest)
#
text = "X-DSPAM-Confidence:    0.8475"
ipos=text.find(':')
print(ipos)
piece = text[ipos+2:]
print(piece)
value = float(piece)
print(value)
#
# people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']
#
# # def split_title_and_name(person):
# #     title = person.split()[0]
# #     lastname = person.split()[-1]
# #     return '{} {}'.format(title, lastname)
# #
# # print(list(map(split_title_and_name, people)))
#
#
# people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']
#
# def split_title_and_name(person):
#     return person.split()[0] + ' ' + person.split()[-1]
#
# #option 1
# for person in people:
#     print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))
#
# #option 2
# list(map(split_title_and_name, people)) == list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people))