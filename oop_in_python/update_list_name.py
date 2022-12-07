conn = "db"
cursor = conn.cursor()
def update_list_name(eligible_list_id):
    cursor.execute("select eligible_list_code from eligible_list where id = %s",eligible_list_id)
    el_code = cursor.fetchall()
    cursor.execute("select count(*) from eligible_list where eligible_list_code = %s",el_code)
    count = cursor.fetchall()
    if count == 1:
        cursor.execute("update eligble_list set list_name = %s where id = %",(el_code,eligible_list_id,))
        conn.commit()
    else:
        list_name = str(el_code)+'_'+str(count+1)
        cursor.execute("update eligble_list set list_name = %s where id = %", (list_name, eligible_list_id,))
        conn.commit()

#we may get confuse what if we have more than one beta lists but according to my knowledge
# we get them on montly basis so we will have one alphe list already exists and we will get a new beta
# list and


