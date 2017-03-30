import pymysql as mysql
import sys

# Initialize MySQL DB connection
db = mysql.connect(host="localhost", user="root",
                   passwd="root", db="learning_analytics"
                   )

def fetch_grade(id):
    """
    Fetch grades for all semesters and return in db
    """
    cursor = db.cursor()
    cursor.execute("""SELECT sem1, sem2, sem3, sem4 FROM grades WHERE userID = '%s' LIMIT 1""" % (id))
    result = list(cursor.fetchone())
    return result

def insert_grades(id, gpas):
    """
    Handle data insertion
    """
    status = None
    try:
        with db.cursor() as cursor:
            sql = "INSERT INTO grades (sem1, sem2, sem3, sem4, userID) VALUES (%f, %f, %f, %f, '%s')" % (gpas["sem1"], gpas["sem2"], gpas["sem3"], gpas["sem4"], id)
            print(sql)
            cursor.execute(sql)
            db.commit()
            status = True
    except:
        print("error happens" + sys.exec_info())
        status = False
        db.rollback()
    finally:
        return dict(status = status)
        db.close()


def fetch_average_grade():
    """
    Fetch grades for all semesters from all users
    and calculate the average among all of them for each semester
    """
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM grades""")
    total_users = cursor.rowcount

    results = list(cursor.fetchall())

    # avg_sem = dict(sem1 = 0, sem2 = 0, sem3 = 0, sem4 = 0)
    avg_sem = [0,0,0,0]

    for gpa in results:
        gpa = list(gpa)
        avg_sem[0] += gpa[0]
        avg_sem[1] += gpa[1]
        avg_sem[2] += gpa[2]
        avg_sem[3] += gpa[3]

    for i in range(0,4):
        avg_sem[i] = avg_sem[i] / total_users

    all_sem = (( avg_sem[0] + avg_sem[1] + \
                  avg_sem[2] + avg_sem[3]  ) \
                  / 4
                )

    return avg_sem, all_sem
