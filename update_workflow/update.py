import datetime

joinDate=datetime.date.fromisoformat("2017-08-23")
today=datetime.date.today()
deltaYear=today.year-joinDate.year

replace={
    "{years}":f'{deltaYear}'
}

with open("./Readme.md","w+") as file:
    with open("./update_workflow/Readme_template.md","r") as template:
        templateContent=template.read()
        for i in replace:
            newContent=templateContent.replace(i,replace[i])
        file.write(newContent)


