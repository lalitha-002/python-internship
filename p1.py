new_hieres=[('mark adams','sql analyst',4000),
            ('leslie burton','hr specialist',2300),
            ('dorothy castillo','UX designer',3100)]
def remove_sql_specialist(new_hieres):
    #if new_hieres =='sql':
    for i in new_hieres:
        for n in i:
            if 'sql' in str(n):
                 new_hieres.remove(i)
    print("new_hieres",new_hieres)
remove_sql_specialist(new_hieres)
         
