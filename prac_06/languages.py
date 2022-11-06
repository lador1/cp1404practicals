from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

programs = [python, ruby, visual_basic]


print(python)
print(ruby)
print(visual_basic)

#

print("Dynamically typed languages are:")

for program in programs:
    if program.is_dynamic():
        print(program.field)