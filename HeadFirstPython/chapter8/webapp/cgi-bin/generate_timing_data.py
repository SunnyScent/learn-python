import athletemodel
import yate
import cgi

athletes=athletemodel.get_from_store()
form_data=cgi.FieldStorage()
athlete_name=form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))
print(yate.header("Athlete: "+athlete_name+",Dob: "+athlete[athlete_name].dob+"."))
print(yate.para("The top times for this athlete are: "))
print
