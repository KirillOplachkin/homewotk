def name(*name):
    print(name)
    return list(map(lambda x: x.title(), name))

changed_name = name('kirill', 'larisa' , 'tilek')
print(changed_name)