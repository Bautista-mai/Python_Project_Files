name = input("Enter your is your name? ")

print("----------------------------------------------------------------------------------------")

p_lims = int(input("enter your score in Prelims: "))
m_terms = int(input("Enter your score in Midterm: "))
s_f = int(input("Enter your score in Semi-Finals: "))
Finals = int(input("Enter your score in Final: "))
quiz =int(input("Enter your score in Quizes: "))
p_ject = int(input("Enter your score in Projects: "))

print("---------------------------------------------------------------------------------------------")
Final_Grade = (p_lims * 0.15) + (m_terms * 0.15) + (s_f * 0.15) + (Finals * 0.15) + (quiz * 0.15) + (p_ject * 0.15)
print(round(Final_Grade,2))

print(f"Good Day! {name} your Final grade is : {Final_Grade}")

if Final_Grade >=100:
    print("Congratulations!! You made it!, And You're  a fantastic student! Goodjob!!")
elif Final_Grade >= 75:
    print("Conratulations!! You passed, But still you need to improve or maintain your grade. ")
else:
    print("Sorry to say that you are failed. Try again next year. It's never too late")    