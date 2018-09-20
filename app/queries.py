query_user = ("""SELECT name, surname, work_from, pozition, """
              """phone, `e-mail`, access_level FROM users """
              """WHERE username= "%s" ;""")

time_tracking = ("""INSERT INTO time_tracking """
                """(username, registration_time, registration_status)"""
                 """VALUES (%s, %s, %s)""")

get_registration_status = (""" SELECT registration_status FROM """
                           """ time_tracking WHERE username= "%s" ORDER BY registration_time DESC LIMIT 1; """)

get_last_registration = (""" SELECT registration_time FROM """
                        """ time_tracking WHERE username= "%s" AND """
                        """ registration_status = 1 ORDER BY registration_time DESC LIMIT 1; """)
get_time_reg_today = (""" SELECT registration_time, registration_status FROM"""
                      """ time_tracking WHERE registration_time """)