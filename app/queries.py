query_user = ("""SELECT name, surname, work_from, pozition, """
              """phone, `e-mail`, access_level FROM users """
              """WHERE username= "%s" ;""")
