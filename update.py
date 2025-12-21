import datetime

joinDate=datetime.date.fromisoformat("2017-08-23")
today=datetime.date.today()
delta=today-joinDate

replace={
    "{days}":f'{delta.days}'
    }

with open("./Readme.md","w+") as file:
    with open("./Readme_template.md","r") as template:
        templateContent=template.read()
        for i in replace:
            
            newContent=templateContent.replace(i,replace[i])
        file.write(newContent)


