import statistics
def get_student_average(students_list):
    
    dict_principal = {}
    
    global_average = [grade for student in students_list for grade in student['grades']]
    total_average =  sum(global_average) / len(global_average)
    total_average = round(total_average, 2)

    dict_principal['class_average'] = total_average

    #print(total_average)
    all_students = [{"name": student['name'], "average" : round(statistics.mean(student['grades']), 2)} for student in students_list]
    dict_principal.update({"students": all_students})
    #print(dict_principal)

    return dict_principal